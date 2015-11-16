def myFunction(a,b):
    print "El resutlado de ",a,"x 2 es:",b
test = -1
while test<1 or test>10 :
    test = int(raw_input("Enter an integer (1-10:"))
try:
   test = int(test)
except:  
   print "Invalid entry."
   quit()  
result = test * 2
x=1
while x <=test:
    myFunction(test,result)
    print "X:",x
    x += 1

