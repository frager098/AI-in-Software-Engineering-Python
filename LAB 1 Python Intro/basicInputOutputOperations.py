#Exercise : Basic InputOutputOperations

# (i)Write a Python program to swap 4 variables values (input four values.
# Sample input:
# Before swapping
# a=2,b=56,c=78,d=9
# After Swapping
# a=,9,b=78,c=56,d=2
def swap(a,b,c,d):
    temp = d
    d = a 
    a = temp 
    temp = c 
    c = b
    b = temp 
    del(temp)
    return a,b,c,d
# a = input("Enter Value for a:")
# b = input("Enter Value for b:")
# c = input("Enter Value for c:")
# d = input("Enter Value for d:")
# print(a,b,c,d,"Before swapping")
# a,b,c,d = swap(a,b,c,d)
# print(a,b,c,d,"After swapping")

# (ii) Write a Python program to convert temperatures to and from celsius,
# Fahrenheit.
# Formula : c/5 = f-32/9
# Expected Output :
# Enter temp in Celsius: 60°C
# Temperature in Fahrenheit is :140

def interconversionOfTemperatures(toConvert) :
    conversion = 1
    while(conversion != 0 ):
        prompt ="Press 0 to exit\nPress 1 to convert Celcius into Fahrenheit\nPress 2 to convert Fahrenheight into Celcius\nPress 3 to convert Kelvin into Celcius\nPress 4 to convert Celcius into Kelvin"
        print(prompt)
        conversion = eval(input("Enter:"))
        print(conversion)
    
        if( conversion == 0 ):
            print("Exit!")
            break
        elif(conversion == 1 ):
            celcius = toConvert 
            fahrenheit = (celcius * (9/5) ) + ( 32)
            print("Temperature in Fahrenheit is:" , fahrenheit)
        elif(conversion == 2 ):
            fahrenheit = toConvert
            celcius = ( (fahrenheit - 32 ) * ( 5 / 9 ) )
            print("Temperature in Celcius is:",celcius)
        elif(conversion == 3 ):
            kelvin = toConvert
            celcius = kelvin - 273 
            print("Temperature in Celcius is:",celcius)
    
        elif(conversion == 4 ):
            celcius = toConvert
            kelvin = celcius + 273 
            print("Temperature in Celcius is:",kelvin)
        else :
            print("Wrong input!")
            continue 

toConvert = eval(input("Enter Temperature:"))
interconversionOfTemperatures(toConvert)