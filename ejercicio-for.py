tienemasbultos = True 
nrobulto = 1
valorpagarporkilo = 0
valorpesoliviano = 1000
valorpesonormal = 4500
totalliviano = 0
totalnormal = 0
contadorbultoslivianos = 0
contadorbultosnormales = 0

cantidadbultos = int(input("Ingrese cantidad de bultos :"))
for i in range (cantidadbultos):
    try:
        pesobulto = int(input(f"ingrese el peso (1 a 10kg) del bulto nro. {nrobulto}: "))
    except ValueError:
        print("Peso del bulto deben estar en el rango de 1 y 10kg. ")
        continue

    if 1 <= pesobulto <= 5:
        totalliviano += valorpesoliviano
        contadorbultoslivianos += 1
    elif 6 <= pesobulto <= 10:
        totalnormal += valorpesonormal
        contadorbultosnormales += 1 
    else:
        print("Peso ingresado incorrecto (1 - 10kg)")

    nrobulto += 1   
print(f"Total a pagar por los bultos livianos: {totalliviano}")
print(f"Total a pagar por los bultos normales: {totalnormal}")
print(f"Cantidad de bultos livianos: {contadorbultoslivianos}")
print(f"Cantidad de bultos normales: {contadorbultosnormales}")