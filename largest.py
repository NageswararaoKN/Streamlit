def largest(n1,n2,n3):
     mx = (n1 if (n1 > n2 and n1 > n3) else
          (n2 if (n2 > n1 and n2 > n3) else n3))
     return mx

n1=int(input())
n2=int(input())
n3=int(input())

print("Largest number among " + str(n1) + ", " + str(n2) + " and " + str(n3) + " is " + str(largest(n1,n2,n3)))
