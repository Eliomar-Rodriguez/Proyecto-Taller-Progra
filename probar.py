def logo():
    print("""
        *
        *
        *
  * * * * * * *          *                   *  *
        *            *       *            *          *
        *          *  * * * *  *        *
        *         *                     *
        *          *           *          *          *
        *            *  *   *                *   *
        """)

print("""Digite el tipo de cuenta que va a crear
                                                    1. Estudiante
                                                    2. Profesor""")
tipo=int(input("Digite el tipo de cuenta que va a crear"))
carne=int(input("Digite el número de carnet."))
name=input("Digite su nombre completo.")
mail=int(input("Digite su correo electrónico."))
contra=int(input("Digite la contraseña que desea utilizar."))

usuarios=[]
usuarios.append([carne,name,mail,contra]) #listo
