num1 = int(input("Enter the 1st number: "))
num2 = int(input("Enter the 2nd number: "))
primes = []
for i in range(num1, num2+1):
    flag = 0
    if i < 2:
        continue
    if i == 2:
        primes.append(2)
        continue
    for x in range(2, i):
        if i % x == 0:
            flag = 1
            break
    if flag == 0:
        primes.append(i)
print(primes)