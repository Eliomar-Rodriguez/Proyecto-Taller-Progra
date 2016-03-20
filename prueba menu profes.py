cursos=[{'codigo':'1403','id':'116790325','nombre':'Mate Discreta','creditos':'4'},]
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
                      {"nombre":"Carlos Restrepo Marín","correo":"crmarin21","pass":"","id":"","tipo":"1"},
                      {"nombre":"Antonio Rodríguez Arguedas","correo":"antonio16--2012@hotmail.com","pass":"Capitan123","id":"2016108661","tipo":"1"},
                      {"nombre":"Angelo Aguilar","correo":"angelomix@gmail.com","pass":"mixmix1","id":"2011152364","tipo":"1"},
                      {"nombre":"Josue Chaves","correo":"jchaves@gmail.com","pass":"jchaves","id":"2009887512","tipo":"1"},
                      {"nombre":"Joshua Ramirez","correo":"jramirez4223@gmail.com","pass":"lolita123","id":"2014723912","tipo":"1"},
                      {"nombre":"Dere Solorzano","correo":"dsolorsano97@gmail.com","pass":"matediscreta</3","id":"2014334523","tipo":"1"}]#Estudiantes y profesores



##Menu de cursos (profes)
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
        quit()
    else:
        print("Digite una opcion valida, por favor")
        curso()
##Funcion para crear cursos
def crear_curso():
    x=input("""Digite el codigo del curso
""")
    y=input("""Digite su ID
""")
    z=input("""Digite el nombre del curso
""")
    w=input("""Digite la cantidad de creditos del curso
""")
    cursos.append({'codigo':x,'id':y,'nombre':z,'creditos':w})
    print("El curso ha sido creado exitosamente")
    def otra_accion(): #Funcion para repetir acciones dentro de otra funcion
        v=input("""
Desea realizar otra accion?
Si=1
No=2
""")
        if v=="1":
            curso()
        elif v=="2":
            print("Gracias por utilizar este sistema")
            quit()
        else:
            print("Error, digite un valor valido")
            otra_accion()
    otra_accion()   

#Funcion de modificar cursos
def modificar_curso():
    x=input("""Digite el codigo del curso
""")
    for i in cursos:
        for a in i:
            if x in i.values():
                print("El curso esta en el sistema")
                def cambio_cursos(): #Funcion para realizar cambios en los cursos.
                    v=input("""
Desea realizar cambios en el curso?
Si=1
No=2
""")
                    if v=="1":
                        b=input("""Digite el nuevo codigo del curso
""")
                        i['codigo']=b  
                        c=input("""Digite su ID
""")
                        i['id']=c
                        d=input("""Digite el nuevo nombre del curso
""")
                        i['nombre']=c
                        e=input("""Digite la cantidad de creditos del nuevo curso
""")
                        i['creditos']=e
                        print("El curso ha sido modificado exitosamente")
                        def otra_accion():
                            u=input("""
Desea realizar otra accion?
Si=1
No=2
""")
                            if u=="1":
                                curso()
                            elif u=="2":
                                print("Gracias por utilizar este sistema")
                                quit()
                            else:
                                print("Error, digite un valor valido")
                                otra_accion()
                        otra_accion()
                    elif v=="2":
                        curso()
                    else:
                        print("Error, digite un valor valido")
                        cambio_cursos()
                cambio_cursos()
            else:
                print("El curso no se encuentra en el sistema")
                def otra_accion():
                            u=input("""
Desea realizar otra accion?
Si=1
No=2
""")
                            if u=="1":
                                curso()
                            elif u=="2":
                                print("Gracias por utilizar este sistema")
                                quit()
                            else:
                                print("Error, digite un valor valido")
                                otra_accion()
                otra_accion()

def borrar_curso():#PENDIENTE
    x=input("""Digite el codigo del curso
""")
    for i in cursos:
        for a in i:
            if x in i.values():
                print("El curso esta en el sistema")
                def borr_cursos(): #Funcion para borrar en los cursos.
                    v=input("""
Desea borrar el curso?
Si=1
No=2
""")
                    if v=="1":
                         #PENDIENTE
                        print("El curso ha sido borrado exitosamente")
                        def otra_accion():
                            u=input("""
Desea realizar otra accion?
Si=1
No=2
""")
                            if u=="1":
                                curso()
                            elif u=="2":
                                print("Gracias por utilizar este sistema")
                                quit()
                            else:
                                print("Error, digite un valor valido")
                                otra_accion()
                        otra_accion()
                    elif v=="2":
                        curso()
                    else:
                        print("Error, digite un valor valido")
                        borr_cursos()
                borr_cursos()
            else:
                print("El curso no se encuentra en el sistema")
                def otra_accion():
                            u=input("""
Desea realizar otra accion?
Si=1
No=2
""")
                            if u=="1":
                                curso()
                            elif u=="2":
                                print("Gracias por utilizar este sistema")
                                quit()
                            else:
                                print("Error, digite un valor valido")
                                otra_accion()
                otra_accion()
#Menu estudiantes (profes)
def estudiantes():
    print("""---------Cursos---------
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
        quit()
    else:
        print("Digite una opcion valida, por favor")
        curso()

def agregar_estudiante():
    


#Menu de profes

def menu_profes():
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
        consultas()
    elif op=="5":
        print("Gracias por utilizar este sistema")
        quit()
    else:
        print("Digite una opcion valida, por favor")
        menu_profes()
menu_profes()
