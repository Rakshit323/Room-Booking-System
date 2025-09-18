class Hotel: 
    def __init__(self): 
        self.bookings = {} 
        self.roomprices = {'Standard': 2000, 'Deluxe': 3500, 'Suite': 5000} 
        self.serviceprices = {'Food': 500, 'Laundry': 300, 'Cleaning': 200, 'Extra Bed': 700, 'Airport Pickup': 1500} 
        self.allrooms = [] 
        roomnumber = 101 
        while len(self.allrooms) < 100: 
            self.allrooms.append(str(roomnumber)) 
            roomnumber += 1 
 
    def bookroom(self): 
        roomno = input("Enter Room Number: ") 
        if roomno in self.bookings.keys(): 
            print("Room already booked.") 
            return 
        if roomno not in self.allrooms: 
            print("Invalid Room Number.") 
            return 
        guestname = input("Enter the name of guest: ") 
        print("\nRoom Types:") 
        i = 1 
        for key, value in self.roomprices.items(): 
            print(i, ".", key, "- ₹", value) 
            i += 1 
        try: 
            choice = int(input("Choose Room Type (1-3): ")) 
            roomtype = list(self.roomprices.keys())[choice - 1] 
        except (ValueError, IndexError): 
            print("Invalid choice.") 
            return 
        self.bookings[roomno] = {'name': guestname, 'roomtype': roomtype, 'roomprice': 
self.roomprices[roomtype], 'services': [], 'servicebill': 0} 
        print("Room", roomno, "booked for", guestname) 
 
    def addservice(self): 
        roomno = input("Enter Room Number: ") 
        if roomno not in self.bookings.keys(): 
            print("No booking for this room.") 
            return 
        print("\nAvailable Services:") 
        i = 1 
        for key, value in self.serviceprices.items(): 
            print(i, ".", key, "- ₹", value) 
            i += 1 
        try: 
            choice = int(input("Choose service (1-5): ")) 
            servicename = list(self.serviceprices.keys())[choice - 1] 
        except (ValueError, IndexError): 
            print("Invalid choice.") 
            return 
        price = self.serviceprices[servicename] 
        self.bookings[roomno]['services'].append(servicename) 
        self.bookings[roomno]['servicebill'] += price 
        print("Added", servicename, "to Room", roomno, "Total Service Bill: ₹", 
self.bookings[roomno]['servicebill']) 
 
    def viewbill(self): 
        roomno = input("Enter Room Number: ") 
        if roomno not in self.bookings.keys(): 
            print("No booking for this room.") 
            return 
 
        data = self.bookings[roomno] 
        total = data['roomprice'] + data['servicebill'] 
 
        print("\nBill Summary") 
        print("Guest Name:", data['name']) 
        print("Room Type:", data['roomtype'], "- ₹", data['roomprice']) 
 
        if len(data['services']) > 0: 
            services = "" 
            for service in data['services']: 
                services += service + ", " 
            services = services[:-2] 
            print("Services Used:", services) 
        else:
            print("Services Used: None") 
        print("Service Charges: ₹", data['servicebill']) 
        print("Total Bill: ₹", total) 
 
    def cancelbooking(self): 
        roomno = input("Enter Room Number to cancel: ") 
        if roomno in self.bookings.keys(): 
            self.bookings.pop(roomno) 
            print("Booking for Room", roomno, "cancelled.") 
        else: 
            print("No booking for this room.") 
 
    def viewallbookings(self): 
        if len(self.bookings.keys()) == 0: 
            print("No bookings available.All rooms are empty :( ") 
            return 
        print("\nAll Bookings:-") 
        for key, value in self.bookings.items(): 
            services = "None" 
            if len(value['services']) > 0: 
                services = "" 
                for service in value['services']: 
                    services += service + ", " 
                services = services[:-2] 
            print("Room:", key, ", Guest:", value['name'], ", Type:", value['roomtype'], ", Services:", services) 
 
    def menu(self): 
        while True: 
            print("\nHotel Management System:-") 
            print("Rooms - 101 to 200") 
            print("1. Book Room") 
            print("2. Add Room Service") 
            print("3. View Guest Bill") 
            print("4. Cancel Booking") 
            print("5. View All Bookings") 
            print("6. Exit") 
            choice = input("Enter your choice: ") 
            if choice == '1': 
                self.bookroom() 
            elif choice == '2': 
                self.addservice() 
            elif choice == '3': 
                self.viewbill() 
            elif choice == '4': 
                self.cancelbooking() 
            elif choice == '5': 
                self.viewallbookings() 
            elif choice == '6': 
                print("THANKS!") 
                break 
            else:
                print("Invalid choice.") 
 
hotel = Hotel() 

hotel.menu() 
