print("\n === mi primera claculadora 🧩 === \n")

numero1 = int(input("ingresa el numero1: "))
numero2 = int(input("ingresa el numero2: "))

operador = input("ingresa la operacion (+, -, *, /): ")

if operador == "+":
    print("el resultado de la suma es: ", numero1 + numero2)
elif operador == "-":
    print("el resultado de la resta es: ", numero1 - numero2)
elif operador == "*":
    print("el resultado de la multiplicacion es: ", numero1 * numero2)
elif operador == "/":
    print("el resultado de la division es: ", numero1 / numero2)

else:
    if numero2 == 0:
        print("opracion no valida 🥀")


