print("**calculador python**")
print("1.- suma")
print("2.- resta")
print("3.- multiplicacion")
print("4.- division")
#tratamiento de calculadora
opcion=input("ingresa tu opcion: ")
num1=float(input("ingrese nuemro 1: "))
num2=float(input("ingrese numero 2: "))
if opcion =="1":
    print("la suma es", num1+num2)
elif opcion =="2":
       print("la resta es", num1-num2)
elif opcion =="3":
    print("la multiplicacion es", num1*num2) 
elif opcion =="4":
        if num2 == 0:
            print("no se puede dividir por cero")
        else:
             print("la division es", num1/num2)
else:
     print("error")             
              

                     
               
               


                    