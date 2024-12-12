import random
import re
class Customer:
    def __init__(self,cust_id,name,phno):
        self.cust_id=ciust_id
        self.name=name
        self.phno=phno
    def gen_rand_id(self):
        c_id=random.randint(1000,9999)
        return f"TICK{c_id}"
    def verify_customer_id(cust_id):
        length=len(cust_id)
        number=0
        uppercase=0
        for i in cust_id:
            if i.isdigit():
                number+=1
            else:
                uppercase+=1
        if length>=8 and number>=4 and cust_id[0:4]=="TICK":
            print("Valid Customer_id")
        else:
            print("Invalid Customer_id")
class TicketBooking:
    def __init__(self):
        self.events={"Concert":{"price":100,"seats":100},"Movie":{"price":150,"seats":1000},"Drama":{"price":500,"seats":600}}
        self.booked_tickets=[]
    def view_events():
        for events,details in self.events.items():
            print(f"{events}:{details['Price'],details['Seats']} Seats are available")
            print("Concert",100,100)
            print("Movie",120,1000)
            print("Drama",500,600)
    def book_tickets():
    def view_tickets():
book=       
print("*****Welcome to  TICKET Bokking apllication*****")
cust_id=input("Enter the customer id:")
if Customer.verify_customer_id(cust_id):
    name=input("Enter your name:")
    phno=int(input("Enter your phone number:")
    customer=Customer(cust_id,name,phno)
    print("Valid!!! View the booking details") #or print("****Booking Details****")
else:
    print("Invalid!!!Please Register")
    name=input("Enter your name:")
    phno=int(input("Enter your phone number:")
    cust_id=gen_rand_id()
    customer=Customer(cust_id,name,phno)
    print("Your Customer id is:",cust_id)
while True:
    print("***Booking Info***")
    print("\n1.View Events")
    print("\n2.Book Tickets")
    print("\n3.Vie my tickets")
    print("\n4.Exit")
    choice=int(input("Enter any optical to continue booking"))
    if choice==1:
        book.view_events()
    elif choice==2:
        event_name=input("Enter any event:")
        quantity=int(input("Enter the number of tickets"))
        
        
    
