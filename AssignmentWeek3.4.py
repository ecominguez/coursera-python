 #Agregando el try al ejercicio anterior

try:
    hrs = input("Enter Hours:")
    rph = float(input("Enter rate per hour:"))
    h = float(hrs)
except SystemExit:
    print("Error. Enter a numeric value.")
    raise
if h>40:
    pay = 40 *rph
    pay += (h-40)* (rph*1.5)
else:
    pay = h*rph
print("Should pay {}".format(pay))
