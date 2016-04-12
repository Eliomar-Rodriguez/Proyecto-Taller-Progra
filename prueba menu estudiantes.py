cursos=[{'codigo':'1403','id':'116790325','nombre':'Mate Discreta','creditos':'4','estudiantes mat':[{"nombre":"Dere Solorzano","correo":"dsolorsano97@gmail.com","pass":"matediscreta</3","id":"2014334523","tipo":"1"}]},{'codigo':'1407','id':'116790325','nombre':'Mate General','creditos':'4','estudiantes mat':[{"nombre":"Steven Peraza","correo":"stevenperaza@gmail.com","pass":"stevenperaza","id":"2016112209","tipo":"1"}]}]
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
                      {"nombre":"Dere Solorzano","correo":"dsolorsano97@gmail.com","pass":"matediscreta</3","id":"2014334523","tipo":"1"}]



#Funcion que repite acciones dentro de una funcion, en este caso menu_estudiantes.
#Recibe un string por parte del usuario para regresar al menu principal o salir del programa. La restricción es que la opción debe ser "1" o "2".
def otra_accion_est(): 
        v=input("""
Desea realizar otra accion?
Si=1
No=2
""")
        if v=="1":
            menu_estudiantes()
        elif v=="2":
            print("Gracias por utilizar este sistema")
            menu_principal()
        else:
            print("Error, digite un valor valido")
            otra_accion_est()
        otra_accion_est()
        
#Funcion que imprime todos los cursos en los que se encuentra matriculado el estudiante.
#Entrada: ID del estudiante.
#Salida: Lista impresa de todos los cursos matriculados del estudiante con su informacion general.
#Restricciones: Los estudiantes se deben encontrar en la lista de estudiantes_y_profes y estar matriculados en los cursos.
def ver_cursos(): #Pendiente!!/Idea para selec cursos:Pedir un input con el nombre del curso, (ej:'Mate Discreta'), hacer un ciclo para buscarlo en [cursos] y que imprima las notas.
        x=input("asd")#Provisional, (unir con login)
        print ("\t","Lista de cursos matriculados")
        for t in cursos:
                for w in t['estudiantes mat']:                          #Ciclo que recorre la lista de cursos, y los diccionarios dentro de cada curso hasta encontrar si el estudiante esta matriculado en un curso, en ese caso, lo imprime inmediatamente. 
                        if x in w['id']  and len (x)==10:
                                print ("Nombre Curso:",t['nombre'],"\n","Codigo Curso:",t['codigo'])
                                break
        otra_accion_est()

#Funcion que permite matricular a un estudiante dentro de un curso en el cual no este matricualdo previamente.
#Entrada: ID del estudiante.
#Salida: Lista impresa de todos los cursos matriculados y los no matriculados del estudiante con su informacion general.
#Restricciones: Los estudiantes se deben encontrar en la lista de estudiantes_y_profes.

def cursos_matri():
        x=input("asd")#Provisional, (unir con login)/Misma idea de arriba...
        print("\t","Lista de cursos matriculados")
        for r in cursos:
                for w in r['estudiantes mat']:                                          #Ciclo que recorre la lista de cursos, y los diccionarios dentro de cada curso hasta encontrar si el estudiante esta matriculado en un curso, en ese caso, lo imprime inmediatamente.
                        if x in w['id'] and len (x)==10:
                                print ("Nombre Curso:",r['nombre'],"\n","Codigo Curso:",r['codigo'])
                                break
        print("\t","Lista de cursos no matriculados")
        for r in cursos:
                for w in r['estudiantes mat']:                                          #Ciclo que recorre la lista de cursos, y los diccionarios dentro de cada curso hasta encontrar si el estudiante no esta matriculado en un curso, en ese caso, lo imprime inmediatamente.
                        if x not in w['id'] and len (x)==10:
                                print ("Nombre Curso:",r['nombre'],"\n","Codigo Curso:",r['codigo'])
                                break
        otra_accion_est()

#Funcion que permite desmatricular a un estudiante dentro de un curso en el cual este previamente matriculado.
#Entrada: ID del estudiante, codigo de curso que se desea desmatricular.
#Salida: Estudiante desmatriculado de un curso elegido por el usuario.
#Restricciones: Los estudiantes se deben encontrar en la lista de estudiantes_y_profes y estar matriculados en un curso, el codgio de curso debe corresponder con uno que exista en el sistema.
def desmatri_cursos():
        x=input('id')#Provisional, (unir con login)
        code=input("""Digite el codigo de curso en el cual se desea desmatricular
""")
        for p in cursos:
                if code==p['codigo']:
                        for t in estudiantes_y_profes:
                                    if x==t['id']:    
                                            for i in p['estudiantes mat']:
                                                    if x==i['id']:
                                                        p['estudiantes mat'].remove(i)
                                                        print ("Se ha desmatriculado con exito")
                                                    else:
                                                        print("Usted no se encuentra matriculado en el curso")
                                                        otra_accion_est()
                else:
                        print("El curso no se encuentra en el sistema, intente de nuevo"]
                        otra_accion_est()
        otra_accion_est()

def matri_cursos():
        x=input("id")#Provisional, (unir con login)
        matri=[]
        code=input("""Digite el codigo de curso en el cual se desea matricular
""")
        for p in cursos:
                if code==p['codigo']:
                        for t in estudiantes_y_profes:
                                    if x==t['id']:    
                                            matri.append(t)
                                            for i in p['estudiantes mat']:
                                                    if x!=i['id']:
                                                        p['estudiantes mat']=p['estudiantes mat']+matri
                                                        print ("Se ha matriculado con exito")
                                                    else:
                                                        print("Usted ya se encuentra matriculado en el curso")
                                                        otra_accion_est()
                                            return
                else:
                        print("El curso no se encuentra en el sistema, intente de nuevo"]
                        otra_accion_est()  
        otra_accion_est()


def matricular():
        z=input("""Elija una accion
1.  Matricular cursos
2.  Desmatricular cursos
3.  Ver cursos matriculados y no matriculados 
4.  Volver al menu de estudiantes
""")
        if z=="1":
                matri_cursos()
        elif z=="2":
                desmatri_cursos()
        elif z=="3":
                cursos_matri()
        elif z=="4":
                menu_estudiantes()
        else:
                print("Error en los datos, intentalo de nuevo.")
                matricular()



        
#Menu de estudiantes
def menu_estudiantes():
##    print("Bienvenido Estudiante",x) Nombre del chivo, falta conectarlo con login.
    print("""---------Menú Estudiantes---------
1.    Ver Cursos
2.    Matricular
3.    Consultas
4.    Salir
""")

    op=(input("""Digite una opción, por favor
"""))
    if op=="1":
        ver_cursos()#Pendiente!! Faltan las evaluaciones...
    elif op=="2":
        matricular()
    elif op=="3":
        consultas()#Pendiente!!
    elif op=="4":
        print("Gracias por utilizar este sistema")
        menu_principal()
    else:
        print("Digite una opcion valida, por favor")
        menu_estudiantes()
menu_estudiantes()
