# excepciones.py

class ClienteInvalidoError(Exception):
    """Se lanza cuando los datos del cliente son inválidos."""
    pass

class ReservaInvalidaError(Exception):
    """Se lanza cuando la reserva tiene parámetros incorrectos."""
    pass

class ReservaError(Exception):
    """Error genérico para problemas en reservas."""
    pass

