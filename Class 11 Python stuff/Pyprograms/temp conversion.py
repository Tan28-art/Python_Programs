# conversion of temperature
print("Menu")
print("1:C to F")
print("2:C to K")
print("3:F to C")
print("4:K to C")

# converting Celcius to Farenheit
x = int(input("Enter your choice here:"))
if x == 1:
    c = float(input("Enter temperature in celcius:"))
    f = (9 / 5 * c) + 32
    print("Temperature in Farenheit is :", f)

# converting Celcius to Kelvin
if x == 2:
    c = float(input("Enter temperature in celcius:"))
    k = c + 273.15
    print("Temperature in Kelvin is:", k)

# converting farenheit to celcius
if x == 3:
    f = float(input("Enter temperature in farenheit:"))
    c = 5 / 9 * (f - 32)
    print("Temperature in Celcius is:", c)

# Converting Kelvin to celcius
if x == 4:
    k = float(input("Enter Temperature in kelvin:"))
    c = k - 273.15
    print("Temperature in Celcius is:", c)
