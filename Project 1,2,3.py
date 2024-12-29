#Multiples of 3 and 5 below a number
'''
number = 10;
i = 1;
sum = 0
while i < number :
    if i % 3 == 0 :
        sum = sum + i 
        i = i + 1
    elif i % 5 == 0 :
        sum = sum + i
        i = i + 1
    else : i += 1

print(sum)
'''

# Even Fibonacci numbers: Starting on with 1 & 2, do Fib. and get sum of even terms below 4x10**6

'''
#For Fib
n1,n2 = 1,2
print(n1,n2)

n_i = n1 + n2
print(n_i)
n_aux = n2
n_aux1 = 0
limit = 4000000
sum = n2

while n_i < limit:
    n_aux1 = n_i
    n_i = n_aux + n_i
    n_aux = n_aux1
   # print(n_i)
    if n_i % 2 == 0:
        sum = sum + n_i

print("this the sum:",sum)

'''

#Largest prime factor
'''heck if number is prime

number = 997
i = 2
while i <= number**0.5 and (number % i != 0) :
    i += 1
if number % i == 0 :
    print(number,"is not prime")
else : print(number, "is prime")

'''

''' IN THEORY THIS WORKS, BUT TAKES TOOOOOO LONG
# For all numbers that divide number
number = 600851475143
j = 2
#list = []
primes = []
while j <= number :
    if number % j == 0 :
        p = 2
        while (j % p != 0) and p <= j**0.5 : #Just to check if j is prime
            p += 1
        if j % p != 0:
            primes.append(j)
            j += 1
    j += 1
print(primes)
'''


'''
# From all divisors, take primes
for x in list:
    p = 2
    while (x % p != 0) and p <= x**0.5 :
        p += 1
    if x % p != 0:
        primes.append(x)

print(max(primes))

'''
number = 600# 851475143
pn = 2
divisors = []

while True:
    while number % pn != 0:
        pn += 1
    divisors.append(pn)
    number = number / pn
    x = 2
    while number % x != 0 and (x < number**0.5) :
        x += 1
    if number % x != 0:
        divisors.append(number)
        break
    pn = 2
    
print(divisors)

for x in divisors:
    j = 2
    while x % j != 0 and j < x**0.5:
        j += 1
    if x % j != 0:
        print(x, "is prime")
    
'''
# USING BASIC PRIME DECOMPOSITION: find lowest divisor, then divide by it and so on
number = 49*5*9
prime = 2
while prime <= number**0.5 and number % prime != 0: #This will break at my lowest divisor
    prime += 1

new_number = number % prime

print(prime)
'''



