def agregar_gastos(descripcion, categoria, monto):
    """
    Función que devuelve un dict y agrega todos los valores a sus claves correspondientes
    """
    return {
        "descripcion": descripcion,
        "categoria": categoria,
        "monto": monto
    }


def guardar_datos(gasto, archivo="data.txt"):
    """
    Función que permite guardar datos en un archivo txt, se agrega cada clave en el orden
    correspondiente
    """
    with open (archivo, "a") as d:
        d.write(f"{gasto["descripcion"]},{gasto["categoria"]},{gasto["monto"]}\n")


def leer_datos(archivo="data.txt"):
    """
    Función que permite leer los datos del archivo txt, se accede al archivo, luego se filtra
    utilizando strip y split y se separan los valores según el índice de la nueva lista.
    Se llama la función agregar gastos para crear un reporte de gasto y se agrega a la lista de
    gastos que es el valor a retornar
    """
    gastos = []

    try:
        with open (archivo, "r") as d:
            contenido = d.readlines()
    except FileNotFoundError:
        return gastos
    
    for linea in contenido:
        datos_filtrados = linea.strip().split(",")
        descripcion = datos_filtrados[0]
        categoria = datos_filtrados[1]
        monto = int(datos_filtrados[2])


        gasto = agregar_gastos(descripcion, categoria, monto)
        gastos.append(gasto)
    
    return gastos


def total_categorias():
    """
    Función que permite leer el total por categorías, se utiliza la función leer datos que retorna
    un dict, en base a esto se pueden obtener los valores y crear nuevas variables utilizando
    las claves correspondientes. En este caso solo se utiliza categoria y monto
    """
    total = {}
    datos = leer_datos()

    for i in datos:
        categoria = i["categoria"]
        monto = i["monto"]
    
        if categoria not in total:
            total[categoria] = monto

        else:
            total[categoria] += monto

    return total

def valor_total():
    """
    Función que permite retornar el valor total
    """    
    total = 0
    datos = leer_datos()

    for d in datos:
        monto = d["monto"]
        total += monto

    return total

def gasto_mayor():
    """
    Función que permite retornar el gasto mayor del archivo
    """
    datos = leer_datos()
    return max(datos, key=lambda x: x["monto"])


def mostrar_reporte():
    """
    Esta función solo llama a las otras funciones para crear un reporte general del archivo
    """
    tc = total_categorias()
    vt = valor_total()
    gm = gasto_mayor()

    print("REPORTE DE GASTOS\n")

    print("Gasto total por categorías:\n")
    for categoria, monto in tc.items():
        print(categoria, monto)

    print("Gastos totales\n", vt)
    print("Gasto más alto:\n", gm)

    return ":)"


if __name__ == "__main__":
    """
    Programa principal que permite agregar gastos al archivo y permite leer los datos del mismo
    llamando a las funciones correspondientes
    """
    while True:
        print("EXPENSE TRACKER\n")
        print("1. Agregar un gasto")
        print("2. Ver reporte")
        print("3. Salir")

        try:
            opcion = int(input("\nIngresa una opción: "))
        except ValueError:
            print("Opción inválida, intenta nuevamente\n")
            continue

        if opcion == 1:

            descripcion = input("Agrega una descripción: ")
            categoria = input("Agrega la categoría: ")
            try:
                monto = int(input("Ingresa el monto: "))
            except ValueError:
                print("Monto inválido, intenta nuevamente")
                continue
            
            gasto = agregar_gastos(descripcion,categoria, monto)
            guardar_datos(gasto)
            print("\nDatos guardados exitosamente:)\n")
        
        elif opcion == 2:
            reporte = mostrar_reporte()
            print(reporte)

        elif opcion == 3:
            print("Cerrando el programa...")
            break
