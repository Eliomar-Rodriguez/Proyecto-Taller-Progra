def login():
    usuario=input("Digite el usuario")
    password=input("Digite la contraseña")
    user=[[2016108660,"Eliomar","Rodriguez","Funcionario","gato"],[2016108661,"Steven","Peraza","Estudiante"]]
    i=0
    j=0
    while True:
        while i!=0:
            while j!=0:
                if usuario==user[i][0] and password==user[i][4]:
                    print(user[i][0])
        i+=1
        j=0
login()