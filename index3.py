#Ejemplo 3 (Calculadora)

usd_cop = 3300
eur_cop = 3800

def give_ammount(money):
    return int(input('Cuantos {} desea cambiar a COP? '.format(money)))


def exchange(ammount, tipo_cambio):
    return float(ammount * tipo_cambio)


def message(ammount, money, result):
    print('${} {} equivalen a ${} pesos COP'.format(ammount, money, result))


def dolar_peso():
    money = 'USD'
    ammount = give_ammount(money)
    result = exchange(ammount, usd_cop)
    message(ammount, money, result)


def eur_peso():
    money = 'EUR'
    ammount = give_ammount(money)    
    result = exchange(ammount, eur_cop)
    message(ammount, money, result)


def run():
    print('C A L CU L A D O R A  D E  D I V I S A S')
    print('*' * 50)
    print('')
    print('Convierte de Dolares a Pesos : USD a COP : Presiona 1')
    print('Convierte de Euros a Pesos   : EUR a COP : Presiona 2')
    print('')

    option = int(input('Elige el tipo de cambio que deseas: '))

    if option == 1:
        dolar_peso()

    elif option == 2:
        eur_peso()

    else:
        print('Elegiste una opcion INCORRECTA, vuelve a intentar')


if __name__ == "__main__":
    run()
    print('')
