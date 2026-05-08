from cliente import Cliente
from servicio import ReservaSala, AlquilerEquipo, AsesoriaEspecializada
from reserva import Reserva
from excepciones import ClienteInvalidoError, ReservaError

def ejecutar_operaciones():
    clientes = [
        Cliente("Ana", "ana@mail.com"),
        Cliente("", "correo_invalido"),  # Error
    ]

    servicios = [
        ReservaSala("Sala de reuniones", 50),
        AlquilerEquipo("Proyector", 30),
        AsesoriaEspecializada("Consultoría TI", 100),
    ]

    operaciones = [
        (clientes[0], servicios[0], 2),
        (clientes[1], servicios[1], -1),  # Error
    ]

    for cliente, servicio, duracion in operaciones:
        try:
            reserva = Reserva(cliente, servicio, duracion)
            print(reserva.confirmar())
        except (ClienteInvalidoError, ReservaError) as e:
            print(f"Operación fallida: {e}")

if __name__ == "__main__":
    ejecutar_operaciones()
