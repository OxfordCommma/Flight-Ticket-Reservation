import sqlite3
from clase_vuelos import Vuelos

class Usuario:
   
    def __init__(self):
        self.nombre = input("Nombre: ")
        self.apellido = input("Apellido: ")
        self.mail = input("Correo electrónico: ")
        self.telefono = int(input("Teléfono: "))
        self.dni = int(input("Documento de Identidad: "))
    
    def reservar(self):

        self.pais_salida = int(input("\n1- \033[33mArgentina\033[0m\n2- \033[32mBrasil\033[0m\n3- \033[36mUruguay\033[0m\n4- \033[31mPerú\033[0m\n5- \033[34mChile\033[0m\nIndique el país de salida: "))
        self.pais_destino = int(input("Indique el país de destino: "))

        while self.pais_salida not in range(1,6):
            self.pais_salida = int(input("Valor desconocido: indique el país de salida: \n1- Argentina\n1- Brasil\n1- Uruguay\n1- Peru\n1- Chile"))
        else:
            while self.pais_destino not in range(1,6):
                self.pais_destino = int(input("Valor desconocido: indique el país de destino: \n1- Argentina\n1- Brasil\n1- Uruguay\n1- Peru\n1- Chile"))
        
        gestor_vuelos = Vuelos()
        dispo = list(gestor_vuelos.muestra_vuelos(self.pais_salida, self.pais_destino))
        
        print("\nEstas son los vuelos disponibles que puede elegir segun sus criterios:")
        index = 1
        self.dispo_dicc = {}

        for vuelo in dispo:
            self.dispo_dicc[index] = vuelo
            index += 1

        for clave, valor in self.dispo_dicc.items():
            print(f"{clave} - {valor}")
        
        def ultimos_pasos(): 
            dispo_elecc = int(input("\nElija el número de vuelo a reservar: "))
            while True:
                if dispo_elecc in self.dispo_dicc:
                    dispo_elecc_conf = input(f"""\n¿Confirma el vuelo {dispo_elecc} - {self.dispo_dicc[dispo_elecc]}? Escriba 's' para confirmar reserva, 'r' para elegir otro vuelo o 'n' para cancelar reserva: """)    
                    if dispo_elecc_conf.lower() == "s":
                        vuelo_elegido = self.dispo_dicc[dispo_elecc]
                        break    
                    elif dispo_elecc_conf.lower() == "r":
                        ultimos_pasos()    
                    elif dispo_elecc_conf.lower() == "n":
                        print("Operación cancelada. No se ha realizado ninguna reserva.")
                        return "Operación cancelada"
                else:
                    repregunta = input("N° de vuelo elegido no disponible. ¿Desea reservar un vuelo? 's' para SI y 'n' para NO: ")
                    if repregunta.lower() == 's':
                        ultimos_pasos()
                    else:
                        print("Operación cancelada. No se ha realizado ninguna reserva.")
                        return "Operación cancelada"
            return vuelo_elegido
        return ultimos_pasos()

    
    def __str__(self):
        return [f"Usuario - {self.nombre} {self.apellido}, {self.mail}, {self.telefono}, {self.dni}"]
    
    def comprar(self):
        self.diccionario = {1: 'Argentina', 2: 'Brasil', 3: 'Uruguay', 4: 'Perú', 5: 'Chile'}
        self.a = self.reservar()
        print("\n------------------------------------------------------")
        self.ticket_resumen = f"Resumen del ticket\nUsuario: {self.nombre} {self.apellido}\nCorreo Electronico: {self.mail}\nTelefono {self.telefono}\nDocumento de Identidad {self.dni}\nDetalles del Vuelo: {self.a}"
        return self.ticket_resumen


class Gestor_de_Tickets:
    
    lista_usuarios = []

    def getLista_usuarios(self):
        return self.lista_usuarios


class Menu:

    def run(self):
        iniciador = 0
        while iniciador == 0:
            print("Bienvenido al sitio de reservas de vuelo PyAirways\n\nIngrese sus datos")
            usuario = Usuario()
            app_gestora = Gestor_de_Tickets()
            app_gestora.lista_usuarios.append(usuario.__str__())
            print(usuario.comprar())
            print("------------------------------------------------------\n")
            iniciador = int(input("Ingrese 0 para crear un nuevo usuario y reservar, o 99 para salir: "))


Menu().run()