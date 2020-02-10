def Tipo_de_Cambio(_Monto):
    cambio_soles_dolares = 0.30 
    return cambio_soles_dolares * _Monto

def run():
    print('C A L C U L A D O R A  D E  D I V I S A S ')
    print('convierte de soles peruanos a dolares')
    print('')

    _Monto = int(input('Ingresa la cantidad de soles peruanos que quieres convertir a dolares:'))
    
    _result = Tipo_de_Cambio(_Monto)

    return message(_Monto,_result)

def message(_Monto,_result):

     print('S/{} soles peruanos son ${} dolares'.format(_Monto,_result))
     print('') 
   
if __name__ == '__main__':
    run()