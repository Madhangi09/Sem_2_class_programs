#reverse a string without using in-built functions
k=input("Enter a string :").strip()  #strip() is used for removing spaces
length=0
reverse=""
for i in k:
    length+=1
for i in range(length-1,-1,-1):  #(5,-1,-1)
    reverse+=k[i]
    print("The reversed string is :",reverse) #this print statement will print step-by-step

#same method with different print statement atlast
k=input("Enter a string :").strip()  #strip() is used for removing spaces
length=0
reverse=""
for i in k:
    length+=1
for i in range(length-1,-1,-1):  #(5,-1,-1)
    reverse+=k[i]
print(f"The reversed string is : {reverse}") #this statement will print the final answer

#same thing with method call
def reverse_string():
    length=0
    reverse=""
    for i in k:
        length+=1
    for i in range(length-1,-1,-1):  #(5,-1,-1)
        reverse+=k[i]
    print(reverse)
k=input("Enter a string :").strip()  #strip() is used for removing spaces
reverse_string()

#same without parameter
def reverse_string():
    length=0
    reverse=""
    for i in k:
        length+=1
    for i in range(length-1,-1,-1):  #(5,-1,-1)
        reverse+=k[i]
    return reverse
k=input("Enter a string :").strip()  #strip() is used for removing spaces
rev=reverse_string(k)
print(f"The reversed string is :",rev)

#replace the letter in a given string
input_string=input("Enter the string :").strip()
to_replace=input("Enter a character to replace :")
replace_with=input("Enter the character to replace with :")
replaced_string=""
for c in input_string:
    if c==to_replace:
        replaced_string+=replace_with
    else:
        replace_string+=c
print("Replaced string is :",replaced_string)






























































