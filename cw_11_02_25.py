#to print a pyramid with gap
def hollow_pyramid(n):
    for i in range(1,n+1):
        space=" "*(n-i)  #space calculation for the 1st row
        if i==1:
            print(space+"*")
        elif i==n:
            print("*"*(2*n-1))
        else:
            print(space+"*"+" "*(2*i-3)+"*")  #middle rows ---> space+*+space+*
n=int(input())
hollow_pyramid(n)  #function call

#to print without gap
def hollow_pyramid(n):
    for i in range(1,n+1):
        space=" "*(n-i)  #space calculation for the 1st row
        if i==1:
            print(space+"*")
        elif i==n:
            print("*"*(2*n-1))
        else:
            print(space+"*"+"*"*(2*i-3)+"*")  #middle rows ---> space+*+space+*
n=int(input())
hollow_pyramid(n)  #function call

#to print 1 to 5 in a pyramid
n=5
for i in range(1,n+1):
    print(" "*(n-i),end="")
    for j in range(1,i+1):
        print(j,end="")
    for j in range(i-1,0,-1):
        print(j,end="")
    print()
