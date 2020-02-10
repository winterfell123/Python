#Ejemplo 1 (Preguntar nombre y consultar edad  )
def run():
    edad = int(input('Ingresa tu edad porfavor: '))
    edades(edad)

def edades(edad):
    if edad > 18:
        print('Puedes sacar tu DNI')
    else: 
        print('Aun te falta edad para tener tu DNI')    

if __name__=='__main__':
    run()

