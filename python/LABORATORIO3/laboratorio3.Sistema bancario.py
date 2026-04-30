saldo = 1000
movimientos = []
while True:
    print("\n--- SISTEMA BANCARIO ---")
    print("1. Consultar saldo")
    print("2. Depositar dinero")
    print("3. Retirar dinero")
    print("4. Ver movimientos")
    print("5. Salir")
    opcion = input("Seleccione una opción: ")
    match opcion:
        case "1":
            print(f"Su saldo actual es: ${saldo}")
        case "2":
            deposito = float(input("Ingrese monto a depositar: "))

            if deposito > 0:
                saldo += deposito
                movimientos.append(f"Depósito: +${deposito}")
                print("Depósito realizado con éxito un valesito para celebrar")
            else:
                print("Monto inválido")
                continue
        case "3":
            retiro = float(input("Ingrese monto a retirar: "))

            if retiro <= 0:
                print("Monto inválido")
                continue
            if retiro > saldo:
                print("Fondos insuficientes")
            else:
                saldo -= retiro
                movimientos.append(f"Retiro: -${retiro}")
                print(
                    "Retiro realizado con éxito,goso,alegria, bamos agastarnos ese dinero pero recuerde de no dejarme la cuenta en 000"
                )
        case "4":
            print("\n--- MOVIMIENTOS ---")

            if len(movimientos) == 0:
                print("No hay movimientos registrados")
            else:
                for movimiento in movimientos:
                    print(movimiento)
        case "5":
            print(
                "Gracias por usar el sistema bancario cundo desee volver a retirar dinero aqui estoy para servirle y procure que su cuenta bancaria no quede como la de patricia fernandes"
            )
            break
        case _:
            print("Opción inválida, intente nuevamente")
            continue
