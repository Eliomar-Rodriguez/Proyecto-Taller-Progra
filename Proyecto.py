estudiantes_y_profes=[{"nombre":"Vera Gamboa","Correo":"vgamboa@itcr.ac.cr","pass":"vgamboa","id":"309870123","tipo":"2","telefono":"88765412"},
                      {"nombre":"Diego Rojas","correo":"drojas@itcr.ac.cr","pass":"drojas","id":"109870654","tipo":"2","telefono":"12347654"},
                      {"nombre":"Eladio Cruz","correo":"ecruz@itcr.ac.cr","pass":"ecruz","id":"207650987","tipo":"2","telefono":"24750091"},
                      {"nombre":"Diego Mora","correo":"dmora@itcr.ac.cr","pass":"dmora","id":"701230234","tipo":"2","telefono":"50986123"},
                      {"nombre":"Steven Peraza","correo":"stevenperaza@gmail.com","pass":"stevenperaza","id":"2016074411","tipo":"1","carrera":"1","telefono":"70245788"},
                      {"nombre":"Kembly Salazar","correo":"kemsalazar@gmail.com","pass":"kemsalazar","id":"2016402331","tipo":"1","carrera":"5","telefono":"50887766"},
                      {"nombre":"Juan Mora","correo":"jmora@hotmail.com","pass":"jmora123","id":"2010198009","tipo":"1","carrera":"3","telefono":"27471385"},
                      {"nombre":"Gabriel Martinez","correo":"gmartinez@estudiantec.cr","pass":"gmatinez","id":"2013443216","tipo":"1","carrera":"1","telefono":"60998945"},
                      {"nombre":"Juan Rafael Morales","correo":"jrmorales@hotmail.com","pass":"jrmorales96","id":"2014772139","tipo":"1","carrera":"2","telefono":"62436822"},
                      {"nombre":"Carlos Morera","correo":"cmorera21@gmail.com","pass":"cmorera","id":"2009123456","tipo":"1","carrera":"4","telefono":"24602221"},
                      {"nombre":"Eliomar Rodríguez","correo":"rodriguez.elio.97@gmail.com","pass":"Capitan1","id":"2016108660","tipo":"2","carrera":"1","telefono":"87237514"},
                      {"nombre":"Angelo Medina","correo":"amedina@estudiantec.cr","pass":"amedina","id":"2016109990","tipo":"1","carrera":"5","telefono":"24619877"},
                      {"nombre":"Juan Primito Rivas","correo":"jprivas@gmail.com","pass":"jprivas","id":"2015012349","tipo":"1","carrera":"3","telefono":"4751218"},
                      {"nombre":"Jafeth Salas","correo":"jafsal97@gmail.com","pass":"Jafsal123","id":"2016421763","tipo":"1","carrera":"3","telefono":"88772197"},
                      {"nombre":"Carlos Restrepo Marín","correo":"crmarin21@gmail.com","pass":"crmarin21","id":"2016198611","tipo":"1","carrera":"1","telefono":"88710712"},
                      {"nombre":"Antonio Rodríguez Arguedas","correo":"antonio16--2012@hotmail.com","pass":"Capitan123","id":"2016108661","tipo":"1","carrera":"2","telefono":"24761213"},
                      {"nombre":"Angelo Aguilar","correo":"angelomix@gmail.com","pass":"mixmix1","id":"2011152364","tipo":"1","carrera":"3","telefono":"89654310"},
                      {"nombre":"Josue Chaves","correo":"jchaves@gmail.com","pass":"jchaves","id":"2009887512","tipo":"1","carrera":"4","telefono":"70223112"},
                      {"nombre":"Joshua Ramirez","correo":"jramirez4223@gmail.com","pass":"lolita123","id":"2014723912","tipo":"1","carrera":"3","telefono":"87341514"},
                      {"nombre":"Dere Solorzano","correo":"dsolorsano97@gmail.com","pass":"matediscreta","id":"2014334523","tipo":"1","carrera":"2"},
                      {"nombre":"Agie Rodriguez Arguedas","correo":"arodriarg@estudiantec.cr","pass":"arodriarg","id":"2011321937","tipo":"1","carrera":"1","telefono":"24756623"},
                      {"nombre":"Juan Carlos Arias","correo":"jcarias@hotmail.com","pass":"jcarias","id":"2012202421","tipo":"1","carrera":"2","telefono":"87651164"},
                      {"nombre":"Carlos José Mora","correo":"cjmora@hotmail.com","pass":"cjmora","id":"2010356721","tipo":"1","carrera":"3","telefono":"40224312"},
                      {"nombre":"Silvia Fulopp Patiño","correo":"silfupat48@gmail.com","pass":"gatoconrabia123","id":"2014234667","tipo":"1","carrera":"4","telefono":"50123381"},
                      {"nombre":"Carlos Restrepo Marín","correo":"cremarin@estudiantec.cr","pass":"carritoazul297","id":"2009176889","tipo":"1","carrera":"5","telefono":"89764528"},]#Estudiantes y profesores

cursos=[{"codigo":"123","nombre_curso":"Discreta","tottareas":0,"tareas":["tarea1",1,"tarea2",2,"tarea3",3,"tarea4",4],"totexaemenes":0,"examenes":[],"totproyectos":0,"proyectos":[],"totquiz":0,"quiz":[],"tototros":0,"otros":[],"totlaboratorios":0,"laboratorios":[]},{"codigo":"111","nombre_curso":"General","tareas":[],"examenes":[],"proyectos":[],"quiz":[],"otros":[],"laboratorios":[]}]

c=[]

#de prueba
def menu_profes(x):
    print("Bienvenido ",x)
    print("""1.Cursos
    2.Estudiantes
    3.Evaluaciones
    4.Consultas
    5.Cerrar Sesión""")
    op=input("Digite la opción que desea.  ")
    if op=="1":
        print("Retornar a cursos con la x por si necesito enviarlo al menu de profes")#falta agregar cursos
    elif op=="2":
        print("Retornar a estudiantes con la x por si necesito enviarlo al menu de profes") #falta agregar estudiantes
    elif op=="3":
        return menu_evaluaciones(x)
    elif op=="4":
        print("Retornar a consultas con la x por si necesito enviarlo al menu de profes")
    elif op=="5":
        menu_principal()
    else:
        print("Debe digitar datos válidos.")
        menu_profes(x)



#de prueba
def menu_estudiantes(x):
    print("Bienvenido (a) ",x)



#logup totalmente listo
def singup():
    #FUNCION: registro de estudiantes en el sistema
    #ENTRADAS: datos del estudiante para poder guardarlos
    #SALIDAS: almacemaniento de los datos del estudiante
    #RESTRICCIONES: debe ser un estudiante nuevo, no podrá crear una cuenta con un carnet o cedula que ya se encuentre registrado
    print("""Digite el tipo de cuenta que va a crear
                                                1. Estudiante
                                                2. Profesor
                                                3. Volver al menú principal""")
    tipo=input("""Digite la opción deseada.
""")
    if tipo=="1":
        carne1=(input("Digite el número de carnet."))
        for m in estudiantes_y_profes:   #busca que el carnet digitado no se encuentre registrado
            if carne1==m["id"]:
                print(" _ _ _ _ _ _ _ _ _ ")
                print("""|      Error      |
|- - - - - - - - -|- - - - - - - - - - - - - -|
|   El número de carnet ingresado pertenece   |
|   a otro usuario que ya está registrado,    |
|   inténtalo nuevamente.                     | """)
                print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")
                singup()
            elif carne1.isdigit():
                carne=carne1
            else:
                print("\nEl número de carnet debe de contener únicamente números, inténtalo nuevamente.\n")
                singup()

    elif tipo=="2":
        carne1=input("Digite el número de cédula.")
        for m in estudiantes_y_profes:      #busca que la cedula digitada no se encuentre registrada
            if carne1==m["id"]:
                print(" _ _ _ _ _ _ _ _ _ ")
                print("""|      Error      |
|- - - - - - - - -|- - - - - - - - - - - - - -|
|   El número de carnet ingresado pertenece   |
|   a otro usuario que ya está registrado,    |
|   inténtalo nuevamente.                     | """)
                print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")
                singup()
            elif carne1.isdigit():
                carne=carne1
            else:
                print("\nEl número de cédula debe de contener únicamente números, inténtalo nuevamente.\n")
                singup()
    elif tipo=="3":
        menu_principal()
    else:
        print("Error en los datos, inténtalo nuevamente.")
        singup()
    name=input("Digite su nombre completo.")
    telef=input("Digite su número de teléfono.")
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
        estudiantes_y_profes.append({"nombre":name,"correo":mail,"pass":contra,"id":carne,"tipo":tipo,"carrera":carrera,"telefono":telef})  #Guardo la informacion
    elif tipo=="2":
        estudiantes_y_profes.append({"nombre":name,"correo":mail,"pass":contra,"id":carne,"tipo":tipo})
    print("El proceso de registro se realizó correctamente.")
    menu_principal()
    return



#menú principal totalmente listo
def menu_principal():
    #FUNCION: menu principal, aqui el usuario decide que hacer si ingresar al sistema en caso de tener cuenta o registrarse para ingresar
    #ENTRADAS: opcion que desea ejecutar
    #SALIDAS: proceso de ingreso o proceso de registro
    #RESTRICCIONES: la opcion debe ser un numero entero, ya sea 1, 2, o 3
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
        singup()
    elif op=="3":
        quit()
    else:
        print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
        print("""| >> Error en su respuesta << |
|- - - - - - - - - - - - - - -|- - - - - - - -|
|   La respuesta que usted ingresó no es      |
|   ninguna de las anteriores, por favor      |
|   digite una opción válida.                 | """)
        print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n")
        menu_principal()



#login totalmente listo
def login():
    #FUNCION: Tomar los datos del usuario para enviarlo a su respectivo menu, ya sea estudiante o profesor
    #ENTRADAS: el ususario debe digitar su cedula en caso de profesor o su carnet en caso de estudiante y luego la contraseña
    #SALIDAS:enviarlo al menu que le corresponde
    #RESTRICCIONES: debe digitar el carnet o cedula junto con la contraseña bien
    print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    ide=input("| Digite su identificación.    ")
    passw=input("| Digite su contraseña.        ")
    print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n")
    for i in  range (0,len(estudiantes_y_profes)):
        if ide==estudiantes_y_profes[i]["id"] and passw==estudiantes_y_profes[i]["pass"]: #proceso de validacion si existen esos datos y corresponden a un usuario especifico
            if estudiantes_y_profes[i]["tipo"]=="1": #si el usuario es de tipo 1 es decir estudiantes entonces...
                x=estudiantes_y_profes[i]["nombre"]     #...en una variable guardo el nombre y luego...
                return menu_estudiantes(x)              #lo envio al menu de estudiantes donde recibira la variable con el nombre para mostrarlo
            elif estudiantes_y_profes[i]["tipo"]=="2":  #Si el usuario es de tipo 2 es decir profesor entonces lo envio a su respectivo menu
                x=estudiantes_y_profes[i]["nombre"]
                return menu_profes(x)
    print(" Datos no válidos, inténtalo nuevamente.\n")#sino estan los datos se le muestra un mensaje y el proceso se repite hasta que ingrese bien los datos
    login()



def nomporeva(hh,resp):
    #FUNCION: guardar evaluaciones
    #ENTRADAS: nombre de la evaluacion, porcentaje a asignar
    #SALIDAS: crear la evaluacion
    #RESTRICCIONES: no debe existir una evaluacion con el mismo nombre, el porcentaje no puede pasarse de 100%, el procentaje debe tener punto en vez de coma

    if resp=="1":
        evaluacion="tareas"
    elif resp=="2":
        evaluacion="proyectos"
    elif resp=="3":
        evaluacion="examenes"
    elif resp=="4":
        evaluacion="quiz"
    elif resp=="5":
        evaluacion="laboratorios"
    elif resp=="6":
        evaluacion="otros"
    name_eval=input("Digite el nombre de la evaluación a crear. ")
    for i in cursos:
        if hh==i["codigo"]:
            if name_eval in i[evaluacion]:
                print("Error, la tarea a crear ya existe. ")
                add_evaluations()
            else:
                for m in i:
                    if name_eval in m: #si la evaluacion a crear ya existe entonces entonces se le pone un mensaje de error
                        print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                        print("""| >> Error en la operación << |
|- - - - - - - - - - - - - - -|- - - - - - - - -|
|  El nombre que le asignó a la evaluación que  |
|      usted intenta crear ya está siendo       |
|   utilizado en otra evaluación, elija otro    |
|       nombre e inténtalo nuevamente.        |""")
                        print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n")
                        add_evaluations()
                    else:
                        try:
                            print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
                            print("|    El porcentaje a asignar debe de tener punto, ejemplo: 15.7     |")
                            print("|  El porcentaje total de este tipo de evaluación no puede superar  |")
                            print("|                            el 100%                                |")
                            print(" - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
                            porcantaje=float(input("Digite el procenteje a asignar  "))
                            c.append(name_eval) #proceso de agregar la evaluacion
                            c.append(porcantaje)
                            break
                        except ValueError:
                            print("Error en los datos, el número decimal debe de usar punto en vez de coma. ")
                            add_evaluations()
                            break


#agregar totalmente listo
def add_evaluations():
    #FUNCION:   egreagar evaluaciones a cada curso
    #ENTRADAS:  el tipo de evaluacion, porcentaje y nombre
    #SALIDAS:   guardar la evaluacion
    #RESTRICCIONES: el porcentaje de tareas no debe sobrepasar el 100%
    tot=0
    code_course=input("Digite el código del curso. ")
    for i in cursos:
        if code_course ==i["codigo"]: #recorro la lista de cursos en busca del codigo del curso
            print("----------------------------------")
            print("-  Evaluaciones predeterminadas  -")
            print("----------------------------------")
            print("""
            1.Tarea
            2.Proyecto
            3.Exámen
            4.Prueba Corta (quiz)
            5.Laboratorio
            6.Otro
            """)
            resp=input("Digite la opción de la evaluación que desea crear. ")
            hh=code_course
            if resp=="1":
                nomporeva(hh,resp)
                i['tareas']=i['tareas']+c
                print(cursos)
            elif resp=="2":
                nomporeva(hh,resp)
                i['proyectos']=i['proyectos']+c
                print(cursos)
            elif resp=="3":
                nomporeva(hh,resp)
                i['examenes']=i['examenes']+c
                print(cursos)
            elif resp=="4":
                nomporeva(hh,resp)
                i['quiz']=i['quiz']+c
                print(cursos)
            elif resp=="5":
                nomporeva(hh,resp)
                i['laboratorios']=i['laaboratorios']+c
                print(cursos)
            elif resp=="6":
                nomporeva(hh,resp)
                i['otros']=i['otros']+c
                print(cursos)
            else:
                print("Digite un valor válido, por favor ")
                add_evaluations()




#en proceso
def edit_evaluations():
    x=""
    code_course=input("Digite el código del curso. ")
    for i in cursos:
        if code_course ==i["codigo"]:
            print("--------------------------------------")
            print("-   Tipos de evaluaciones a editar   -")
            print("--------------------------------------")
            print("""
            1.Tarea
            2.Proyecto
            3.Exámen
            4.Prueba Corta (quiz)
            5.Laboratorio
            6.Otro
            """)
            resp=input("Digite la opción de la evaluación que desea eliminar. ")
            if resp=="1":
                posicion="tareas"
            elif resp=="2":
                posicion="proyectos"
            elif resp=="3":
                posicion="examenes"
            elif resp=="4":
                posicion="quiz"
            elif resp=="5":
                posicion="laboratorios"
            elif resp=="6":
                posicion="otros"
            else:
                print("Error, debe digitar una opción válida. ")
                edit_evaluations()
            print("\nEstas son las tareas creadas en este curso: ")
            for p in range (0,len (i["tareas"]),2):
                z=p+1
                print("\t",i['tareas'][p],"\t",i['tareas'][z])
            op=input("""¿Qué desea modificar?
            1.Nombre de la evaluación
            2.Porcentaje asignado
            """)
            if op=="1":
                nombre_viejo=input("Digite el nombre de la evaluación a modificar. ")
                new_name=input("Digite el nuevo nombre a asignar")
                for u in i["tareas"]:
                    if nombre_viejo==u[i("tareas")]:
                        nombre_viejo[u]=new_name
                print(cursos)

            elif op=="2":
                nombre_viejo=input("Digite el nombre de la evaluación a modificar. ")
                porc=input("Digite el nuevo porcentaje que asiganará. ")
                if nombre_viejo in i["tareas"]:
                    i[nombre_viejo]=porc
            elif op=="3":
                menu_profes(x)
            else:
                print("Error, debe digitar alguna de las opciones. ")


#en proceso
def del_evaluations():
    code_course=input("Digite el código del curso. ")
    for i in cursos:
        if code_course ==i["codigo"]:
            print("--------------------------------------")
            print("-  Tipos de Evaluaciones a eliminar  -")
            print("--------------------------------------")
            print("""
            1.Tarea
            2.Proyecto
            3.Exámen
            4.Prueba Corta (quiz)
            5.Laboratorio
            6.Otro
            """)
            resp=input("Digite la opción de la evaluación que desea eliminar. ")
            if resp=="1":
                posicion="tareas"
            elif resp=="2":
                posicion="proyectos"
            elif resp=="3":
                posicion="examenes"
            elif resp=="4":
                posicion="quiz"
            elif resp=="5":
                posicion="laboratorios"
            elif resp=="6":
                posicion="otros"

            delpala=input("Digite el nombre de la evaluación que desea eliminar. ")
            for d in i[posicion]:
                if d==delpala:
                    print(d)
                    print(delpala)
                    del i[posicion][d]

                if delpala==d:
                    del i[posicion][d]

                    try:

                        #if delpala==d:
                            #xx=d
                        #del i[posicion][d]          #BUSCAR Y ELIMINAR LOS DOS DATOS, YA QUE ESTA ELIMINANDO SOLAMENTE UNO

                        print(cursos)
                        #print(xx)
                        break

                    except:
                        print("listo")
            else:
                print("La palabra que busca eliminar no se encuentró, inténtalo nuevamente. ")
                del_evaluations()




#menu de evaluaciones listo
def menu_evaluaciones(x):
    print("----------------------------------")
    print("-------|   Evaluaciones   |-------")
    print("----------------------------------")
    op=input("""-   1. Agregar evaluaciones      -
-   2. Modificar evaluaciones    -
-   3. Eliminar evaluaciones     -
-   4. Menú de profesores
-    """)
    if op.isdigit():
        if op=="1":
            return add_evaluations()
        elif op=="2":
            return edit_evaluations(x)
        elif op=="3":
            return del_evaluations(x)
        elif op=="4":
            return menu_profes(x)
        else:
            print("\n__________________________________")
            print(">>Debe de digitar datos válidos.<<")
            print("__________________________________\n")
            menu_evaluaciones(x)
    else:
        print("\n__________________________________")
        print(">>Debe de digitar datos válidos.<<")
        print("__________________________________\n")
        menu_evaluaciones(x)

menu_principal()