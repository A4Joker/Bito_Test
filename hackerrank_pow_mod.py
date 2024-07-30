n = list(map(int, input("enter values a , b ,m -:").split()))
print(pow(n[0], n[1]))
if (len(n) == 3) and (n[1] >= 0):

    print(pow(n[0], n[1], n[2]))
else:
    print(f"Value of {n[1]}cannot be negative")