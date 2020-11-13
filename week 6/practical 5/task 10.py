prices = ()

for i in range(5):
    Price = input("Enter price of sweet ")
    prices += (int(Price[:-1]),)

TotalPrice = sum(prices)
AveragePrice = sum(prices)/len(prices)
HighestPrice = max(prices)
LowestPrice = min(prices)

print("Total price:", TotalPrice, '\n'
      "Average price:", AveragePrice, '\n'
      "Highest price:", HighestPrice, '\n'
      "Lowest price", LowestPrice)