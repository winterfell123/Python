def average_temps(temps):
    total = 0

    for temp in temps:
        total += float(temp)
    
    
    return total / len(temps)
    
    

if __name__ == "__main__":
    temps = [21, 24, 24, 23, 22, 20, 24]

    average = average_temps(temps)

    # Aqui imprimo la lista de temperaturas
    
    print("Temperatura registradas {}".format(temps))

    print("La temperatura promedio es {}".format(average))