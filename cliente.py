from excepciones import ClienteInvalidoError

class Cliente:
    def __init__(self, nombre, correo):
        self.__nombre = nombre
        self.__correo = correo

    def validar(self):
        if not self.__nombre or "@" not in self.__correo:
            raise ClienteInvalidoError("Datos de cliente inválidos")

    def get_nombre(self):
        return self.__nombre

    def get_correo(self):
        return self.__correo
