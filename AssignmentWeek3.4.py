 #Agregando el try al ejercicio anterior

try:
    hrs = raw_input("Enter Hours:")
    rph = float(raw_input("Enter rate per hour:"))
    h = float(hrs)
except:
    print "Error. Enter a numeric value."
    quit()
if h>40:
    pay = 40 *rph
    pay += (h-40)* (rph*1.5)
else:
    pay = h*rph
print "Should pay {}".format(pay)
