current_odometer = int(input("enter current odometer: "))
previous_odometer = int(input("enter previous odometer: "))
gas_added = int(input("enter gas added: "))
gas_price = int(input("enter gas price: "))
fmt = input("enter format: ")
if fmt.lower() == "us":
  miles_traveled = previous_odometer - current_odometer
  print(miles_traveled)
  mileage = miles_traveled / gas_added
  print("mileage: " + str(mileage) + "m/g")
  print("total = $" + str(mileage * gas_price) + ".")
elif fmt.lower() == "metric":
  miles_traveled = previous_odometer - current_odometer
  mileage = miles_traveled / gas_added
  print("mileage: " + str(mileage) + "kg/g")
  print("total = $" + str(mileage * gas_price) + ".")
else:
  print("Invalid Format! Try Again")
