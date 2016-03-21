estudiantes_y_profes=[{"nombre":"Vera Gamboa","Correo":"vgamboa@itcr.ac.cr","pass":"vgamboa","id":"309870123","tipo":"2"},
                      {"nombre":"Diego Rojas","correo":"drojas@itcr.ac.cr","pass":"drojas","id":"109870654","tipo":"2"},
                      {"nombre":"Eladio Cruz","correo":"ecruz@itcr.ac.cr","pass":"ecruz","id":"207650987","tipo":"2"},
                      {"nombre":"Diego Mora","correo":"dmora@itcr.ac.cr","pass":"dmora","id":"701230234","tipo":"2"},
                      {"nombre":"Steven Peraza","correo":"stevenperaza@gmail.com","pass":"stevenperaza","id":"2016112209","tipo":"1","carrera":"1"},
                      {"nombre":"Kembly Salazar","correo":"kemsalazar@gmail.com","pass":"kemsalazar","id":"2016402331","tipo":"1","carrera":"5"},
                      {"nombre":"Juan Mora","correo":"jmora@hotmail.com","pass":"jmora123","id":"2010198009","tipo":"1","carrera":"3"},
                      {"nombre":"Gabriel Martinez","correo":"gmartinez@estudiantec.cr","pass":"gmatinez","id":"2013443216","tipo":"1","carrera":"1"},
                      {"nombre":"Juan Rafael Morales","correo":"jrmorales@hotmail.com","pass":"jrmorales96","id":"2014772139","tipo":"1","carrera":"2"},
                      {"nombre":"Carlos Morera","correo":"cmorera21@gmail.com","pass":"cmorera","id":"2009123456","tipo":"1","carrera":"4"},
                      {"nombre":"Eliomar Rodríguez","correo":"rodriguez.elio.97@gmail.com","pass":"Capitan1","id":"2016108660","tipo":"1","carrera":"1"},
                      {"nombre":"Angelo Medina","correo":"amedina@estudiantec.cr","pass":"amedina","id":"2016109990","tipo":"1","carrera":"5"},
                      {"nombre":"Juan Primito Rivas","correo":"jprivas@gmail.com","pass":"jprivas","id":"2015012349","tipo":"1","carrera":"3"},
                      {"nombre":"Jafeth Salas","correo":"jafsal97@gmail.com","pass":"Jafsal123","id":"2016421763","tipo":"1","carrera":"3"},
                      {"nombre":"Carlos Restrepo Marín","correo":"crmarin21@gmail.com","pass":"crmarin21","id":"2016198611","tipo":"1","carrera":"1"},
                      {"nombre":"Antonio Rodríguez Arguedas","correo":"antonio16--2012@hotmail.com","pass":"Capitan123","id":"2016108661","tipo":"1","carrera":"2"},
                      {"nombre":"Angelo Aguilar","correo":"angelomix@gmail.com","pass":"mixmix1","id":"2011152364","tipo":"1","carrera":"3"},
                      {"nombre":"Josue Chaves","correo":"jchaves@gmail.com","pass":"jchaves","id":"2009887512","tipo":"1","carrera":"4"},
                      {"nombre":"Joshua Ramirez","correo":"jramirez4223@gmail.com","pass":"lolita123","id":"2014723912","tipo":"1","carrera":"3"},
                      {"nombre":"Dere Solorzano","correo":"dsolorsano97@gmail.com","pass":"matediscreta","id":"2014334523","tipo":"1","carrera":"2"},
                      {"nombre":"Agie Rodriguez Arguedas","correo":"arodriarg@estudiantec.cr","pass":"arodriarg","id":"2011321937","tipo":"1","carrera":"1"},
                      {"nombre":"Juan Carlos Arias","correo":"jcarias@hotmail.com","pass":"jcarias","id":"2012202421","tipo":"1","carrera":"2"},
                      {"nombre":"Carlos José Mora","correo":"cjmora@hotmail.com","pass":"cjmora","id":"2010356721","tipo":"1","carrera":"3"},
                      {"nombre":"Silvia Fulopp Patiño","correo":"silfupat48@gmail.com","pass":"gatoconrabia123","id":"2014234667","tipo":"1","carrera":"4"},
                      {"nombre":"Carlos Restrepo Marín","correo":"cremarin@estudiantec.cr","pass":"carritoazul297","id":"2009176889","tipo":"1","carrera":"5"},]#Estudiantes y profesores

def menu_profes(x):
    print("Bienvenido ",x)

#logup totalmente listo
def logup():
    print("""Digite el tipo de cuenta que va a crear
                                                    1. Estudiante
                                                    2. Profesor
                                                    3. Volver al menú principal""")
    tipo=input("""Digite la opción deseada
""")
    if tipo=="1":
        carne=(input("Digite el número de carnet."))
    elif tipo=="2":
        carne=input("Digite el número de cédula.")
    elif tipo=="3":
        menu_principal()
    else:
        print("Error, inténtalo nuevamente.")
        logup()
    name=input("Digite su nombre completo.")
    mail=input("Digite su correo electrónico.")
    contra=input("Digite la contraseña que desea utilizar.")
    if tipo=="1":
        print("""
        1. Ingeniería en Computación
        2. Ingeniería en Producción Industrial
        3. Ingeniería en Agronomía
        3. Electrónica
        4. Gestión del Turismo Rural Sostenible
        5. Administración de Empresas
        """)
        carrera=input("Digite la opción de su carrera.")
        estudiantes_y_profes.append({"nombre":name,"correo":mail,"pass":contra,"id":carne,"tipo":tipo,"carrera":carrera})
    else:
        print("Error en los datos, inténtalo nuevamente.")
    estudiantes_y_profes.append({"nombre":name,"correo":mail,"pass":contra,"id":carne,"tipo":tipo})
    print("El proceso de registro se realizó correctamente.")
    menu_principal()
    return


def menu_principal():
    print("""                 Menú de inico de sesión
                    1. Iniciar sesión.
                    2. Crear Cuenta.
                    3. Salir
    """)
    op=(input("""Digite la opción a elegir.
"""))
    if op=="1":
        login()
    elif op=="2":
        logup()
    elif op=="3":
        quit()
    else:
        print("\nError en los datos, debe de digitar una opción válida.\n")
        menu_principal()


def menu_estudiantes(x):
    print("Bienvenido ",x)


def login():
    print("______________________________")
    ide=input("Digite su identificación.")
    passw=input("Digite su contraseña")
    for i in  range (0,len(estudiantes_y_profes)):
        if ide==estudiantes_y_profes[i]["id"] and passw==estudiantes_y_profes[i]["pass"]:
            if estudiantes_y_profes[i]["tipo"]=="1":
                x=estudiantes_y_profes[i]["nombre"]
                return menu_estudiantes(x)
            elif estudiantes_y_profes[i]["tipo"]=="2":
                x=estudiantes_y_profes[i]["nombre"]
                return menu_profes(x)
    print("Datos no validos, intentalo nuevamente.")

menu_principal()