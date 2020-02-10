#Ejemplo 2 (Dibujar un cuadrado segun el tamaño que se le otorgue)
import turtle


def main():
    _window = turtle.Screen() 
    renzo = turtle.Turtle()

    make_square(renzo)
    turtle.mainloop()
    
   
   # Este comando sirve para que no se cierra le ventana de python turtle


def make_square(renzo):
    length = int(input('Tamaño de cuadrado: '))

    for _i in range(9):
        make_line_and_turn(renzo, length)

def make_line_and_turn(renzo, length):
    renzo.forward(length)
    renzo.right(45)

if __name__ == '__main__':
    main()