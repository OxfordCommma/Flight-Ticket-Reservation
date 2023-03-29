import sqlite3

class Vuelos():

    def muestra_vuelos(self, salida, destino):
        self.salida = salida
        self.destino = destino
        miConexion = sqlite3.connect("VuelosDisponiblesAbril")
        miCursor = miConexion.cursor()
            
        self.diccionario = {1: 'Argentina', 2: 'Brasil', 3: 'Uruguay', 4: 'Peru', 5: 'Chile'}
        
        miCursor.execute(f"SELECT * FROM VUELOS WHERE PARTIDA = '{self.diccionario[self.salida]}' AND DESTINO ='{self.diccionario[self.destino]}'")
        self.todos_los_vuelos = miCursor.fetchall()
        return self.todos_los_vuelos




