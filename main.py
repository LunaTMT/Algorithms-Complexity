#Basic Recursive Program    - 21/01/2022 - Taylor Threader

def recusive(n, b):
    if n == 1:  # basecase
        print(b)
        return False
    else:  # recursive func
        print(b ** n)
        recusive(n - 1, b)


if __name__ == '__main__':
    n = input("Enter exponent (power) : ")
    n = int(n)


    b = input("Enter base value : ")
    b = int(b)

    recusive(n, b)
