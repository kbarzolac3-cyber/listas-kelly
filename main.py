from pasajero import Pasajero
from mi_lista import MiLista
from lista_python import ListaPython

lista1 = MiLista(10)
lista2 = ListaPython()


def leer_entero(mensaje):
    while True:
        try:
            return int(input(mensaje))
        except ValueError:
            print('Debe escribir un numero entero.')


def leer_pasajero():
    numero = leer_entero('Numero: ')
    nombre = input('Nombre: ').strip()
    cedula = input('Cedula: ').strip()
    edad = leer_entero('Edad: ')
    fecha = input('Fecha (AAAA-MM-DD): ').strip()
    destino = input('Destino: ').strip()
    asiento = input('Asiento: ').strip().upper()
    return Pasajero(numero, nombre, cedula, edad, fecha, destino, asiento)


def cargar_datos_prueba(lista):
    datos = [
        Pasajero(1005, 'Diana', '0923456789', 22, '2026-11-15', 'Quito', '12A'),
        Pasajero(1002, 'Ana', '0912345678', 28, '2026-11-15', 'Lima', '03C'),
        Pasajero(1009, 'Luis', '0987654321', 35, '2026-11-20', 'Bogotá', '18F'),
        Pasajero(1004, 'Beto', '0934567890', 16, '2026-11-20', 'Quito', '07B'),
        Pasajero(1001, 'Elena', '0901234567', 41, '2026-11-22', 'Lima', '01A')
    ]
    agregados = 0
    for p in datos:
        if lista.añadir(p):
            agregados = agregados + 1
    print('Datos nuevos cargados:', agregados)


def mostrar_opciones(titulo, extras=False):
    print('\n======', titulo, '======')
    print('1. Añadir             2. Listar             3. Insertar')
    print('4. Buscar             5. Busqueda binaria    6. Modificar')
    print('7. Eliminar posicion  8. Eliminar numero     9. Orden ascendente')
    print('10. Orden descendente 11. Reversar           12. Copiar')
    print('13. Longitud')
    if extras:
        print('14. Filtrar destino   15. Mayores de edad')
    print('C. Cargar pruebas     0. Volver')


def mostrar_encontrado(lista, numero, binaria=False):
    if binaria:
        pos = lista.buscar_binaria(numero)
    else:
        pos = lista.buscar(numero)
    if pos == -1:
        print('No existe')
    else:
        print(f'Encontrado en [{pos}]')
        if isinstance(lista, MiLista):
            print(lista.datos[pos])
        else:
            print(lista.pasajeros[pos])


def mostrar_pasajeros(pasajeros):
    if not pasajeros:
        print('No hay resultados')
    for p in pasajeros:
        print(p)


def ejecutar_menu(lista, titulo, extras=False):
    while True:
        mostrar_opciones(titulo, extras)
        op = input('Opcion: ').strip().upper()

        if op == '1':
            p = leer_pasajero()
            print('Anadido' if lista.anadir(p) else 'No se pudo añadir (lleno o repetido)')
        elif op == '2':
            lista.listar()
        elif op == '3':
            pos = leer_entero('Posicion: ')
            p = leer_pasajero()
            print('Insertado' if lista.insertar(pos, p) else 'Posición inválida, lleno o repetido')
        elif op == '4':
            numero = leer_entero('Numero que busca: ')
            mostrar_encontrado(lista, numero)
        elif op == '5':
          
            lista.ordenar_asc()
            print('Lista ordenada para buscar:')
            lista.listar()
            numero = leer_entero('Numero que busca: ')
            mostrar_encontrado(lista, numero, True)
        elif op == '6':
            numero = leer_entero('Numero a modificar: ')
            destino = input('Nuevo destino: ').strip()
            asiento = input('Nuevo asiento: ').strip().upper()
            print('Modificado' if lista.modificar(numero, destino, asiento) else 'No existe')
        elif op == '7':
            pos = leer_entero('Posicion que desea eliminar: ')
            eliminado = lista.eliminar_por_posicion(pos)
            print('Eliminado:', eliminado if eliminado is not None else 'Posición inválida')
        elif op == '8':
            numero = leer_entero('Numero que desea eliminar: ')
            print('Eliminado' if lista.eliminar_por_valor(numero) else 'No existe')
        elif op == '9':
            lista.ordenar_asc()
            lista.listar()
        elif op == '10':
            lista.ordenar_desc()
            lista.listar()
        elif op == '11':
            lista.reversar()
            lista.listar()
        elif op == '12':
            copia = lista.copiar()
            copia.reversar()
            print('Copia reversada:')
            copia.listar()
            print('Original sin cambios de orden:')
            lista.listar()
        elif op == '13':
            print('Cantidad:', lista.longitud())
        elif op == '14' and extras:
            destino = input('Destino: ').strip()
            mostrar_pasajeros(lista.filtrar_por_destino(destino))
        elif op == '15' and extras:
            mostrar_pasajeros(lista.mayores_de_edad())
        elif op == 'C':
            cargar_datos_prueba(lista)
        elif op == '0':
            break
        else:
            print('Opción no válida')


def menu_lista1():
    ejecutar_menu(lista1, 'MENU 1 - MiLista')


def menu_lista2():
    ejecutar_menu(lista2, 'MENU2 - Lista Python', True)


def main():
    while True:
        print('\n===== SISTEMA DE PASAJEROS =====')
        print('1. MiLista (a mano)')
        print('2. Lista de Python')
        print('3. Salir')
        op = input('Opcion: ').strip()
        if op == '1':
            menu_lista1()
        elif op == '2':
            menu_lista2()
        elif op == '3':
            print('Hasta pronto')
            break
        else:
            print('Opción no válida')


if __name__ == '__main__':
    main()
