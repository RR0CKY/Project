import math

# Step 1: Triangle ki teeno sides a,b aur c ke jagha per daloo
a = float(input("Pehli side (a) dalo: "))
b = float(input("Dusri side (b) dalo: "))
c = float(input("Teesri side (c) dalo: "))

# Step 2: Aadha perimeter (s) nikalo
s = (a + b + c) / 2

# Step 3: Heron's Formula se Area calculate keraga yeh code
area = math.sqrt(s * (s - a) * (s - b) * (s - c))

# Final Result yeha hi 
print("Triangle ka Area hai:", area)