def largest(n1,n2,n3):
    mx = (n1 if (n1 > n2 and n1 > n3) else
          (n2 if (n2 > n1 and n2 > n3) else n3))
    return mx

num1=int(input())
num2=int(input())
num3=int(input())

print("Largest number among " + str(num1) + ", " + str(num2) + " and " + str(num3) + " is " + str(largest(num1,num2,num3)))
