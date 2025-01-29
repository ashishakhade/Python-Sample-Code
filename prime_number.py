num =int(input("Enter a number: "))
# prime number is greater than 1 and it is not divisible by any number between 2 and square root of the number(+1 is used to include the square root number)
if num>1 and all(num%i!=0 for i in range(2,int(num**0.5)+1)): 
    print(f"{num} is a prime number")
else:
    print(f"{num} is not a prime number")