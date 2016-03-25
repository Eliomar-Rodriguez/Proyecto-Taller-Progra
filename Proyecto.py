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

cursos=[{"codigo":"123","nombre_curso":"Discreta","evaluaciones":{}},{"codigo":"111","nombre_curso":"General","evaluaciones":{}}]


#de prueba
def menu_profes(x):
    print("Bienvenido ",x)
    print("""1.Cursos
    2.Estudiantes
    3.Evaluaciones
    4.Consultas
    5.Cerrar Sesión""")



#de prueba
def menu_estudiantes(x):
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
        carne1=(input("Digite el número de carnet."))
        if carne1.isdigit():
            carne=carne1
        else:
            print("\nEl número de carnet debe de contener únicamente números, inténtalo nuevamente.\n")
            logup()
    elif tipo=="2":
        carne1=input("Digite el número de cédula.")
        if carne1.isdigit():
            carne=carne1
        else:
            print("\nEl número de cédula debe de contener únicamente números, inténtalo nuevamente.\n")
            logup()
    elif tipo=="3":
        menu_principal()
    else:
        print("Error en los datos, inténtalo nuevamente.")
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
    elif tipo=="2":
        estudiantes_y_profes.append({"nombre":name,"correo":mail,"pass":contra,"id":carne,"tipo":tipo})
    print("El proceso de registro se realizó correctamente.")
    menu_principal()
    return



#menú principal totalmente listo
def menu_principal():
    print("  _ _ _   _ _ _   _ _ _        _ _ _     _ _    _ _ _     _ _   _ _ _     _       |")
    print("    |    |       |            |      -    |   _       -    |      |     _   _     |")
    print("    |    | _     |            |       -   |   _   _ _ _    |      |    _     _    |")
    print("    |    |       |            |       -   |   _        -   |      |   _  _ _  _   |")
    print("    |    |_ _ _  |_ _ _       |_ _ _ -   _|_    _  _  -   _|_     |  _         _  |_ _ _")

    print("\t\t\t\t\t\t_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    print("""\t\t\t\t\t   |       1. Iniciar sesión.      |
\t\t\t\t\t   |       2. Crear Cuenta.        |
\t\t\t\t\t   |       3. Salir                |
\t\t\t\t\t   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|""")
    op=(input("""\t\t\t\t\t   | Digite la opción a elegir.    |
                       |       """))
    print("\t\t\t\t\t   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n")
    if op=="1":
        login()
    elif op=="2":
        logup()
    elif op=="3":
        quit()
    else:
        print("\n _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
        print("|     Error en los datos, debe de digitar una opción válida.    |")
        print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n")
        menu_principal()



#login totalmente listo
def login():
    print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    ide=input("| Digite su identificación.    ")
    passw=input("| Digite su contraseña.        ")
    print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n")
    for i in  range (0,len(estudiantes_y_profes)):
        if ide==estudiantes_y_profes[i]["id"] and passw==estudiantes_y_profes[i]["pass"]:
            if estudiantes_y_profes[i]["tipo"]=="1":
                x=estudiantes_y_profes[i]["nombre"]
                return menu_estudiantes(x)
            elif estudiantes_y_profes[i]["tipo"]=="2":
                x=estudiantes_y_profes[i]["nombre"]
                return menu_profes(x)
    print(" Datos no válidos, inténtalo nuevamente.\n")

    login()



#agregar evaluaciones en proceso
def add_evaluations():
    x=0
    code_course=input("Digite el código del curso. ")
    for i in cursos:
        if code_course ==i["codigo"]:
            print("----------------------------------")
            print("-  Evaluaciones predeterminadas  -")
            print("----------------------------------")
            print("""
        1.Tarea
        2.Proyecto
        3.Exámen
        4.Prueba Corta
        5.Quiz
        6.Laboratorio
        7.Otro
            """)
            resp=input("Digite la opción de la evaluación que desea crear. ")
            if resp=="1":
                name_eval="porc_tarea"
            elif resp=="2":
                name_eval="porc_proyecto"
            elif resp=="3":
                name_eval="porc_examen"
            elif resp=="4":
                name_eval="porc_pruebcort"
            elif resp=="5":
                name_eval="porc_quiz"
            elif resp=="6":
                name_eval="porc_laboratorio"
            elif resp=="7":
                name_eval=input("Digite el nombre de la evaluación que desea crear.  ")
            else:
                print("Error en los datos, inténtalo nuevamente.")
                add_evaluations()
            porcantaje=input("Digite el procenteje que la va a asignar a ésta evaluación, de 0% a 100%  ")
            #for q in cursos:
             #   for i in q:
              #      print(i)
                    #x+=i
            #print("Por el momento el porcentaje asignado es de",x)
            for j in cursos:
                for evaluaciones in j:
                    evaluaciones[name_eval]=porcantaje

    print("El código que ingresó del curso no existe, inténtalo nuevamente.")
    add_evaluations()



#en proceso
def edit_evaluations():
    print("Editar Evaluaciones")



#en proceso
def del_evaluations():
    print("Eliminar Evaluaciones")


#menu de evaluaciones listo
def menu_evaluaciones():
    print("----------------------------------")
    print("-------|   Evaluaciones   |-------")
    print("----------------------------------")
    op=input("""-   1. Agregar evaluaciones      -
-   2. Modificar evaluaciones    -
-   3. Eliminar evaluaciones     -
-   4. Menú principal
-    """)
    if op.isdigit():
        if op=="1":
            add_evaluations()
        elif op=="2":
            edit_evaluations()
        elif op=="3":
            del_evaluations()
        elif op=="4":
            menu_principal()
        else:
            print("\n__________________________________")
            print(">>Debe de digitar datos válidos.<<")
            print("__________________________________\n")
            menu_evaluaciones()
    else:
        print("\n__________________________________")
        print(">>Debe de digitar datos válidos.<<")
        print("__________________________________\n")
        menu_evaluaciones()