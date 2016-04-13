estudiantes_y_profes = [
    {"nombre": "Vera Gamboa", "Correo": "vgamboa@itcr.ac.cr", "pass": "vgamboa", "id": "309870123", "tipo": "2",
     "telefono": "88765412"},
    {"nombre": "Diego Rojas", "correo": "drojas@itcr.ac.cr", "pass": "drojas", "id": "109870654", "tipo": "2",
     "telefono": "12347654"},
    {"nombre": "Eladio Cruz", "correo": "ecruz@itcr.ac.cr", "pass": "ecruz", "id": "207650987", "tipo": "2",
     "telefono": "24750091"},
    {"nombre": "Diego Mora", "correo": "dmora@itcr.ac.cr", "pass": "dmora", "id": "701230234", "tipo": "2",
     "telefono": "50986123"},
    {"nombre": "Steven Peraza", "correo": "stevenperaza@gmail.com", "pass": "stevenperaza", "id": "2016074411",
     "tipo": "1", "carrera": "1", "telefono": "70245788"},
    {"nombre": "Kembly Salazar", "correo": "kemsalazar@gmail.com", "pass": "kemsalazar", "id": "2016402331",
     "tipo": "1", "carrera": "5", "telefono": "50887766"},
    {"nombre": "Juan Mora", "correo": "jmora@hotmail.com", "pass": "jmora123", "id": "2010198009", "tipo": "1",
     "carrera": "3", "telefono": "27471385"},
    {"nombre": "Gabriel Martinez", "correo": "gmartinez@estudiantec.cr", "pass": "gmatinez", "id": "2013443216",
     "tipo": "1", "carrera": "1", "telefono": "60998945"},
    {"nombre": "Juan Rafael Morales", "correo": "jrmorales@hotmail.com", "pass": "jrmorales96", "id": "2014772139",
     "tipo": "1", "carrera": "2", "telefono": "62436822"},
    {"nombre": "Carlos Morera", "correo": "cmorera21@gmail.com", "pass": "cmorera", "id": "2009123456", "tipo": "1",
     "carrera": "4", "telefono": "24602221"},
    {"nombre": "Eliomar Rodríguez", "correo": "rodriguez.elio.97@gmail.com", "pass": "Capitan1", "id": "2016108660",
     "tipo": "2", "carrera": "1", "telefono": "87237514"},
    {"nombre": "Angelo Medina", "correo": "amedina@estudiantec.cr", "pass": "amedina", "id": "2016109990", "tipo": "1",
     "carrera": "5", "telefono": "24619877"},
    {"nombre": "Juan Primito Rivas", "correo": "jprivas@gmail.com", "pass": "jprivas", "id": "2015012349", "tipo": "1",
     "carrera": "3", "telefono": "4751218"},
    {"nombre": "Jafeth Salas", "correo": "jafsal97@gmail.com", "pass": "Jafsal123", "id": "2016421763", "tipo": "1",
     "carrera": "3", "telefono": "88772197"},
    {"nombre": "Carlos Restrepo Marín", "correo": "crmarin21@gmail.com", "pass": "crmarin21", "id": "2016198611",
     "tipo": "1", "carrera": "1", "telefono": "88710712"},
    {"nombre": "Antonio Rodríguez Arguedas", "correo": "antonio16--2012@hotmail.com", "pass": "Capitan123",
     "id": "2016108661", "tipo": "1", "carrera": "2", "telefono": "24761213"},
    {"nombre": "Angelo Aguilar", "correo": "angelomix@gmail.com", "pass": "mixmix1", "id": "2011152364", "tipo": "1",
     "carrera": "3", "telefono": "89654310"},
    {"nombre": "Josue Chaves", "correo": "jchaves@gmail.com", "pass": "jchaves", "id": "2009887512", "tipo": "1",
     "carrera": "4", "telefono": "70223112"},
    {"nombre": "Joshua Ramirez", "correo": "jramirez4223@gmail.com", "pass": "lolita123", "id": "2014723912",
     "tipo": "1", "carrera": "3", "telefono": "87341514"},
    {"nombre": "Dere Solorzano", "correo": "dsolorsano97@gmail.com", "pass": "matediscreta", "id": "2014334523",
     "tipo": "1", "carrera": "2"},
    {"nombre": "Agie Rodriguez Arguedas", "correo": "arodriarg@estudiantec.cr", "pass": "arodriarg", "id": "2011321937",
     "tipo": "1", "carrera": "1", "telefono": "24756623"},
    {"nombre": "Juan Carlos Arias", "correo": "jcarias@hotmail.com", "pass": "jcarias", "id": "2012202421", "tipo": "1",
     "carrera": "2", "telefono": "87651164"},
    {"nombre": "Carlos José Mora", "correo": "cjmora@hotmail.com", "pass": "cjmora", "id": "2010356721", "tipo": "1",
     "carrera": "3", "telefono": "40224312"},
    {"nombre": "Silvia Fulopp Patiño", "correo": "silfupat48@gmail.com", "pass": "gatoconrabia123", "id": "2014234667",
     "tipo": "1", "carrera": "4", "telefono": "50123381"},
    {"nombre": "Carlos Restrepo Marín", "correo": "cremarin@estudiantec.cr", "pass": "carritoazul297",
     "id": "2009176889", "tipo": "1", "carrera": "5", "telefono": "89764528"}, ]  # Estudiantes y profesores

cursos = [{"codigo": "123","id":"2016108660","creditos":"2", "nombre": "Discreta", "tottareas": 0,
           "tareas":[{'porcentaje': 2.0, 'nombre': 'tarea1'},{'porcentaje': 3.0, 'nombre': 'tarea2'}], "totexaemenes": 0, "examenes": [],
           "totproyectos": 0, "proyectos": [], "totquiz": 0, "quiz": [], "tototros": 0, "otros": [],
           "totlaboratorios": 0, "laboratorios": [],"estudiantes mat":[]},
          {"codigo": "111", "nombre": "General", "tareas": [], "examenes": [], "proyectos": [], "quiz": [],
           "otros": [], "laboratorios": [],"id":"2016108660","creditos":"2","estudiantes mat":[]}]

c = []
##################################################################################################################################################
##
##          esta parte pertenece a estudiantes
##
##################################################################################################################################################


# Funcion que repite acciones dentro de una funcion, en este caso menu_estudiantes.
# Recibe un string por parte del usuario para regresar al menu principal o salir del programa. La restricción es que la opción debe ser "1" o "2".
def otra_accion_est(xl):
    v = input("""
Desea realizar otra accion?
Si=1
No=2
""")
    if v == "1":
        menu_estudiantes(xl)
    elif v == "2":
        print("Gracias por utilizar este sistema")
        menu_principal()
    else:
        print("Error, digite un valor valido")
        otra_accion_est(xl)
    otra_accion_est(xl)


# Funcion que imprime todos los cursos en los que se encuentra matriculado el estudiante.
# Entrada: ID del estudiante.
# Salida: Lista impresa de todos los cursos matriculados del estudiante con su informacion general.
# Restricciones: Los estudiantes se deben encontrar en la lista de estudiantes_y_profes y estar matriculados en los cursos.

def ver_cursos(xl):  # Pendiente!!/Idea para selec cursos:Pedir un input con el nombre del curso, (ej:'Mate Discreta'), hacer un ciclo para buscarlo en [cursos] y que imprima las notas.
    x = input("Digite su identificación. ")  # Provisional, (unir con login)
    print("\t", "Lista de cursos matriculados. ")
    for t in cursos:
        for w in t[
            'estudiantes mat']:  # Ciclo que recorre la lista de cursos, y los diccionarios dentro de cada curso hasta encontrar si el estudiante esta matriculado en un curso, en ese caso, lo imprime inmediatamente.
            if x in w['id'] and len(x) == 10:
                print("Nombre Curso:", t['nombre'], "\n", "Codigo Curso:", t['codigo'])
                break
    otra_accion_est(xl)


# Funcion que permite matricular a un estudiante dentro de un curso en el cual no este matricualdo previamente.
# Entrada: ID del estudiante.
# Salida: Lista impresa de todos los cursos matriculados y los no matriculados del estudiante con su informacion general.
# Restricciones: Los estudiantes se deben encontrar en la lista de estudiantes_y_profes.

def cursos_matri(xl):
    x = input("Digite su identificación. ")  # Provisional, (unir con login)/Misma idea de arriba...
    print("\t", "Lista de cursos matriculados. ")
    for r in cursos:
        for w in r[
            'estudiantes mat']:  # Ciclo que recorre la lista de cursos, y los diccionarios dentro de cada curso hasta encontrar si el estudiante esta matriculado en un curso, en ese caso, lo imprime inmediatamente.
            if x in w['id'] and len(x) == 10:
                print("Nombre Curso:", r['nombre'], "\n", "Codigo Curso:", r['codigo'])
                break
    print("\t", "Lista de cursos no matriculados")
    for r in cursos:
        for w in r[
            'estudiantes mat']:  # Ciclo que recorre la lista de cursos, y los diccionarios dentro de cada curso hasta encontrar si el estudiante no esta matriculado en un curso, en ese caso, lo imprime inmediatamente.
            if x not in w['id'] and len(x) == 10:
                print("Nombre Curso:", r['nombre'], "\n", "Codigo Curso:", r['codigo'])
                break
    otra_accion_est(xl)


# Funcion que permite desmatricular a un estudiante dentro de un curso en el cual este previamente matriculado.
# Entrada: ID del estudiante, codigo de curso que se desea desmatricular.
# Salida: Estudiante desmatriculado de un curso elegido por el usuario.
# Restricciones: Los estudiantes se deben encontrar en la lista de estudiantes_y_profes y estar matriculados en un curso, el codgio de curso debe corresponder con uno que exista en el sistema.
def desmatri_cursos(xl):
    x = input('Digite su identificación. ')  # Provisional, (unir con login)
    code = input("""Digite el codigo de curso en el cual se desea desmatricular
""")
    for p in cursos:
        if code == p['codigo']:
            for t in estudiantes_y_profes:
                if x == t['id']:
                    for i in p['estudiantes mat']:
                        if x == i['id']:
                            p['estudiantes mat'].remove(i)
                            print("Se ha desmatriculado con exito")
                        else:
                            print("Usted no se encuentra matriculado en el curso")
                            otra_accion_est(xl)
        else:
            print("El curso no se encuentra en el sistema, intente de nuevo")
            otra_accion_est(xl)
    otra_accion_est(xl)


def matri_cursos(xl):
    x = input("Digite su identificación. ")  # Provisional, (unir con login)
    matri = []
    code = input("""Digite el codigo de curso en el cual se desea matricular
""")
    for p in cursos:
        if code == p['codigo']:
            for t in estudiantes_y_profes:
                if x == t['id']:
                    matri.append(t)
                    for i in p['estudiantes mat']:
                        if x != i['id']:
                            p['estudiantes mat'] = p['estudiantes mat'] + matri
                            print("Se ha matriculado con exito")
                        else:
                            print("Usted ya se encuentra matriculado en el curso")
                            otra_accion_est(xl)
                    return
        else:
            print("El curso no se encuentra en el sistema, intente de nuevo")
            otra_accion_est(xl)
    otra_accion_est(xl)


def matricular(xl):
    z = input("""Elija una accion
1.  Matricular cursos
2.  Desmatricular cursos
3.  Ver cursos matriculados y no matriculados
4.  Volver al menu de estudiantes
""")
    if z == "1":
        matri_cursos(xl)
    elif z == "2":
        desmatri_cursos(xl)
    elif z == "3":
        cursos_matri(xl)
    elif z == "4":
        menu_estudiantes(xl)
    else:
        print("Error en los datos, intentalo de nuevo.")
        matricular(xl)


# Menu de estudiantes
def menu_estudiantes(xl):
    print("Bienvenido estudiante", xl)
    print("""---------Menú Estudiantes---------
1.    Ver Cursos
2.    Matricular
3.    Consultas
4.    Salir
""")

    op = (input("""Digite una opción, por favor
"""))
    if op == "1":
        ver_cursos(xl)  # Pendiente!! Faltan las evaluaciones...
    elif op == "2":
        matricular(xl)
    elif op == "3":
        consultas()  # Pendiente!!
    elif op == "4":
        print("Gracias por utilizar este sistema")
        menu_principal()
    else:
        print("Digite una opcion valida, por favor")
        menu_estudiantes(xl)


######################################################################################################################################################
##Función que despliega un menu con las funciones relacionadas con los cursos del profesor.
##Entradas: Una opción que ingresa el usuario.
##Salidas: Una función de acuerdo al deseo del usuario.
##Restricciones: La opción debe ser "1","2","3","4" o "5".
def curso(xl):
    print("""---------Cursos---------
1.    Crear Curso
2.    Modificar Curso
3.    Borrar Curso
4.    Volver al menu de profesores
5.    Salir
""")
    op = (input("""Digite una opción, por favor
"""))
    if op == "1":
        crear_curso(xl)
    elif op == "2":
        modificar_curso(xl)
    elif op == "3":
        borrar_curso(xl)
    elif op == "4":
        menu_profes(xl)
    elif op == "5":
        print("Gracias por utilizar este sistema")
        menu_principal()
    else:
        print("Digite una opcion valida, por favor")
        curso(xl)


# Funcion para repetir acciones dentro de otra funcion(en este caso en cursos)
# Recibe un string por parte del usuario para regresar al menu principal o salir del programa. La restricción es que la opción debe ser "1" o "2".
def otra_accion_cur(xl):
    v = input("""
Desea realizar otra accion?
Si=1
No=2
""")
    if v == "1":
        curso(xl)
    elif v == "2":
        print("Gracias por utilizar este sistema")
        menu_principal()
    else:
        print("Error, digite un valor valido")
        otra_accion_cur(xl)
    otra_accion_cur(xl)


##Funcion para crear cursos mediante la utilización de ciclos con variables "i" y "a", la función input y comandos de listas y diccionarios.
##Entradas: Código de curso, nombre de curso, ID del profesor, cantidad de créditos, todos tipo string que ingresa el usuario.
##Salidas: Un diccionario dentro de la lista de cursos con todos los datos del curso que se ha creado.
##Restricciones: Los valores deben ser de tipo string, además de no estar ya incluídos en la lista de cursos, en el caso del código o no incluídos en la lista estudiantes_y_profes (ID del profesor)
def crear_curso(xl):
    x = input("""Digite el código del curso a crear
""")
    for i in cursos:
        if x in i['codigo']:
            print(
                "Error, el codigo ya se encuentra en el sistema. ")  # Ciclo que verifica si el código del curso no se repite en la lista de cursos para continuar con la función.
            otra_accion_cur(xl)
    y = input("""Digite su identificación
""")
    for a in estudiantes_y_profes:
        if y == a['id']:
            z = input("""Digite el nombre del curso a crear
""")  # Ciclo que valida si el ID del profesor concuerda con el de la lista de estudiantes_y_profes.
            w = input("""Digite la cantidad de creditos del curso
""")
            break
    if y not in a.values():
        print("Error, el id no se encuentra en el sistema")
        otra_accion_cur(xl)
    cursos.append({'codigo': x, 'id': y, 'nombre': z, 'creditos': w, 'estudiantes mat': [], 'tareas': [], 'examenes': [],
         'proyectos': [], 'quiz': [], 'laboratorios': [],
         'otros': []})  # Comando que añade el curso con sus datos en la lista de cursos.
    print("El curso ha sido creado exitosamente")
    otra_accion_cur(xl)


# Funcion de modificar cursos
# Entrada: Codigo de curso, nuevo código, ID, nombre y créditos del curso que se desea modificar.
# Salida: Curso modificado.
# Restricciones: El curso a modificar se debe encontrar en la lista de cursos.
def modificar_curso(xl):
    x = input("""Digite el codigo del curso
""")
    for i in cursos:  # Ciclo con variables "i", la cual recorre la lista cursos.
        if x==i['codigo']:        # Pequeño menú que indica que parte de la información del curso se desea modicficar.
            o = input("""Digite donde desea realizar los cambios
Codigo===============1
ID===================2
Nombre del curso=====3
Cantidad de creditos=4
""")
            if o == "1":
                b = input("""Digite el nuevo codigo del curso
""")
                i['codigo'] = b
            elif o == "2":
                c = input("""Digite la nueva ID
""")
                i['id'] = c
            elif o == "3":  # Cada uno de estos if/elif modifica una parte del curso que se desea cambiar.
                d = input("""Digite el nuevo nombre del curso
""")
                i['nombre'] = d
            elif o == "4":
                e = input("""Digite la cantidad de creditos del nuevo curso
""")
                i['creditos'] = e
            else:
                print("Digite un valor valido")
                modificar_curso(xl)
            print("El curso ha sido modificado exitosamente")
            u = input("""
Desea realizar otra modificacion?
Si=1
No=2
""")
            if u == "1":
                modificar_curso(xl)
            elif u == "2":
                curso(xl)
            else:
                print("Error, regreso a curso.")
                curso(xl)
        else:
            print("El curso no se encuentra en el sistema")
            otra_accion_cur(xl)


# Funcion para borrar cursos
# Entrada: Codigo de curso
# Salida: Curso eliminado de la lista de cursos.
# Restricciones: El curso a borrar se debe encontrar en la lista de cursos y no debe poseer estudiantes matriculados en él.
def borrar_curso(xl):
    x = input("""Digite el codigo del curso
""")
    for i in cursos:  # Ciclo que busca si el curso está en la lista de cursos recorriendo la lista en sí con la variable "i"
        if x in i.values():
            print("El curso esta en el sistema")
            v = input("""
Desea borrar el curso?
Si=1
No=2
""")
            if v == "1":
                for i in cursos:  # Ciclo que valida si el curso no tiene estudiantes matriculador, en ese caso, lo elimina de la lista de cursos.
                        if i['estudiantes mat']==[]:
                            cursos.remove(i)
                            print("El curso ha sido borrado exitosamente")
                        else:
                            print("El curso no puede ser borrado debido a que posee estudiantes matriculados")
                otra_accion_cur(xl)
            elif v == "2":
                curso(xl)
            else:
                print("Error, digite un valor valido")
                borrar_curso(xl)
            borrar_curso(xl)
        else:
            print("El curso no se encuentra en el sistema")
            otra_accion_cur(xl)


##Función que despliega un menu con las funciones específicas para estudiantes de un profesor.
##Entradas: Una opción que ingresa el usuario.
##Salidas: Una función de acuerdo al deseo del usuario.
##Restricciones: La opción debe ser "1","2","3" o "4".
def estudiantes(xl):
    print("""---------Estudiantes---------
1.    Agregar Estudiante
2.    Eliminar Estudiante
3.    Volver al menu de profesores
4.    Salir
""")
    op = (input("""Digite una opción, por favor
"""))
    if op == "1":
        agregar_estudiante(xl)
    elif op == "2":
        eliminar_estudiante(xl)
    elif op == "3":
        menu_profes(xl)
    elif op == "4":
        print("Gracias por utilizar este sistema")
        menu_principal()
    else:
        print("Digite una opcion valida, por favor")
        estudiantes(xl)


# Funcion para repetir acciones dentro de otra funcion(en este caso en estudiantes)
# Recibe un string por parte del usuario para regresar a estudiantes o al menu principal. La restricción es que la opción debe ser "1" o "2".
def otra_accion_es(xl):
    u = input("""
Desea realizar otra accion?
Si=1
No=2
""")
    if u == "1":
        estudiantes(xl)
    elif u == "2":
        print("Gracias por utilizar este sistema")
        menu_principal()
    else:
        print("Error, digite un valor valido")
        otra_accion_es(xl)
    otra_accion_es(xl)


# Funcion para agregar estudiantes
# Entrada: Codigo de curso y carné del estudiante que desea agregar a un curso el profesor.
# Salida: Estudiante agregado a un curso.
# Restricciones: El estudiante por agregar se debe encontrar en la lista de estudiantes_y_profes y no debe estar matriculado en él.
def agregar_estudiante(xl):
    mat = []  # Lista vacía para agregar estudiantes.
    p = input("""Digite el codigo del curso en el cual desea agregar un estudiante
""")
    for i in cursos:  # Ciclo que busca si el curso está en la lista de cursos recorriendo la lista en sí con la variable "i" y "a", respectivamente
        if p in i.values():
            print("El curso esta en el sistema")

            u = input("""
Conoce el numero de carne del estudiante que desea agregar?
Si=1
No=2
""")
            if u == "1":
                x = input("""Digite el numero de carne del estudiante que desea agregar
""")
                for t in estudiantes_y_profes:
                    if x in t.values():  # Ciclo que busca si el estudiantes está en la lista de estudiantes_y_profes y lo agrega al curso.
                        mat.append(t)
                        i['estudiantes mat'] = i['estudiantes mat'] + mat
                        break
                print("El estudiante ha sido agregado exitosamente")
                otra_accion_es(xl)
            elif u == "2":
                print("""Esta es la lista completa de estudiantes sin matricular en el curso,
Busque el nombre del alumno que desea agregar""")
                print("Nombre", "\t", "\t", "\t", "\t", "Carné", "\t", "\t", "\t", "\n")
                for q in estudiantes_y_profes:
                    if len(q['id']) == 10 and q not in i[
                        'estudiantes mat']:  ##Ciclo que imprime los estudiantes en la lista de estudiantes_y_profes que no se encuentren matriculados en el curso.
                        print(q['nombre'], "\t", "\t", "\t", q['id'], "\n")
                x = input("""Digite el numero de carne del estudiante que desea agregar
""")
                for t in estudiantes_y_profes:  # Ciclo que busca si el estudiante está en la lista de estudiantes_y_profes y lo agrega al curso.
                    if x in t.values():
                        mat.append(t)
                        i['estudiantes mat'] = i['estudiantes mat'] + mat

                print("El estudiante ha sido agregado exitosamente")
                otra_accion_es(xl)
            else:
                print("Error, digite un valor valido")
                agregar_estudiante(xl)
        else:
            print("El curso no se encuentra en el sistema, intente de nuevo")
            agregar_estudiante(xl)


# Funcion para eliminar estudiantes
# Entrada: Codigo de curso y carné del estudiante que desea eliminar de un curso.
# Salida: Estudiante borrado de un curso.
# Restricciones: El estudiante por agregar se debe encontrar en la lista de estudiantes_y_profes y debe estar matriculado en el curso.
def eliminar_estudiante(xl):
    x = input("""Digite el codigo de curso en el cual desea eliminar un estudiante
""")
    for i in cursos:  # Ciclo que busca si el curso está en la lista de cursos recorriendo la lista en sí con la variable "i" y "a", respectivamente
        if x in i.values():
            print("El curso esta en el sistema")
            break
        else:
            print("El curso que ingreso no se encuentra en el sistema, intente nuevamente")
            eliminar_estudiante(xl)
    p = input("""Digite el carne del estudiante que desea eliminar
""")
    for r in i['estudiantes mat']:  # Ciclo que busca si el estudiante está en la lista de estudiantes_y_profes y lo elimina del curso.
        if p in r['id']:
            i['estudiantes mat'].remove(r)
    print("El estudiante ha sido eliminado con exito")
    otra_accion_es(xl)


##Función que despliega un menu con las funciones relacionadas con las consultas del profesor.
##Entradas: Una opción que ingresa el usuario.
##Salidas: Una función de acuerdo al deseo del usuario.
##Restricciones: La opción debe ser "1","2","3","4","5" o "6".
def menu_consultas(xl):
    print("""---------Consultas---------
1.    Ver lista de estudiantes
2.    Ver lista de cursos
3.    Consulta Curso
4.    Consulta Estudiante
5.    Regresar al menu de profesores
6.    Salir
""")

    op = (input("""Digite una opción, por favor
"""))
    if op == "1":
        lis_es(xl)
    elif op == "2":
        lis_cur(xl)
    elif op == "3":
        cons_cur(xl)
    elif op == "4":
        cons_est()
    elif op == "5":
        menu_profes(xl)
    elif op == "6":
        print("Gracias por utilizar este sistema")
        menu_principal()
    else:
        print("Digite una opcion valida, por favor")
        menu_consultas(xl)


# Funcion para repetir acciones dentro de otra funcion(en este caso en consultas)
# Recibe un string por parte del usuario para regresar a consultas o al menu principal. La restricción es que la opción debe ser "1" o "2".
def otra_accion_con(xl):
    v = input("""
Desea realizar otra accion?
Si=1
No=2
""")
    if v == "1":
        menu_consultas(xl)
    elif v == "2":
        print("Gracias por utilizar este sistema")
        menu_principal()
    else:
        print("Error, digite un valor valido")
        otra_accion_con(xl)
    otra_accion_con(xl)


# Funcion para imprimir la lista de todos los estudiantes
# Entrada: Tipo de cuenta creada en el registro, (en este caso, "1" de estudiantes).
# Salida: Lista impresa de todos los estudiantes con sus datos personales.
# Restricciones: Los estudiantes se deben encontrar en la lista de estudiantes_y_profes y ser de tipo "1".
def lis_es(xl):
    for q in estudiantes_y_profes:  # Ciclo que busca a todos los estudiantes en el sistema y los imprime.
        if q['tipo'] == "1":
            if q['carrera']=="1":
                print(q['nombre'], "\t", "\t", "\t", q['id'], "\t", "\t", "\t", q['correo'], "\t", "\t", "\t",q['telefono'], "\t", "\t", "\t", "Ingeniería en Computación", "\t", "\t", "\t", "\n")
            elif q['carrera']=="2":
                print(q['nombre'], "\t", "\t", "\t", q['id'], "\t", "\t", "\t", q['correo'], "\t", "\t", "\t",q['telefono'], "\t", "\t", "\t", "Ingeniería en Producción Industrial", "\t", "\t", "\t", "\n")
            elif q['carrera']=="3":
                print(q['nombre'], "\t", "\t", "\t", q['id'], "\t", "\t", "\t", q['correo'], "\t", "\t", "\t",q['telefono'], "\t", "\t", "\t", "Ingeniería en Agronomía", "\t", "\t", "\t", "\n")
            elif q['carrera']=="4":
                print(q['nombre'], "\t", "\t", "\t", q['id'], "\t", "\t", "\t", q['correo'], "\t", "\t", "\t",q['telefono'], "\t", "\t", "\t", "Ingeniería en Electrónica", "\t", "\t", "\t", "\n")
            elif q['carrera']=="5":
                print(q['nombre'], "\t", "\t", "\t", q['id'], "\t", "\t", "\t", q['correo'], "\t", "\t", "\t",q['telefono'], "\t", "\t", "\t", "Gestión del Turismo Rural Sostenible", "\t", "\t", "\t", "\n")
            elif q['carrera']=="6":
                print(q['nombre'], "\t", "\t", "\t", q['id'], "\t", "\t", "\t", q['correo'], "\t", "\t", "\t",q['telefono'], "\t", "\t", "\t", "Administración de Empresas", "\t", "\t", "\t", "\n")
    otra_accion_con(xl)


# Funcion para imprimir la lista de todos los cursos
# Entrada: Cursos creados por defaulto por el programa.
# Salida: Lista impresa de todos los cursos con su información y el profesor que lo imparte.
# Restricciones: Los cursos se deben encontrar en la lista de cursos y los profesores deben estar en la lista de estudiantes_y_profes y ser de tipo "2".
def lis_cur(xl):
    print("\t", "\t", "\t", "Lista de total de cursos", "\n", "Codigo de curso", "\t", "Nombre del curso", "\t", "\t","Id del profesor", "\t", "\t", "Nombre del profesor")
    for i in cursos:
        for a in estudiantes_y_profes:  # Ciclo que busca todos los cursos en el sistema y los imprime, además de buscar e imprimir la info. del profe que los imparte.
            if a['tipo']=="2" and i['id']==a['id']:
                print(i['codigo'], "\t", "\t", "\t", i['nombre'], "\t", "\t", "\t", i['id'], "\t", "\t", "\t",a['nombre'], "\n")
    otra_accion_con(xl)


# Funcion que despliega un menu de consultas especificamente disenado para un solo curso.
# Entradas: Una opción que ingresa el usuario.
# Salidas: Una función de acuerdo al deseo del usuario.
# Restricciones: La opción debe ser "1","2","3","4","5" o "6".
def cons_cur(xl):
    print("""---------Consulta Curso---------
1.    Lista de estudiantes matriculados
2.    Nota promedio de los estudiantes
3.    Promedio de cada rubro de calificacion
4.    Lista estudiantes con desglose de calificaciones
5.    Volver al menu de profesores
6.    Salir
""")

    op = (input("""Digite una opción, por favor
"""))
    if op == "1":
        lis_es_mat(xl)
    elif op == "2":
        not_prom()
    elif op == "3":
        prom_rub()
    elif op == "4":
        lis_compl()
    elif op == "5":
        menu_profes(xl)
    elif op == "6":
        print("Gracias por utilizar este sistema")
        menu_principal()
    else:
        print("Digite una opcion valida, por favor")
        cons_cur(xl)


# Funcion para imprimir la lista de estudiantes de un curso "x".
# Entrada: Código del curso, tipo de cuenta creada en el registro, (en este caso, "1" de estudiantes).
# Salida: Lista impresa de todos los estudiantes matriculados en un curso con sus datos personales.
# Restricciones: Los estudiantes se deben encontrar en la lista de estudiantes_y_profes y estar matriculados en el curso.
def lis_es_mat(xl):
    p = input("""Digite el codigo del curso en el cual desea ver la lista de estudiantes matriculados
""")
    for i in cursos:  # Ciclo que busca si el curso está en el sistema.
        if p in i.values():
            break
        else:
            print("El curso no se encuentra en el sistema, pruebe de nuevo")
            lis_es_mat(xl)
    print("----------------Lista de estudiantes matriculados-------------------------")
    for q in estudiantes_y_profes:
        if len(q['id']) == 10 and q in i['estudiantes mat']:  ##Ciclo que busca todos los estudiantes matriculados en un curso y los imprime.
            print(q['nombre'], "\t", "\t", "\t", q['id'], "\n")
    otra_accion_con(xl)


def not_prom():
    return  # Aqui quedo por hoy, falta esperar a las evaluaciones para terminarlo.


# Menu de profes
# Funcion que despliega el menu principal especificamente disenado para profesores.
# Entradas: Una opción que ingresa el usuario.
# Salidas: Una función de acuerdo al deseo del usuario.
# Restricciones: La opción debe ser "1","2","3","4" o "5"
def menu_profes(xl):
    print("Bienvenido Profesor (a)", xl)
    print("""---------Menú Profesores---------
1.    Cursos
2.    Estudiantes
3.    Evaluaciones
4.    Consultas
5.    Salir
""")

    op = (input("""Digite una opción, por favor
"""))
    if op == "1":
        curso(xl)
    elif op == "2":
        estudiantes(xl)
    elif op == "3":
        menu_evaluaciones(xl)
    elif op == "4":
        menu_consultas(xl)
    elif op == "5":
        print("Gracias por utilizar este sistema")
        menu_principal()
    else:
        print("Digite una opcion valida, por favor")
        menu_profes(xl)




######################################################################################################################################################





##################################################################################################################################################
##
##          esta parte la hice yo
##
##################################################################################################################################################






# logup totalmente listo
def singup():
    # FUNCION: registro de estudiantes en el sistema
    # ENTRADAS: datos del estudiante para poder guardarlos
    # SALIDAS: almacemaniento de los datos del estudiante
    # RESTRICCIONES: debe ser un estudiante nuevo, no podrá crear una cuenta con un carnet o cedula que ya se encuentre registrado
    print("""Digite el tipo de cuenta que va a crear
                                                1. Estudiante
                                                2. Profesor
                                                3. Volver al menú principal""")
    tipo = input("""Digite la opción deseada.
""")
    if tipo == "1":
        carne1 = (input("Digite el número de carnet."))
        for m in estudiantes_y_profes:  # busca que el carnet digitado no se encuentre registrado
            if carne1 == m["id"]:
                print(" _ _ _ _ _ _ _ _ _ ")
                print("""|      Error      |
|- - - - - - - - -|- - - - - - - - - - - - - -|
|   El número de carnet ingresado pertenece   |
|   a otro usuario que ya está registrado,    |
|   inténtalo nuevamente.                     | """)
                print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")
                singup()
            elif carne1.isdigit():
                carne = carne1
            else:
                print("\nEl número de carnet debe de contener únicamente números, inténtalo nuevamente.\n")
                singup()

    elif tipo == "2":
        carne1 = input("Digite el número de cédula.")
        for m in estudiantes_y_profes:  # busca que la cedula digitada no se encuentre registrada
            if carne1 == m["id"]:
                print(" _ _ _ _ _ _ _ _ _ ")
                print("""|      Error      |
|- - - - - - - - -|- - - - - - - - - - - - - -|
|   El número de carnet ingresado pertenece   |
|   a otro usuario que ya está registrado,    |
|   inténtalo nuevamente.                     | """)
                print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|")
                singup()
            elif carne1.isdigit():
                carne = carne1
            else:
                print("\nEl número de cédula debe de contener únicamente números, inténtalo nuevamente.\n")
                singup()
    elif tipo == "3":
        menu_principal()
    else:
        print("Error en los datos, inténtalo nuevamente.")
        singup()
    name = input("Digite su nombre completo.")
    telef = input("Digite su número de teléfono.")
    mail = input("Digite su correo electrónico.")
    contra = input("Digite la contraseña que desea utilizar.")
    if tipo == "1":
        print("""
        1. Ingeniería en Computación
        2. Ingeniería en Producción Industrial
        3. Ingeniería en Agronomía
        4. Electrónica
        5. Gestión del Turismo Rural Sostenible
        6. Administración de Empresas
        """)
        carrera = input("Digite la opción de su carrera.")
        estudiantes_y_profes.append(
            {"nombre": name, "correo": mail, "pass": contra, "id": carne, "tipo": tipo, "carrera": carrera,
             "telefono": telef})  # Guardo la informacion
    elif tipo == "2":
        estudiantes_y_profes.append({"nombre": name, "correo": mail, "pass": contra, "id": carne, "tipo": tipo})
    print("El proceso de registro se realizó correctamente.")
    menu_principal()
    return


# login totalmente listo
def login():
    # FUNCION: Tomar los datos del usuario para enviarlo a su respectivo menu, ya sea estudiante o profesor
    # ENTRADAS: el ususario debe digitar su cedula en caso de profesor o su carnet en caso de estudiante y luego la contraseña
    # SALIDAS:enviarlo al menu que le corresponde
    # RESTRICCIONES: debe digitar el carnet o cedula junto con la contraseña bien
    print(" _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _")
    ide = input("| Digite su identificación.    ")
    passw = input("| Digite su contraseña.        ")
    print("|_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n")
    for i in range(0, len(estudiantes_y_profes)):
        if ide == estudiantes_y_profes[i]["id"] and passw == estudiantes_y_profes[i][
            "pass"]:  # proceso de validacion si existen esos datos y corresponden a un usuario especifico
            if estudiantes_y_profes[i]["tipo"] == "1":  # si el usuario es de tipo 1 es decir estudiantes entonces...
                xl = estudiantes_y_profes[i]["nombre"]  # ...en una variable guardo el nombre y luego...
                return menu_estudiantes(
                    xl)  # lo envio al menu de estudiantes donde recibira la variable con el nombre para mostrarlo
            elif estudiantes_y_profes[i][
                "tipo"] == "2":  # Si el usuario es de tipo 2 es decir profesor entonces lo envio a su respectivo menu
                xl = estudiantes_y_profes[i]["nombre"]
                return menu_profes(xl)
    print(
        " Datos no válidos, inténtalo nuevamente.\n")  # sino estan los datos se le muestra un mensaje y el proceso se repite hasta que ingrese bien los datos
    login()


def nomporeva(hh, resp):
    # FUNCION: guardar evaluaciones
    # ENTRADAS: nombre de la evaluacion, porcentaje a asignar
    # SALIDAS: crear la evaluacion
    # RESTRICCIONES: no debe existir una evaluacion con el mismo nombre, el porcentaje no puede pasarse de 100%, el procentaje debe tener punto en vez de coma
    q={}
    if resp == "1":
        evaluacion = "tareas"
    elif resp == "2":
        evaluacion = "proyectos"
    elif resp == "3":
        evaluacion = "examenes"
    elif resp == "4":
        evaluacion = "quiz"
    elif resp == "5":
        evaluacion = "laboratorios"
    elif resp == "6":
        evaluacion = "otros"
    name_eval = input("Digite el nombre de la evaluación a crear. ")
    for i in cursos:
        if hh == i["codigo"]:
            if name_eval in i[evaluacion]:
                print("Error, la tarea a crear ya existe. ")
                add_evaluations()
            else:
                for m in i:
                    if name_eval in m:  # si la evaluacion a crear ya existe entonces entonces se le pone un mensaje de error
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
                            porcantaje = float(input("Digite el procenteje a asignar  "))

                            q["nombre"]=name_eval
                            q["porcentaje"]=porcantaje
                            c.append(q)

                            break
                        except ValueError:
                            print("Error en los datos, el número decimal debe de usar punto en vez de coma. ")
                            add_evaluations()
                            break


# agregar totalmente listo
def add_evaluations():
    # FUNCION:   egreagar evaluaciones a cada curso
    # ENTRADAS:  el tipo de evaluacion, porcentaje y nombre
    # SALIDAS:   guardar la evaluacion
    # RESTRICCIONES: el porcentaje de tareas no debe sobrepasar el 100%
    tot = 0
    code_course = input("Digite el código del curso. ")
    for i in cursos:
        if code_course == i["codigo"]:  # recorro la lista de cursos en busca del codigo del curso
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
            resp = input("Digite la opción de la evaluación que desea crear. ")
            hh = code_course
            if resp == "1":
                nomporeva(hh, resp)
                i['tareas'] = i['tareas'] + c
                print(cursos)
            elif resp == "2":
                nomporeva(hh, resp)
                i['proyectos'] = i['proyectos'] + c
                print(cursos)
            elif resp == "3":
                nomporeva(hh, resp)
                i['examenes'] = i['examenes'] + c
                print(cursos)
            elif resp == "4":
                nomporeva(hh, resp)
                i['quiz'] = i['quiz'] + c
                print(cursos)
            elif resp == "5":
                nomporeva(hh, resp)
                i['laboratorios'] = i['laaboratorios'] + c
                print(cursos)
            elif resp == "6":
                nomporeva(hh, resp)
                i['otros'] = i['otros'] + c
                print(cursos)
            else:
                print("Digite un valor válido, por favor ")
                add_evaluations()


# en proceso
def edit_evaluations():
    x = ""
    code_course = input("Digite el código del curso. ")
    for i in cursos:
        if code_course == i["codigo"]:
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
            resp = input("Digite la opción de la evaluación que desea eliminar. ")
            if resp == "1":
                posicion = "tareas"
            elif resp == "2":
                posicion = "proyectos"
            elif resp == "3":
                posicion = "examenes"
            elif resp == "4":
                posicion = "quiz"
            elif resp == "5":
                posicion = "laboratorios"
            elif resp == "6":
                posicion = "otros"
            else:
                print("Error, debe digitar una opción válida. ")
                edit_evaluations()
            print("\nEstas son las(os)",posicion,"disponibles. ")
            for a in i[posicion].items():
                print(a)
            op = input("""¿Qué desea modificar?
            1.Nombre de la evaluación
            2.Porcentaje asignado
            3.Menú principal
            """)
            if op == "1":
                    nombre_viejo = input("Digite el nombre de la evaluación a modificar. ")
                    if nombre_viejo==a:
                            new_name = input("Digite el nuevo nombre a asignar")
                            a=new_name
                            print(cursos)
                            break



            elif op == "2":
                    nombre_viejo = input("Digite el nombre de la evaluación a modificar. ")
                    porc = input("Digite el nuevo porcentaje que asiganará. ")
                    if nombre_viejo in i[posicion]:
                        i[nombre_viejo] = porc
            elif op == "3":
                    menu_profes(x)
            else:
                    print("Error, debe digitar alguna de las opciones. ")


# en proceso
def del_evaluations():
    code_course = input("Digite el código del curso. ")
    for i in cursos:
        if code_course == i["codigo"]:
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
            resp = input("Digite la opción de la evaluación que desea eliminar. ")
            if resp == "1":
                posicion = "tareas"
            elif resp == "2":
                posicion = "proyectos"
            elif resp == "3":
                posicion = "examenes"
            elif resp == "4":
                posicion = "quiz"
            elif resp == "5":
                posicion = "laboratorios"
            elif resp == "6":
                posicion = "otros"

            delpala = input("Digite el nombre de la evaluación que desea eliminar. ")
            for d in i[posicion]:
                    if delpala==d['nombre']:
                        print(cursos)
                        i[posicion].remove(d)
                        print("listo")

                    try:

                        # if delpala==d:
                        # xx=d
                        # del i[posicion][d]          #BUSCAR Y ELIMINAR LOS DOS DATOS, YA QUE ESTA ELIMINANDO SOLAMENTE UNO

                        print(cursos)
                        # print(xx)
                        break

                    except:
                        print("listo")
            else:
                print("La palabra que busca eliminar no se encuentró, inténtalo nuevamente. ")
                del_evaluations()

del_evaluations()
# menu de evaluaciones listo
def menu_evaluaciones(xl):
    print("----------------------------------")
    print("-------|   Evaluaciones   |-------")
    print("----------------------------------")
    op = input("""-   1. Agregar evaluaciones      -
-   2. Modificar evaluaciones    -
-   3. Eliminar evaluaciones     -
-   4. Menú de profesores
-    """)
    if op.isdigit():
        if op == "1":
            return add_evaluations()
        elif op == "2":
            return edit_evaluations(xl)
        elif op == "3":
            return del_evaluations()
        elif op == "4":
            return menu_profes(xl)
        else:
            print("\n__________________________________")
            print(">>Debe de digitar datos válidos.<<")
            print("__________________________________\n")
            menu_evaluaciones(xl)
    else:
        print("\n__________________________________")
        print(">>Debe de digitar datos válidos.<<")
        print("__________________________________\n")
        menu_evaluaciones(xl)


# menú principal totalmente listo
def menu_principal():
    # FUNCION: menu principal, aqui el usuario decide que hacer si ingresar al sistema en caso de tener cuenta o registrarse para ingresar
    # ENTRADAS: opcion que desea ejecutar
    # SALIDAS: proceso de ingreso o proceso de registro
    # RESTRICCIONES: la opcion debe ser un numero entero, ya sea 1, 2, o 3
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
    op = (input("""\t\t\t\t\t   | Digite la opción a elegir.    |
                       |       """))
    print("\t\t\t\t\t   |_ _ _ _ _ _ _ _ _ _ _ _ _ _ _ _|\n")
    if op == "1":
        login()
    elif op == "2":
        singup()
    elif op == "3":
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


menu_principal()
