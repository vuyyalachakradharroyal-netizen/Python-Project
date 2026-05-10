import random
import time

# Move symbols to a constant for easier editing
SYMBOLS = ['🍎', '🍌', '🍍', '🥭', '🍒']

def spin_row():
    return [random.choice(SYMBOLS) for _ in range(3)]

def print_row(row):
    print("\n  " + " | ".join(row) + "  \n")

def get_payout(row, bet):
    payouts = {
        '🍒': 10,
        '🍌': 9,
        '🍎': 5,
        '🥭': 3,
        '🍍': 1
    }
    if len(set(row)) == 1:
        return bet * payouts[row[0]]
    return 0

def main():
    balance = 1000

    print("----------------------------")
    print("  Welcome To Python Slots 🎰")
    print("  Multipliers: 🍒x10 🍌x9 🍎x5")
    print("----------------------------")

    while balance > 0:
        print(f"Current Balance: ${balance}")

        try:
            bet = int(input("Enter bet amount: "))
        except ValueError:
            print("❌ Invalid input! Please enter a number.")
            continue

        if bet > balance:
            print("❌ Insufficient funds!")
            continue
        if bet <= 0:
            print("❌ Bet must be greater than 0.")
            continue

        balance -= bet
        print("Spinning...", end="",)
        
        # Adding a tiny delay for "suspense"
        for _ in range(3):
            time.sleep(0.4)
            print(".", end="",)
        print()

        row = spin_row()
        print_row(row)

        payout = get_payout(row, bet)

        if payout > 0:
            print(f"🎉 WINNER! You won ${payout}")
        else:
            print("😢 No match. Better luck next time!")

        balance += payout

        if balance <= 0:
            print("You've run out of money!")
            break

        play_again = input("Spin again? (Y/N): ").upper()
        if play_again != "Y":
            break

    print(f"\nGame Over! Final Balance: ${balance}")
    print("Thanks for playing!")

if __name__ == "__main__":
    main()