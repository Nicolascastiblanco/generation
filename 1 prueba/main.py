numero, mayor= 0,1000


while numero <= mayor:
    if numero % 3 == 0 and numero % 5 == 0:
        print("fisbuzz")
    elif numero % 3 == 0:
        print("fizz")  
    elif numero % 5 == 0:
        print("fizzbuz")
    else: 
        print(numero)       
    numero += 1


    #grupo conformador por Milma Marmolejo, Yeison Gutierres, Nicolas Castiblanco 