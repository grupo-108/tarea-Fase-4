from excepciones import ReservaError
from logger import registrar_error

class Reserva:
    def __init__(self, cliente, servicio, duracion):
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "Pendiente"

    def confirmar(self):
        try:
            self.cliente.validar()
            costo = self.servicio.calcular_costo(self.duracion, impuesto=0.19)
            self.estado = "Confirmada"
            return f"Reserva confirmada. Costo: {costo}"
        except Exception as e:
            registrar_error(f"Error en reserva: {e}")
            self.estado = "Error"
            raise ReservaError("No se pudo confirmar la reserva")
