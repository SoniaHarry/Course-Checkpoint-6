
class Usuario:
    def __init__ (self, nombre, contraseña):
        self.nombre=nombre
        self.contraseña=contraseña

MiUsuario=Usuario("Sonia","pepitogrillo")

print(MiUsuario.nombre) #Sonia
print(MiUsuario.contraseña) #pepitogrillo
