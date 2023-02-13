class Trains:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def getStatus(self):
        print(f'{self.name} has total {self.seats} seats available ')
    def getFare(self):
        print(f'Price of the train is {self.fare}')
    def bookTicket(self):
        if (self.seats>0):
            print('Your ticket is booked and your seat number is ',self.seats)
            self.seats=(self.seats)-1
        else:
            print("Train is full!")
    def cancelTicket(self):
        print("Your Ticket is cancelled successfully")
        self.seats=(self.seats)+1

    

intercity=Trains("InterCity Express",120,2)
intercity.getStatus()
intercity.getFare()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.bookTicket()
intercity.cancelTicket()
intercity.bookTicket()
intercity.bookTicket()