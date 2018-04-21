from numbers import Numbers

try:
    numbers = input("Porfavor ingrese la cadena de numeros ->:")
    numbers = numbers.split(" ")
    for w in numbers:
        if w == "0,0":
            break
        size, number = w.split(",")
        size = int(size)
        if size<1 or size>10:
            print("Solo se puede medidas entre 1-10")
            break
        n = Numbers(size,number)
        numbers = n.getAllNumbers()

        print('\n')
        for x in numbers:
            print("")
            for y in x:
                print(y, end=" ")
except ValueError:
    print("ERROR: Has insertado un formado incorrecto, intentalo de nuevo.")