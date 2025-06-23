class Coche: 
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

def arrancar(self):
    print("El coche {self.marca}, {self.modelo} ha arrancado")

def detener(self):
    print("El coche {self.marca}, {self.modelo} se ha detenido}")

def pintar(self, nuevo_color):
    self.color = nuevo_color
    print(f"El coche es ahora de color {self.color}.")

def mostrar_info(self):
    print(f"El coche: {self.marca}, {self.modelo}, color: {self.color}")

mi_coche = Coche("Toyota", "Corolla", "Rojo")
   