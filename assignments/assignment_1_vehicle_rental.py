#vehicle rental

rental_id = int(input("Enter Rental ID: "))
customer_name = input("Enter Customer Name: ")
rental_cost = float(input("Enter Rental Cost: ₹"))
vehicle_types = input("Enter Vehicle Types (comma-separated): ").split(",")

booked_hours = int(input("Enter Booked Hours: "))
used_hours = int(input("Enter Used Hours: "))
usage_record = (booked_hours, used_hours)
damage_liability = float(input("Enter Damage Liability Percentage: "))
accessories = input("Enter Accessories Requested (comma-separated): ").split(",")
documents = input("Enter the documents: ").split(",")

agency = {
    'Name': input("Enter Agency Name: "),
    'contact_no': input("Enter Agency Hotline: "),
    'Address': input("Enter Agency Address: ")
}

advance_payment = float(input("Enter advance amount given: "))
pending_payment = float(input("enter remaining amount: "))

print("Rental ID, Name, Cost:", rental_id, customer_name, rental_cost, sep=", ")


print("Damage Liability: %.2f%%" % damage_liability)


print(f"Customer: {customer_name}")
print(f"Vehicle Types: {', '.join(vehicle_types)}")
print(f"Booked: {usage_record[0]} hrs, Used: {usage_record[1]} hrs")
print(f"Accessories Requested: {', '.join(accessories)}")


print("Agency Info: Name - {}, contact - {}, Address - {}".format(
    agency['Name'], agency['contact_no'], agency['Address']))


print(f"advance payment done : ₹{advance_payment:.2f}")
print(f"remaining amount to be paid : ₹{pending_payment} ")
print("Documents Provided:", ', '.join(documents))

 