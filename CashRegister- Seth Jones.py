#Seth Jones
#Cash Register Assignment
#09/09/2019

#Declare and initialize variables
numItems = 5
costPerItem = 80.00
taxRate = 0.08

#Calculate and store the sub-total
subTotal = numItems * costPerItem

#Calculate the amount of tax and store the result
taxAmount = taxRate * subTotal

#Calculate the total price and store the amount
totalCost = taxAmount + subTotal

#Show the full receipt to the screen
print("SALES RECEIPT")
print("Number of items :",numItems)
print("Cost per item   : " + "$" + str(costPerItem))
print("Tax rate        :",taxRate)
print("Tax amount      : " + "$" + str(taxAmount))
print("TOTAL SALE PRICE: " + "$" + str(totalCost))
