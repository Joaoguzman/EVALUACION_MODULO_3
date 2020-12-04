while True:
    try:
        cant = int(input("ingrese: "))
        if cant > 0 and cant < 5:
            print(cant)
            break
        else:
            continue
    except ValueError:
        print("Error")