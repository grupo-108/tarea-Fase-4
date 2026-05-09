from clientes.cliente import Cliente
from servicios.reserva_sala import ReservaSala
from servicios.alquiler_equipo import AlquilerEquipo
from servicios.asesoria import AsesoriaEspecializada
from reservas.reserva import Reserva
import logging

# Configuración de logs
logging.basicConfig(filename="logs/logs.txt", level=logging.INFO)

def main():
    print("=== Simulación del sistema SoftwareFJ ===")

    # 1. Cliente válido
    try:
        cliente1 = Cliente(1, "Ana", "ana@mail.com", "123456")
        print("Cliente válido creado:", cliente1.nombre)
    except Exception as e:
        logging.error(f"Error creando cliente válido: {e}")

    # 2. Cliente inválido (email incorrecto)
    try:
        cliente2 = Cliente(2, "Luis", "luismail.com", "987654")
    except Exception as e:
        logging.error(f"Error creando cliente inválido: {e}")

    # 3. Servicio correcto
    servicio1 = ReservaSala(101, "Sala Ejecutiva")

    # 4. Reserva exitosa
    try:
        reserva1 = Reserva(cliente1, servicio1, 3)
        costo = reserva1.confirmar()
        print(f"Reserva confirmada con costo: {costo}")
    except Exception as e:
        logging.error(f"Error en reserva: {e}")

    # 5. Reserva fallida (duración negativa)
    try:
        servicio2 = AsesoriaEspecializada(102, "Consultoría TI")
        reserva2 = Reserva(cliente1, servicio2, -2)
        reserva2.confirmar()
    except Exception as e:
        logging.error(f"Error en reserva inválida: {e}")

    print("=== Fin de la simulación ===")

if __name__ == "__main__":
    main()
