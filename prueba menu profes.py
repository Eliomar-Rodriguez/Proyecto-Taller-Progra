cursos=[{'codigo':'1403','id':'109870654','nombre':'Mate Discreta','creditos':'4','estudiantes mat':[{"nombre":"Steven Peraza","correo":"stevenperaza@gmail.com","pass":"stevenperaza","id":"2016112209","tipo":"1"}]}]
estudiantes_y_profes=[{"nombre":"Vera Gamboa","Correo":"vgamboa@itcr.ac.cr","pass":"vgamboa","id":"309870123","tipo":"2"},
                      {"nombre":"Diego Rojas","correo":"drojas@itcr.ac.cr","pass":"drojas","id":"109870654","tipo":"2"},
                      {"nombre":"Eladio Cruz","correo":"ecruz@itcr.ac.cr","pass":"ecruz","id":"207650987","tipo":"2"},
                      {"nombre":"Diego Mora","correo":"dmora@itcr.ac.cr","pass":"dmora","id":"701230234","tipo":"2"},
                      {"nombre":"Steven Peraza","correo":"stevenperaza@gmail.com","pass":"stevenperaza","id":"2016112209","tipo":"1"},
                      {"nombre":"Kembly Salazar","correo":"kemsalazar@gmail.com","pass":"kemsalazar","id":"2016402331","tipo":"1"},
                      {"nombre":"Juan Mora","correo":"jmora@hotmail.com","pass":"jmora123","id":"2010198009","tipo":"1"},
                      {"nombre":"Gabriel Martinez","correo":"gmartinez@estudiantec.cr","pass":"gmatinez","id":"2013443216","tipo":"1"},
                      {"nombre":"Juan Rafael Morales","correo":"jrmorales@hotmail.com","pass":"jrmorales96","id":"2014772139","tipo":"1"},
                      {"nombre":"Carlos Morera","correo":"cmorera21@gmail.com","pass":"cmorera","id":"2009123456","tipo":"1"},
                      {"nombre":"Eliomar Rodríguez","correo":"rodriguez.elio.97@gmail.com","pass":"Capitan1","id":"2016108660","tipo":"1"},
                      {"nombre":"Angelo Medina","correo":"amedina@estudiantec.cr","pass":"amedina","id":"2016109990","tipo":"1"},
                      {"nombre":"Juan Primito Rivas","correo":"jprivas@gmail.com","pass":"jprivas","id":"2015012349","tipo":"1"},
                      {"nombre":"Jafeth Salas","correo":"jafsal97@gmail.com","pass":"Jafsal123","id":"2016421763","tipo":"1"},
                      {"nombre":"Carlos Restrepo Marín","correo":"crmarin21","pass":"","id":"121345467","tipo":"1"},
                      {"nombre":"Antonio Rodríguez Arguedas","correo":"antonio16--2012@hotmail.com","pass":"Capitan123","id":"2016108661","tipo":"1"},
                      {"nombre":"Angelo Aguilar","correo":"angelomix@gmail.com","pass":"mixmix1","id":"2011152364","tipo":"1"},
                      {"nombre":"Josue Chaves","correo":"jchaves@gmail.com","pass":"jchaves","id":"2009887512","tipo":"1"},
                      {"nombre":"Joshua Ramirez","correo":"jramirez4223@gmail.com","pass":"lolita123","id":"2014723912","tipo":"1"},
                      {"nombre":"Dere Solorzano","correo":"dsolorsano97@gmail.com","pass":"matediscreta</3","id":"2014334523","tipo":"1"}]#Estudiantes y profesores
#Importante:Falta el telefono de los estudiantes y profes, supongo...


##Función que despliega un menu con las funciones relacionadas con los cursos del profesor.
##Entradas: Una opción que ingresa el usuario.
##Salidas: Una función de acuerdo al deseo del usuario.
##Restricciones: La opción debe ser "1","2","3","4" o "5".
def curso():
    print("""---------Cursos---------
1.    Crear Curso
2.    Modificar Curso
3.    Borrar Curso
4.    Volver al menu de profesores
5.    Salir
""")
    op=(input("""Digite una opción, por favor
"""))
    if op=="1":
        crear_curso()
    elif op=="2":
        modificar_curso()
    elif op=="3":
        borrar_curso()
    elif op=="4":
        menu_profes()
    elif op=="5":
        print("Gracias por utilizar este sistema")
        menu_principal()
    else:
        print("Digite una opcion valida, por favor")
        curso()
        
#Funcion para repetir acciones dentro de otra funcion(en este caso en cursos)
#Recibe un string por parte del usuario para regresar al menu principal o salir del programa. La restricción es que la opción debe ser "1" o "2".
def otra_accion_cur(): 
        v=input("""
Desea realizar otra accion?
Si=1
No=2
""")
        if v=="1":
            curso()
        elif v=="2":
            print("Gracias por utilizar este sistema")
            menu_principal()
        else:
            print("Error, digite un valor valido")
            otra_accion_cur()
        otra_accion_cur()
##Funcion para crear cursos mediante la utilización de ciclos con variables "i" y "a", la función input y comandos de listas y diccionarios.
##Entradas: Código de curso, nombre de curso, ID del profesor, cantidad de créditos, todos tipo string que ingresa el usuario.
##Salidas: Un diccionario dentro de la lista de cursos con todos los datos del curso que se ha creado.
##Restricciones: Los valores deben ser de tipo string, además de no estar ya incluídos en la lista de cursos, en el caso del código o no incluídos en la lista estudiantes_y_profes (ID del profesor)
def crear_curso():
    x=input("""Digite el codigo del curso
""")
    for i in cursos:
            if x in i['codigo']:
                print("Error, el codigo ya se encuentra en el sistema") #Ciclo que verifica si el código del curso no se repite en la lista de cursos para continuar con la función.
                otra_accion_cur()
    y=input("""Digite su ID
""")
    for a in estudiantes_y_profes:
        if y==a['id']:
            z=input("""Digite el nombre del curso
""")                                                                #Ciclo que valida si el ID del profesor concuerda con el de la lista de estudiantes_y_profes.
            w=input("""Digite la cantidad de creditos del curso
""")
            break
    if y not in a.values():
        print("Error, el id no se encuentra en el sistema")
        otra_accion_cur
    cursos.append({'codigo':x,'id':y,'nombre':z,'creditos':w,'estudiantes mat':[],'tareas':[],'examenes':[],'proyectos':[],'quiz':[],'laboratorios':[],'otros':[]}) #Comando que añade el curso con sus datos en la lista de cursos.
    print("El curso ha sido creado exitosamente")
    otra_accion_cur()   

#Funcion de modificar cursos
#Entrada: Codigo de curso, nuevo código, ID, nombre y créditos del curso que se desea modificar.
#Salida: Curso modificado.
#Restricciones: El curso a modificar se debe encontrar en la lista de cursos.
def modificar_curso():
    x=input("""Digite el codigo del curso
""")
    for i in cursos:
        for a in i:         #Ciclo con variables "i", la cual recorre la lista cursos y "a", que recorre los diccionarios de la lista cursos.
            if x in i.values():
                print("El curso esta en el sistema","\n")       #Pequeño menú que indica que parte de la información del curso se desea modicficar.
                o=input("""Digite donde desea realizar los cambios
Codigo===============1
ID===================2
Nombre del curso=====3
Cantidad de creditos=4
""")
                if o=="1":
                    b=input("""Digite el nuevo codigo del curso
""")
                    i['codigo']=b  
                elif o=="2":
                    c=input("""Digite la nueva ID
""")
                    i['id']=c
                elif o=="3":                                        #Cada uno de estos if/elif modifica una parte del curso que se desea cambiar.
                    d=input("""Digite el nuevo nombre del curso
""")
                    i['nombre']=d
                elif o=="4":
                    e=input("""Digite la cantidad de creditos del nuevo curso
""")
                    i['creditos']=e
                else:
                    print("Digite un valor valido")
                    cambio_cursos()
                print("El curso ha sido modificado exitosamente")
                u=input("""
Desea realizar otra modificacion?
Si=1
No=2
""")
                if u=="1":
                    modificar_curso()
                elif u=="2":
                    curso()
                else:
                    print("Error, regreso a curso.")
                    curso()
            else:
                print("El curso no se encuentra en el sistema")
                otra_accion_cur()
                
#Funcion para borrar cursos
#Entrada: Codigo de curso
#Salida: Curso eliminado de la lista de cursos.
#Restricciones: El curso a borrar se debe encontrar en la lista de cursos y no debe poseer estudiantes matriculados en él.
def borrar_curso():
    x=input("""Digite el codigo del curso
""")
    for i in cursos:        #Ciclo que busca si el curso está en la lista de cursos recorriendo la lista en sí con la variable "i" y "a", respectivamente
        for a in i:
            if x in i.values():
                print("El curso esta en el sistema")
                v=input("""
Desea borrar el curso?
Si=1
No=2
""")
                if v=="1":
                    for i in cursos:            #Ciclo que valida si el curso no tiene estudiantes matriculador, en ese caso, lo elimina de la lista de cursos.
                        for a in cursos:                    
                            if a['estudiantes mat']==[]:
                                cursos.remove(i)
                                print("El curso ha sido borrado exitosamente")
                            else:
                                print("El curso no puede ser borrado debido a que posee estudiantes matriculados")
                    otra_accion_cur()
                elif v=="2":
                    curso()
                else:
                    print("Error, digite un valor valido")
                    borrar_curso()
                borrar_curso()
            else:
                print("El curso no se encuentra en el sistema")
                otra_accion_cur()


##Función que despliega un menu con las funciones específicas para estudiantes de un profesor.
##Entradas: Una opción que ingresa el usuario.
##Salidas: Una función de acuerdo al deseo del usuario.
##Restricciones: La opción debe ser "1","2","3" o "4".
def estudiantes():
    print("""---------Estudiantes---------
1.    Agregar Estudiante
2.    Eliminar Estudiante
3.    Volver al menu de profesores
4.    Salir
""")
    op=(input("""Digite una opción, por favor
"""))
    if op=="1":
        agregar_estudiante()
    elif op=="2":
        eliminar_estudiante()
    elif op=="3":
        menu_profes()
    elif op=="4":
        print("Gracias por utilizar este sistema")
        menu_principal()
    else:
        print("Digite una opcion valida, por favor")
        estudiantes()

#Funcion para repetir acciones dentro de otra funcion(en este caso en estudiantes)
#Recibe un string por parte del usuario para regresar a estudiantes o al menu principal. La restricción es que la opción debe ser "1" o "2".
def otra_accion_es():
    u=input("""
Desea realizar otra accion?
Si=1
No=2
""")
    if u=="1":
        estudiantes()
    elif u=="2":
        print("Gracias por utilizar este sistema")
        menu_principal()
    else:
        print("Error, digite un valor valido")
        otra_accion_es()
    otra_accion_es()
    
#Funcion para agregar estudiantes
#Entrada: Codigo de curso y carné del estudiante que desea agregar a un curso el profesor.
#Salida: Estudiante agregado a un curso.
#Restricciones: El estudiante por agregar se debe encontrar en la lista de estudiantes_y_profes y no debe estar matriculado en él.
def agregar_estudiante():
        mat=[] #Lista vacía para agregar estudiantes.
        p=input("""Digite el codigo del curso en el cual desea agregar un estudiante
""")
        for i in cursos:        #Ciclo que busca si el curso está en la lista de cursos recorriendo la lista en sí con la variable "i" y "a", respectivamente
            for a in i:     
                if p in i.values(): 
                    print("El curso esta en el sistema")
                    
                    u=input("""
Conoce el numero de carne del estudiante que desea agregar?
Si=1
No=2
""")
                    if u=="1":
                        x=input("""Digite el numero de carne del estudiante que desea agregar
""")
                        for t in estudiantes_y_profes:            
                                if x in t.values():         #Ciclo que busca si el estudiantes está en la lista de estudiantes_y_profes y lo agrega al curso.
                                    mat.append(t)
                                    i['estudiantes mat']=i['estudiantes mat']+mat
                                    break
                        print("El estudiante ha sido agregado exitosamente")
                        otra_accion_es()
                    elif u=="2":
                        print("""Esta es la lista completa de estudiantes sin matricular en el curso,
Busque el nombre del alumno que desea agregar""")  
                        print("Nombre","\t","\t","\t","\t","Carne","\t","\t","\t","\n")
                        for q in estudiantes_y_profes:
                                if len (q['id'])==10 and q not in i['estudiantes mat']: ##Ciclo que imprime los estudiantes en la lista de estudiantes_y_profes que no se encuentren matriculados en el curso.
                                    print(q['nombre'],"\t","\t","\t",q['id'],"\n")
                        x=input("""Digite el numero de carne del estudiante que desea agregar
""")
                        for t in estudiantes_y_profes:          #Ciclo que busca si el estudiante está en la lista de estudiantes_y_profes y lo agrega al curso.
                                if x in t.values():
                                    mat.append(t)
                                    i['estudiantes mat']=i['estudiantes mat']+mat
                                    
                        print("El estudiante ha sido agregado exitosamente")
                        otra_accion_es()
                    else:
                        print("Error, digite un valor valido")
                        agregar_estudiante()
                else:
                    print("El curso no se encuentra en el sistema, intente de nuevo")
                    agregar_estudiante()
    
                
#Funcion para eliminar estudiantes
#Entrada: Codigo de curso y carné del estudiante que desea eliminar de un curso.
#Salida: Estudiante borrado de un curso.
#Restricciones: El estudiante por agregar se debe encontrar en la lista de estudiantes_y_profes y debe estar matriculado en el curso.
def eliminar_estudiante():
    x=input("""Digite el codigo de curso en el cual desea eliminar un estudiante
""")
    for i in cursos:
        for a in i:                 #Ciclo que busca si el curso está en la lista de cursos recorriendo la lista en sí con la variable "i" y "a", respectivamente
            if x in i.values():
                print("El curso esta en el sistema")
                break
            else:
                print("El curso que ingreso no se encuentra en el sistema, intente nuevamente")
                eliminar_estudiante()
    p=input("""Digite el carne del estudiante que desea eliminar
""")
    for r in i['estudiantes mat']:      #Ciclo que busca si el estudiante está en la lista de estudiantes_y_profes y lo elimina del curso.
        if p in r['id']:
            i['estudiantes mat'].remove(r)
    print("El estudiante ha sido eliminado con exito")
    otra_accion_es()

##Función que despliega un menu con las funciones relacionadas con las consultas del profesor.
##Entradas: Una opción que ingresa el usuario.
##Salidas: Una función de acuerdo al deseo del usuario.
##Restricciones: La opción debe ser "1","2","3","4","5" o "6".
def menu_consultas():
    print("""---------Consultas---------
1.    Ver lista de estudiantes
2.    Ver lista de cursos
3.    Consulta Curso
4.    Consulta Estudiante
5.    Regresar al menu de profesores
6.    Salir
""")

    op=(input("""Digite una opción, por favor
"""))
    if op=="1":
        lis_es()
    elif op=="2":
        lis_cur()
    elif op=="3":
        cons_cur()
    elif op=="4":
        cons_est()
    elif op=="5":
        menu_profes()
    elif op=="6":
        print("Gracias por utilizar este sistema")
        menu_principal()
    else:
        print("Digite una opcion valida, por favor")
        menu_consultas()

#Funcion para repetir acciones dentro de otra funcion(en este caso en consultas)
#Recibe un string por parte del usuario para regresar a consultas o al menu principal. La restricción es que la opción debe ser "1" o "2".
def otra_accion_con(): 
        v=input("""
Desea realizar otra accion?
Si=1
No=2
""")
        if v=="1":
            menu_consultas()
        elif v=="2":
            print("Gracias por utilizar este sistema")
            menu_principal()
        else:
            print("Error, digite un valor valido")
            otra_accion_con()
        otra_accion_con()
#Funcion para imprimir la lista de todos los estudiantes
#Entrada: Tipo de cuenta creada en el registro, (en este caso, "1" de estudiantes).
#Salida: Lista impresa de todos los estudiantes con sus datos personales.
#Restricciones: Los estudiantes se deben encontrar en la lista de estudiantes_y_profes y ser de tipo "1".
def lis_es():
    for q in estudiantes_y_profes: #Ciclo que busca a todos los estudiantes en el sistema y los imprime.
        if a['tipo']=="1":
                print(q['nombre'],"\t","\t","\t",q['id'],"\t","\t","\t",q['correo'],"\t","\t","\t",q['telefono'],"\t","\t","\t",q['carrera'],"\t","\t","\t","\n")
    otra_accion_con()
    
#Funcion para imprimir la lista de todos los cursos
#Entrada: Cursos creados por defaulto por el programa.
#Salida: Lista impresa de todos los cursos con su información y el profesor que lo imparte.
#Restricciones: Los cursos se deben encontrar en la lista de cursos y los profesores deben estar en la lista de estudiantes_y_profes y ser de tipo "2".
def lis_cur():
    print("\t","\t","\t","Lista de total de cursos","\n","Codigo de curso","\t","Nombre del curso","\t","\t","Id del profesor","\t","\t","Nombre del profesor")
    for i in cursos:        
        for a in estudiantes_y_profes:          #Ciclo que busca todos los cursos en el sistema y los imprime, además de buscar e imprimir la info. del profe que los imparte.
            if a['tipo']=="2" and i['id']==a['id']:
                print (i['codigo'],"\t","\t","\t",i['nombre'],"\t","\t","\t",i['id'],"\t","\t","\t",a['nombre'],"\n")
    otra_accion_con()
    
#Funcion que despliega un menu de consultas especificamente disenado para un solo curso.
#Entradas: Una opción que ingresa el usuario.
#Salidas: Una función de acuerdo al deseo del usuario.
#Restricciones: La opción debe ser "1","2","3","4","5" o "6".
def cons_cur():
    print("""---------Consulta Curso---------
1.    Lista de estudiantes matriculados
2.    Nota promedio de los estudiantes
3.    Promedio de cada rubro de calificacion
4.    Lista estudiantes con desglose de calificaciones
5.    Volver al menu de profesores
6.    Salir
""")

    op=(input("""Digite una opción, por favor
"""))
    if op=="1":
        lis_es_mat()
    elif op=="2":
        not_prom()
    elif op=="3":
        prom_rub()
    elif op=="4":
        lis_compl()
    elif op=="5":
        menu_profes()
    elif op=="6":
        print("Gracias por utilizar este sistema")
        menu_principal()
    else:
        print("Digite una opcion valida, por favor")
        cons_cur()
#Funcion para imprimir la lista de estudiantes de un curso "x".
#Entrada: Código del curso, tipo de cuenta creada en el registro, (en este caso, "1" de estudiantes).
#Salida: Lista impresa de todos los estudiantes matriculados en un curso con sus datos personales.
#Restricciones: Los estudiantes se deben encontrar en la lista de estudiantes_y_profes y estar matriculados en el curso.
def lis_es_mat():
    p=input("""Digite el codigo del curso en el cual desea ver la lista de estudiantes matriculados
""")
    for i in cursos:            #Ciclo que busca si el curso está en el sistema.
        for a in i:
            if p in i.values():
                print("El curso esta en el sistema")
                break
    for q in estudiantes_y_profes:
        if len (q['id'])==10 and q in i['estudiantes mat']: ##Ciclo que busca todos los estudiantes matriculados en un curso y los imprime.
            print(q['nombre'],"\t","\t","\t",q['id'],"\n")
    otra_accion_con()
def not_prom():
    return#Aqui quedo por hoy, falta esperar a las evaluaciones para terminarlo.

#Menu de profes
#Funcion que despliega el menu principal especificamente disenado para profesores.
#Entradas: Una opción que ingresa el usuario.
#Salidas: Una función de acuerdo al deseo del usuario.
#Restricciones: La opción debe ser "1","2","3","4" o "5"
def menu_profes():
##    print("Bienvenido Profesor",x) Nombre del profe, falta conectarlo con login.
    print("""---------Menú Profesores---------
1.    Cursos
2.    Estudiantes
3.    Evaluaciones
4.    Consultas
5.    Salir
""")

    op=(input("""Digite una opción, por favor
"""))
    if op=="1":
        curso()
    elif op=="2":
        estudiantes()
    elif op=="3":
        evaluaciones()
    elif op=="4":
        menu_consultas()
    elif op=="5":
        print("Gracias por utilizar este sistema")
        menu_principal()
    else:
        print("Digite una opcion valida, por favor")
        menu_profes()
menu_profes()
