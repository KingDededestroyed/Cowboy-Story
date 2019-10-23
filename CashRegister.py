#Seth Jones
#Cash Register Assignment
#09/09/2019

numItems = 4
costPerItem = 10.00
taxRate = 0.08
subTotal = numItems * costPerItem
taxAmount = taxRate * subTotal
totalCost = taxAmount + subTotal
print("SALES RECEIPT")
print("Number of items :",numItems)
print("Cost per item : " + "$" + str(costPerItem))
print("Tax rate :",taxRate)
print("Tax amount: " + "$" + str(taxAmount))
print("TOTAL SALE PRICE: " + "$" + str(totalCost))
