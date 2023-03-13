class Usuario:
   
    def __init__(self):
        self.nombre = input("Su nombre: ")
        self.apellido = input("Su apellido: ")
        self.mail = input("Su mail: ")
        self.telefono = int(input("Su telefono: "))
        self.dni = int(input("Su DNI: "))
    
    def reservar_destino(self):
        self.reserva_ida = input("Elija un destino del mundo: ")
        return f"Destino elegido: {self.reserva_ida}"
    
    def __str__(self):
        return [f"Usuario - {self.nombre} {self.apellido}, {self.mail}, {self.telefono}, {self.dni} - {self.reservar_destino()}"]
    
    def resumen(self):
        self.ticket_resumen = f"Usuario - {self.nombre} {self.apellido}, {self.mail}, {self.telefono}, {self.dni} - {self.reservar_destino()}"
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
            print(app_gestora.getLista_usuarios())
            iniciador = int(input("Ingrese 0 para crear un nuevo usuario y reservar, o 99 para salir: "))


Menu().run()    
    
        

