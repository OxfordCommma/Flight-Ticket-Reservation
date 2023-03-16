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
            else:
                return [self.pais_salida, self.pais_destino]
    
    def __str__(self):
        self.diccionario = {1: 'Argentina', 2: 'Brasil', 3: 'Uruguay', 4: 'Perú', 5: 'Chile'}
        self.a = self.reservar_destino()
        return [f"Usuario - {self.nombre} {self.apellido}, {self.mail}, {self.telefono}, {self.dni} - Trayecto: {self.diccionario[self.a[0]]} hacia {self.diccionario[self.a[1]]}"]
    
    def resumen(self):
        self.ticket_resumen = f"Usuario - {self.nombre} {self.apellido}, {self.mail}, {self.telefono}, {self.dni} - Trayecto: {self.diccionario[self.a[0]]} hacia {self.diccionario[self.a[1]]}"
        return self.ticket_resumen


class Gestor_de_Tickets:
    
    lista_usuarios = []

    def getLista_usuarios(self):
        return self.lista_usuarios


class Vuelos:
    import sqlite3

    miConexion = sqlite3.connect("VuelosDisponiblesAbril")
    miCursor = miConexion.cursor()

    miConexion.commit()
    miConexion.close()


class Menu:
    

    def run(self):
        iniciador = 0
        while iniciador == 0:
            created_user = Usuario()
            app_gestora = Gestor_de_Tickets()
            app_gestora.lista_usuarios.append(created_user.__str__())
            print(created_user.resumen())
            print(app_gestora.getLista_usuarios())
            iniciador = int(input("Ingrese 0 para crear un nuevo usuario y reservar, o 99 para salir: "))


Menu().run()