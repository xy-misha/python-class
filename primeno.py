num = int(input("Enter a number: "))
def is_prime(n):
    if n<2:
        print(f"{n} is not a prime number")
    else:
        for i in range(2,n):
            if n%i == 0:
                print(f"{n} is not a prime number")
                break
        else:
            print(f"{n} is a prime number")
is_prime(num)
num =int(input("Enter a number: "))
def is_prime(n):
    if n<2:
        print(f"{n} is not a prime number")
    else:
        for i in range (2, n):
            if n %1 ==0:
                print(f"{n} is not a prime number")
                break
        else:
            print(f"{n} is a prime number")
is_prime(num)