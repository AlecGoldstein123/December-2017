"""This program computes the volume (In Litres)of a six pack of soda and thetotal volume of a
six-pack and a 2 litre bottle."""

#Litres in a 12 ounce can and 2-litre bottle
CAN_VOLUME = 0.355
BOTTLE_VOLUME = 2.0

#Number of cans per pack
CansPerPack = 6

#Calculate the total volume in cans
TotalVolume = CansPerPack * CAN_VOLUME
print("A six-pack of 12 ounce cans contains", TotalVolume,)

#Calculate the total volume in cans and the 2 litre bottle
TotalVolume = TotalVolume + BOTTLE_VOLUME
print("A six-pack and a two-litre bottle contains", TotalVolume, "litres")
