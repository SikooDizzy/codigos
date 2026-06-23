tienemasbultos = True 
nrobulto = 1
valorpesoliviano = 1000
valorpesonormal = 4500
totalliviano = 0
totalnormal = 0
contadorbultoslivianos = 0
contadorbultosnormales = 0

cantidadbultos = int(input("Ingrese cantidad de bultos :"))

for i in range(cantidadbultos):
    while True:
        try:
            pesobulto = int(input(f"ingrese el peso (1 a 10kg) del bulto nro. {nrobulto}: "))
            
            if 1 <= pesobulto <= 5:
                totalliviano += valorpesoliviano
                contadorbultoslivianos += 1
                break 
            elif 6 <= pesobulto <= 10:
                totalnormal += valorpesonormal
                contadorbultosnormales += 1 
                break
            else:
                print("Peso ingresado incorrecto. Debe estar entre 1 y 10kg.")
                
        except ValueError:
            print("Entrada inválida. Debe ingresar un número entero entre 1 y 10kg.")

    nrobulto += 1   

print(f"\nTotal a pagar por los bultos livianos: {totalliviano}")
print(f"Total a pagar por los bultos normales: {totalnormal}")
print(f"Cantidad de bultos livianos: {contadorbultoslivianos}")
print(f"Cantidad de bultos normales: {contadorbultosnormales}")
