# Part 1 - Calculate the factorial of a given number
# Part 2 - Calculate the number of trailing zeroes in the factorial of a given number


def factorial(number):
    if number == 0 or number == 1:
        return 1
    else:
        return number * factorial(number - 1)
def factorialTrailingZeroes(number):
    count = 0
    i = 5
    while(number//i !=0):
        count = count + int(number/i)
        i = i*5
    return count
    
    # fac=factorial(number)
    # print(fac)
    # count=0
    # while(fac%10==0):
    #     count+=1
    #     fac=fac//10
    # return count


if __name__ == "__main__":
    number = int(input("Enter the number: \n"))
    fac = factorial(number)
    print(f"The factorial is {fac}")
    print(factorialTrailingZeroes(number))