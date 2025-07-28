print('Hello World')

print('This is a Python script.')

#Write a program to print primary numbers from 1 to 200
print('primary numbers from 1 to 200')
for num in range(1,201):
    if num > 1:
        for i in range(2, int(num**0.5) + 1):
            if (num % i) == 0:
                break
        else:
            print(num, end=' ') 


#Write a program for Fibonacci series, i want to print the values in console
print('\nFibonacci series up to 200:')      
a, b = 0, 1
while a < 200:
    print(a, end=' ')
    a, b = b, a + b     


