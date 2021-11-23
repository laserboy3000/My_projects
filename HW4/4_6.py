######################################
#Autor: Voitov Vladimir              #  
#Date: 21.11.21                      #
#Task: Converter                     #
######################################

def litkm_to_milfal(litres): # def for founding gal/miles
    mile = 1609.344 # met in 1 mile
    gallon = 3.785411784 # litr in 1 gallon

    gal = litres/gallon # find how many gallons in user litres
    miles = 100*1000/mile # how many miles

    return round(miles/gal, 1) # answer 

def milfal_to_litkm(gallons): # def for founding litres/km
    return round(235.22/gallons, 1) # simple formula 

print(litkm_to_milfal(3.9)) # example gal/miles
print(milfal_to_litkm(60.3)) # examle litres/km
 
