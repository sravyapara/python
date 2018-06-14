class Person:   #define the class person
    def __init__(self,name,phone): #define the constructor with params as name and phno
        self.name=name #map the name and phonno
        self.phone=phone
    def showDetails(self): #displays the persons name and phoneno

        print("Name:",self.name)
        print("PhoneNo:",self.phone)

class employee(Person):
    def __init__(self,name,phone,emp_id):
        Person.__init__(name,phone)
        self.emp_id = emp_id

    def showDetails(self): #override showDetails from person class
        print("Employee Details:")
        Person.showDetails(self) #displays the Employee details
        print("Employee Id:",self.emp_id)

class Passenger(Person):  #define the Passenger class that inherits person class
    def __init__(self,name,phone,passenger_id,seat_id): ##define constructor with params student id
        super().__init__(name,phone) #calls the super class constructor
        self.passenger_id=passenger_id #map the passenger id
        self.seat_id=seat_id #map the seat id


    def showDetails(self): #override showDetails from person class
        print("passenger Details:")
        Person.showDetails(self) #displays the student details
        print("Passenger Id:",self.passenger_id)
        print("Seat details",self.seat_id)

class Flight(Passenger):   #defines the book class

    def __init__(self,name,phone,passenger_id,seat_id,flightno): #defines the constructor to map bookdetails
        Passenger.__init__(self,name,phone,passenger_id,seat_id)
        self.flightno=flightno

    def __showDetails(self):
#displays the details of the book
        Passenger.showDetails(self)
        print("Flight Number:",self.flightno)
k=0
# Allow user to enter how many passenger are there
c=int(input("enter how many passengers:"))

# List for creating Instances
pilist={}
# List for passengers
plist=[]
#
for j in range(0,c):
    d = input("enter the passenger details")
    plist.append(d)
for details in plist:
    text=details.split()
    print("Passanger %s Details :" % str(k+1))
    pilist[k]=Passenger(text[0],text[1],text[2],text[3])
    pilist[k].showDetails()
    k+=1



