import Mod.Temp_module

# conversion of temperature
print("Menu")
print("1:C to F")
print("2:C to K")
print("3:F to C")
print("4:K to C")

# converting celsius to fahrenheit
x = int(input("Enter your choice here:"))
if x == 1:
    c = float(input("Enter temperature in celsius:"))
    y = Mod.Temp_module.CtoF(c)
    print(y)

# converting celsius to Kelvin
if x == 2:
    c = float(input("Enter temperature in celsius:"))
    y = Mod.Temp_module.CtoK(c)
    print(y)

# converting fahrenheit to celsius
if x == 3:
    f = float(input("Enter temperature in fahrenheit:"))
    y = Mod.Temp_module.FtoC(f)
    print(y)

# Converting Kelvin to celsius
if x == 4:
    k = float(input("Enter Temperature in kelvin:"))
    y = Mod.Temp_module.KtoC(k)
    print(y)

m_p = Mod.Temp_module.m_p
print(m_p)
print(Mod.Temp_module.b_p)

