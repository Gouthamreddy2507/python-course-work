seats = {
    "U1":{"booking_status": True,  "gender":"M" ,"price":1233, "seat_type":"sleeper","name":"goutham"},
    "U3":{"booking_status": True,  "gender":"F" ,"price":1233, "seat_type":"sleeper","name":"soul"},
    "U4":{"booking_status": True,  "gender":"M" ,"price":1000, "seat_type":"sleeper","name":"vishwa"},
    "U6":{"booking_status": False,  "gender":"F" ,"price":1233, "seat_type":"sleeper","name":None},
    "L2":{"booking_status": False,  "gender":None ,"price":1233, "seat_type":"sleeper","name":"strange"},
    "L7":{"booking_status": True,  "gender":"F" ,"price":1233, "seat_type":"sleeper","name":"nikhil"},
    "L8":{"booking_status": True,  "gender":"M" ,"price":1233, "seat_type":"sleeper","name":"lenin"},
    "L9":{"booking_status": False,  "gender":None ,"price":1233, "seat_type":"sleeper","name":"chapri"},
    "L10":{"booking_status":True,  "gender":None ,"price":1233, "seat_type":"sleeper","name":"varma"}
    }
for i in seats:
    if seats[i]['booking_status']:
        if seats[i]["gender"]=="M":
            print(f"{i} - M")
        else:
            print(f"{i}-F")
    else:
        print(f"{i}-{seats[i]["price"]}")

selected_seat = input("enter the seat number: ").upper()
if selected_seat in seats:
    if seats[selected_seat]["booking_status"]:
        print("seat is already booked> Try with other one")
    else:
        seats[selected_seat]["booking_status"]=True
        seats[selected_seat]["name"] = input("enter the name: ")
        seats[selected_seat]["gender"]=input("enter the gender(F or M): ")
        seats[selected_seat]["age"] = int(input("enter the age: "))

        if seats[selected_seat]["age"] < 5:
            print(f"Hello {seats[selected_seat]["name"]}\nYou have booked your seat")
        elif seats[selected_seat]["age"] < 60:
            payment = int(input(f"enter the payment: {seats[selected_seat]["price"]}"))
            if payment==seats[selected_seat]["age"]:
                print(f" Hello {seats[selected_seat]["name"]}\nYou have booked")
            else:
                print("Payment process failed. Try again")
        else:
            print(f"You have booked the seat-{selected_seat}")
else:
    print("Enter the proper seat number: ")
        


