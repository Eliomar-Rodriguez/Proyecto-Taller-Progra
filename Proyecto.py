def menu_profes():
    print("")


def logup():
    print("""Digite el tipo de cuenta que va a crear
                                                    1. Estudiante
                                                    2. Profesor""")
    tipo=int(input("Digite el tipo de cuenta que va a crear"))
    carne=int(input("Digite el número de carnet."))
    name=input("Digite su nombre completo.")
    mail=input("Digite su correo electrónico.")
    contra=input("Digite la contraseña que desea utilizar.")

    usuarios=[]
    usuarios.append([carne,name,mail,contra,tipo])
    print("El proceso de registro se realizó correctamente.")
    menu_principal()
    return usuarios

def login(usuarios): ################################### PENDIENTE  ##################################
    user=input("Digite su usuario")
    password=input("Digite la contraseña")
    i=0
    j=0
    if user==usuarios[i][0] and password==usuarios[i][3]:
        print("correcto")

def menu_principal():
    print("""                 Menú de inico de sesión
                    1. Iniciar sesión.
                    2. Crear Cuenta.
                    3. Salir
    """)
    op=int(input("Digite la opción a elegir."))
    if op==1:
        login()
    elif op==2:
        logup()
    elif op==3:
        quit()
    else:
        print("Error en los datos, debe de digitar una opción válida.")

def menu_estudiantes():
    print("")

menu_principal()