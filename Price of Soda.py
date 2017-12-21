"""This program prints the price per ounce for a six-pack off cans"""

#Define constatnts for the pack size
CANS_PER_PACK = 6

#Obtain price per pack and can volume
UserInput = input("Please enter the price for a six pack: ")
UserInput = input("Please enter the volume for each can in ounces: ")
CanVolume = float(UserInput)
PackPrice = float(UserInput)
#Compute can volume
PackVolume = CanVolume * CANS_PER_PACK
#Compute and print price per ounce
PricePerOunce = PackPrice/PackVolume
print("Price Pper Ounce: ", PricePerOunce)
