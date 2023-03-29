import sqlite3
from clase_vuelos import Vuelos

class Usuario:
   
    def __init__(self):
        self.nombre = input("Su nombre: ")
        self.apellido = input("Su apellido: ")
        self.mail = input("Su mail: ")
        self.telefono = int(input("Su telefono: "))
        self.dni = int(input("Su DNI: "))
    
    def reservar_destino(self):

        self.pais_salida = int(input("Indique el país de salida: \n1- Argentina\n2- Brasil\n3- Uruguay\n4- Peru\n5- Chile\n"))
        self.pais_destino = int(input("Indique el país de destino: \n1- Argentina\n2- Brasil\n3- Uruguay\n4- Peru\n5- Chile\n"))

        while self.pais_salida not in range(1,6):
            self.pais_salida = int(input("Valor desconocido: indique el país de salida: \n1- Argentina\n1- Brasil\n1- Uruguay\n1- Peru\n1- Chile"))
        else:
            while self.pais_destino not in range(1,6):
                self.pais_destino = int(input("Valor desconocido: indique el país de destino: \n1- Argentina\n1- Brasil\n1- Uruguay\n1- Peru\n1- Chile"))
        
        gestor_de_vuelos_disponibles = Vuelos()
        all_flights = list(gestor_de_vuelos_disponibles.muestra_vuelos(self.pais_salida, self.pais_destino))
        
        print("\nEstas son los vuelos disponibles que puede elegir segun sus criterios. Elija segun el orden dado:")
        avl_flights_index = 1
        self.saved_avl_flights = {}
        for vuelo in all_flights:
            self.saved_avl_flights[avl_flights_index] = vuelo
            avl_flights_index += 1
        for clave, valor in self.saved_avl_flights.items():
            print(f"{clave} - {valor}")
        
        #Cuando vuelvas, tratá de colocar a wished_flight dentro de def ultimos_pasos()
        def ultimos_pasos(): 
            wished_flight = int(input("\nElija el número de vuelo que desea reservar: "))
            while True:
                if wished_flight in self.saved_avl_flights:
                    asegura_vuelo = input(f"""¿Seguro que desea elegir el vuelo número {wished_flight} - {self.saved_avl_flights[wished_flight]}?
                    Escriba 's' si desea confirmar su reserva, 'r' para elegir otro vuelo o 'n' para cancelar reserva: """)    
                    if asegura_vuelo.lower() == "s":
                        vuelo_elegido = self.saved_avl_flights[wished_flight]
                        print(f"Perfecto, le mostramos los detalles del vuelo: opción nro {wished_flight},\nvuelo nro {vuelo_elegido[0]},\npaís partida {vuelo_elegido[1]},\npaís destino {vuelo_elegido[2]},\ncosto {vuelo_elegido[3]}\nasientos disponibles {vuelo_elegido[4]}.")
                        break    
                    elif asegura_vuelo.lower() == "r":
                        ultimos_pasos()    
                    elif asegura_vuelo.lower() == "n":
                        print("Operación cancelada. No se ha realizado ninguna reserva.")
                        return "Operación cancelada"
                else:
                    repregunta = input("El número de vuelo elegido no está disponible. Desea reservar un vuelo? 's' para SI y 'n' para NO: ")
                    if repregunta.lower() == 's':
                        ultimos_pasos()
                    else:
                        print("Operación cancelada. No se ha realizado ninguna reserva.")
                        return "Operación cancelada"
            return vuelo_elegido
        return ultimos_pasos()

    
    def __str__(self):
        return [f"Usuario - {self.nombre} {self.apellido}, {self.mail}, {self.telefono}, {self.dni}"]
    
    def resumen(self):
        self.diccionario = {1: 'Argentina', 2: 'Brasil', 3: 'Uruguay', 4: 'Perú', 5: 'Chile'}
        self.a = self.reservar_destino()
        self.ticket_resumen = f"Resumen del ticket\nUsuario - {self.nombre} {self.apellido}, {self.mail}, {self.telefono}, {self.dni} - {self.a}"
        return self.ticket_resumen


class Gestor_de_Tickets:
    
    lista_usuarios = []

    def getLista_usuarios(self):
        return self.lista_usuarios


class Menu:
    

    def run(self):
        iniciador = 0
        while iniciador == 0:
            created_user = Usuario()
            app_gestora = Gestor_de_Tickets()
            app_gestora.lista_usuarios.append(created_user.__str__())
            print(created_user.resumen())
            iniciador = int(input("Ingrese 0 para crear un nuevo usuario y reservar, o 99 para salir: "))


Menu().run()