def change():
    gasto = 23.75
    dinero_recibido = 100
    print("Ingresar gasto:")
    print(gasto)
    print("Dinero recibido")
    print(dinero_recibido)
    vuelto = dinero_recibido - gasto
    pesos = int(vuelto)
    centavos = int(round((vuelto - pesos) * 100))

    print("\nVuelto\n")
    print(f"Pesos:\n{pesos}")
    print(f"Centavos:\n{centavos}")
