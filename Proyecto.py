
def logout():
    carne=int(input("Digite el número de carnet."))
    name=int(input("Digite su nombre completo."))
    mail=int(input("Digite su correo electrónico."))
    contra=int(input("Digite la contraseña que desea utilizar."))
    users.append([carne,name,mail,contra])


def login():
    print("Hola")

print("""                 Menú de inico de sesión
                    1. Iniciar sesión.
                    2. Crear Cuenta.
    """)
op=int(input("Digite la opción a elegir."))
if op==1:
    login()
elif op==2:
    logout()
else:
    print("Error en los datos")


