from abc import ABC, abstractmethod

class Servicio(ABC):
    def __init__(self, nombre, costo_base):
        self.nombre = nombre
        self.costo_base = costo_base

    @abstractmethod
    def calcular_costo(self, duracion=1, impuesto=0.0, descuento=0.0):
        pass

class ReservaSala(Servicio):
    def calcular_costo(self, duracion=1, impuesto=0.0, descuento=0.0):
        return (self.costo_base * duracion) * (1 + impuesto) - descuento

class AlquilerEquipo(Servicio):
    def calcular_costo(self, duracion=1, impuesto=0.0, descuento=0.0):
        return (self.costo_base * duracion) * (1 + impuesto) - descuento

class AsesoriaEspecializada(Servicio):
    def calcular_costo(self, duracion=1, impuesto=0.0, descuento=0.0):
        return (self.costo_base * duracion) * (1 + impuesto) - descuento
