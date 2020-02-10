import random

def run():
    number_found = False
    rango = int(input('Hasta que número deseas que se genere el Rango: '))
    random_number = random.randint(0, rango)

    while not number_found:
        number = int(input('Ingresa un Numéro: '))

        if number == random_number:
            print('Felicitaciones!! Lo habéis Encontrado!! "Eres Un Crack con los Números')
            number_found = True
        elif number > random_number:
            print('El número es más Pequeño. Intenta nuevamente!')
        else:
            print('El número es más Grande. Intenta nuevamente!')

if __name__ == "__main__":
    run()