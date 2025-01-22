customer_name = input("Enter your name: \n")   #Get the customer's name
sum = 0
with open("bill_history.txt","a") as file:   #Open the file in append mode
    file.write(f"Customer Name: {customer_name}\n")   #Write the customer's name at the beginning of the file
    while(True):
        item_name = (input("Enter the item name (or press q to quit): \n"))
        if(item_name != 'q'):
            item_price = input(f"Enter the price of {item_name}: \n")
            sum=sum+int(item_price)
            file.write(f"Item:{item_name}, Price:{item_price}, Total bill so far: {sum}\n")   #Write the item name, price and total bill so far in the file
            print(f"Your total bill so far is: {sum}")
        else:
            file.write(f"Final total bill: {sum}\n")   #Write the final total bill in the file
            file.write("\n")   #Add a new line between the bills of different customers
            print(f"Your total bill is {sum}. Thanks for shopping with us.")
            break
