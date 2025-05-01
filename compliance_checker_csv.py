import pandas as pd

# Load portfolio data from CSV
df = pd.read_csv("portfolio.csv")

# Calculate total value for each asset
df["Value"] = df["Quantity"] * df["Price"]

# Calculate total portfolio value
total_value = df["Value"].sum()

# Check compliance: No asset > 25% of total
print("📊 Portfolio Compliance Report")
print(f"Total Portfolio Value: ${total_value:.2f}\n")

compliant = True

for index, row in df.iterrows():
    percentage = (row["Value"] / total_value) * 100
    print(f"{row['Symbol']}: ${row['Value']:.2f} ({percentage:.2f}%)")

    if percentage >= 25:
        print(f"❌ COMPLIANCE BREACH: {row['Symbol']} exceeds 25% limit!\n")
        compliant = False

if compliant:
    print("✅ Portfolio is compliant with the 25% rule.")
else:
    print("⚠️ Portfolio is NOT compliant.")
