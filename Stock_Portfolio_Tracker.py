print("========== STOCK PORTFOLIO TRACKER ==========\n")

stocks = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOG": 150,
    "MSFT": 420,
    "AMZN": 170,
    "META": 510,
    "NVDA": 145,
    "NFLX": 690,
    "AMD": 165,
    "INTC": 35
}

total_cost = 0

print("Available Stocks:\n")
for i in stocks:
    print(i, ":", f"${stocks[i]}")

print()

while True:

    user_input = input("Enter stock name: ").upper()

    if user_input in stocks:

        stock_rate = stocks[user_input]

        quantity = int(input("Enter quantity: "))

        cost = stock_rate * quantity

        total_cost += cost

        print(f"\n{user_input} x {quantity} = ${cost}")
        print(f"Current Total = ${total_cost}\n")

        choice = input("Do you want to add another stock? (Y/N): ").upper()

        if choice == "N":
            break

    else:
        print(" Invalid stock name. Please try again.\n")
print("\n========== PORTFOLIO SUMMARY ==========")
print(f"Current Investment = ${total_cost}")

try:
    with open("portfolio.txt", "r") as file:
        previous_total = int(file.read())
except (FileNotFoundError, ValueError):
    previous_total = 0

grand_total = previous_total + total_cost

with open("portfolio.txt", "w") as file:
    file.write(str(grand_total))

print("\n========== INVESTMENT SUMMARY ==========")
print(f"Previous Investment : ${previous_total}")
print(f"Current Investment  : ${total_cost}")
print(f"Grand Total         : ${grand_total}")