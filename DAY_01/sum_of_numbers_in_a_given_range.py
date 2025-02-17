num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
sum = 0
for i in range(num1, num2+1):
    sum += i
print(f"The sum is {sum}")