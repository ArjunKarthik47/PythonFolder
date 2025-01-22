#Currency Convertor

with open('CurrencyData.txt') as f:
    lines=f.readlines()

CurrencyDict={}
for line in lines:
    parsed=line.split("\t")
    CurrencyDict[parsed[0]]=parsed[1]

Amount=int(input("enter Amount:\n"))
print("Enter the name of the cuurency you want to convert this amount to? Available Options:\n")
[print(item) for item in CurrencyDict.keys()]
Currency=input("Please enter one of these values:\n")
print(f"{Amount} INR is equal to {Amount * float(CurrencyDict[Currency])} {Currency}")