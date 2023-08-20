class Asiento:
    def __init__(self, color, precio, registro):
        self.color = color
        self.precio = precio
        self.registro = registro

    def cambiarColor(self, color):
        if color in ["rojo", "verde", "amarillo", "negro", "blanco"]:
            self.color = color


class Auto:
    cantidadCreados = 1
    def __init__(self, modelo, precio, asientos, marca, motor, registro):
        self.modelo = modelo
        self.precio = precio
        self.asientos = asientos
        self.marca = marca
        self.motor = motor
        self.registro = registro

    def cantidadAsientos(self):
        return sum(1 for a in self.asientos if isinstance(a, Asiento))

    def verificarIntegridad(self):
        registro_auto = self.registro
        for asiento in self.asientos:
            if isinstance(asiento, Asiento):
                if registro_auto != asiento.registro:
                    return 'Las piezas no son originales'
        if registro_auto != self.motor.registro:
            return 'Las piezas no son originales'
        return 'Auto original'

class Motor:
    def __init__(self, numeroCilindros, tipo, registro):
        self.numeroCilindros = numeroCilindros
        self.tipo = tipo
        self.registro = registro

    def cambiarRegistro(self, registro):
        self.registro = registro

    def asignarTipo(self, tipo):
        if tipo in ["electrico", "gasolina"]:
            self.tipo = tipo

