stockPrice = [45, 24, 35, 31, 40, 38, 11]
def findMaxStock (arr) :
    minStock = arr[0]
    maxStock = arr[0]
    for indx , price in enumerate(arr) :
        if price < minStock and indx != len(arr) - 1 :
            maxStock = minStock
            minStock = price
        elif price > maxStock :
            maxStock = price

        if maxStock == 0 :
            maxStock = minStock
        print(maxStock , '--', minStock)

    profit = maxStock - minStock
    return profit if profit > 0 else -1
print(findMaxStock(stockPrice))
