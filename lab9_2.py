A = set(range(1, 251))

n = int(input('Введіть число: '))

divisors = set()

for i in A:
    if n % i == 0:
        divisors.add(i) 
       
result = A - divisors

print(divisors)
print()
print(result)