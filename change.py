def change():
	gasto = float(input("Ingresar gasto:\n"))
	recibo = float(input("Dinero recibido\n"))
	pesos = recibo-gasto
	centavos = (float(pesos)-int(pesos))*100


	print("\nVuelto\n")
	print("Pesos:")
	print(int(pesos))
	print("\nCentavos:")
	print(int(centavos))

print(change())
