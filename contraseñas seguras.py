import random
import string

def generar_contrasena(longitud):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contrasena = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contrasena

longitud_contrasena = 12  # Puedes ajustar la longitud de la contraseña según tus necesidades
contrasena_generada = generar_contrasena(longitud_contrasena)

print("Contraseña generada:", contrasena_generada)
