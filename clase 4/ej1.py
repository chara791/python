num_1=int(input("ingrese el promer numero: "))
num_2=int(input("ingrese el segundo numero: "))

if(num_1>num_2):
    print("{} es mayor a {}".format(num_1,num_2))
    if(num_1%2==0):
        print("el numero el numero es par ")
    else:
        print("el numero es impar")
elif(num_1<num_2):
    print("{} es mayor a {}".format (num_2,num_1))
    if(num_2% 2==0):
        print("el numero es par ")
    else:
        print("el numro es impar")
else:
    print("los numro son iguales ")