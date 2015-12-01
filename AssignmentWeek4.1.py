 #Functions

def greet(lang):
    if lang=='es':
        return 'Hola'
    elif lang == 'fr':
        return 'Bonjour'
    else:
        return 'Hello'

def addtwo(a,b):
    added = a + b
    return added

print greet('en'),'Glenn'
print greet('es'),'Sally'
print greet('fr'),'Michael'
x=addtwo(3,5)
print 'x:',x

