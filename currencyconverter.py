with open("currencyconverterdata.txt") as f:
    lines= f.readlines()


curencyDict={}
for line in lines:
   parsed = line.split("\t")
   curencyDict[parsed[0]]=parsed[1]



amount=int(input("enter amount:\n"))
print("enter the name of the currency you want to convert this amount to? Available Options:\n")
[print(item) for item in curencyDict.keys()]
currency=input("please enter one of these values\n")
print(f"{amount} INR is equal to {amount* float(curencyDict[currency])} {currency}")
