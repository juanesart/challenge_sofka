class Carril:
    def __init__(self, limite, auto):
        self.limite = limite
        self.auto = auto.marca
        self.id = auto.id
    
def crearCarril(limite, auto):
    carril = Carril(limite, auto)
    return carril
