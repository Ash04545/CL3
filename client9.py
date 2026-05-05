import xmlrpc.client

proxy = xmlrpc.client.ServerProxy("http://localhost:8000/")

print("1. Book Room")
print("2. Cancel Booking")

choice = int(input("Enter choice: "))
guest = input("Enter guest name: ")

if choice == 1:
    print(proxy.book_room(guest))

elif choice == 2:
    print(proxy.cancel_booking(guest))