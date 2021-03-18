def my_function(a,b):
    print('El resutlado de ',a,'x 2 es:',b)
aNumber = -1
while aNumber<1 or aNumber>10 :
    try:
        aNumber = int(input("Enter an integer (1-10):"))
        if (aNumber <0 or aNumber > 10):
            print ('No estaríamos entendiendo... el valor {} es incorrecto. Tiene que ser entre 1 y 10.'.format(aNumber))
    except ValueError as vE:
        print('Sonamos!!! valor incorrecto:{}. Tiene que ser integer entre 1 y 10.'.format(aNumber))
        quit 
result = aNumber * 2
x=1
while x <=aNumber:
    my_function(aNumber,result)
    print("X:",x)
    x += 1

