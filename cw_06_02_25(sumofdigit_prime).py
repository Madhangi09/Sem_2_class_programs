#sum of digit and add prime numbers
def is_prime(p):
    if p<2:
        return False
    if p==2:
        return True
    for i in range(2,p):
        if p%i==0:
            return False
    return True
#logic to find the total
def sum_digits(s):
    total=0
    for i in str(s):  #it will covert into string      
        if is_prime(int(i)): #function call
            total+=int(i)
    return total
n=int(input())
result=sum_digits(n)#function call
print(result)


