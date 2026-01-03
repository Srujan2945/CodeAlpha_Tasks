# Stock Portfolio Tracker

# Hardcoded stock prices
stock_prices = {
    "AAPL": 180,     # Apple
    "TSLA": 250,     # Tesla
    "GOOG": 140,     # Google (Alphabet)
    "MSFT": 310,     # Microsoft
    "AMZN": 155,     # Amazon
    "META": 350,     # Meta (Facebook)
    "NFLX": 480,     # Netflix
    "NVDA": 720,     # NVIDIA
    "ORCL": 120,     # Oracle
    "IBM": 165,      # IBM
    "INTC": 45,      # Intel
    "AMD": 150,      # AMD
    "ADBE": 560,     # Adobe
    "SAP": 185,      # SAP
    "UBER": 70,      # Uber
    "DIS": 95,       # Disney
    "PYPL": 65,      # PayPal
    "SHOP": 80,      # Shopify
    "BABA": 75,      # Alibaba
    "TCS": 3900,     # Tata Consultancy Services (India)
    "INFY": 1650,    # Infosys (India)
    "WIPRO": 520,    # Wipro (India)
    "RELIANCE": 2900 # Reliance Industries (India)
}

portfolio = {}
total_investment = 0

print("📈 Welcome to Stock Portfolio Tracker")
print("Available stocks and prices:")
for stock, price in stock_prices.items():
    print(f"{stock} : ₹{price}")


print("\nEnter stock details (type 'done' to finish):")

# Input loop
while True:
    stock_name = input("Enter stock name: ").upper()

    if stock_name == "DONE":
        break

    if stock_name not in stock_prices:
        print("❌ Stock not available. Please choose from the list.\n")
        continue

    try:
        quantity = int(input("Enter quantity: "))
        if quantity <= 0:
            print("❌ Quantity must be greater than zero.\n")
            continue
    except ValueError:
        print("❌ Please enter a valid number.\n")
        continue

    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity
    print("✅ Stock added successfully!\n")


# Calculate total investment
print("\n📊 Portfolio Summary:")
print("----------------------")

for stock, qty in portfolio.items():
    investment = stock_prices[stock] * qty
    total_investment += investment
    print(f"{stock} | Quantity: {qty} | Value: ₹{investment}")

print("----------------------")
print(f"💰 Total Investment Value: ₹{total_investment}")

