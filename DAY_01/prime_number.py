num = int(input("Enter a number: "))
flag = 0
if num < 2:
    flag = 1
else:
    for i in range(2, num):
        if num % i == 0:
            flag = 1
            break
if flag == 1:
    print(f"{num} is not a prime number.")
else:
    print(f"{num} is a prime number.")