#Bienvenida al usuario
print("----------Universidad de Oriente----------\n")
print("Bienvenidos a nuestros nuevos aspirantes 2023-2026")
print("Unica disponibilidad: Ing.Sistemas Computacionales")
print("Porfavor ingrese los datos que se le pidan \n")

#Le pedimos al usuario que ingrese los datos solicitados
nombre = input("Ingresa tu nombre completo: ")
edad = input("Ingresa tu edad: ")
carrera = input("Ingresa tu carrera deseada: ")

#Guardamos en un diccionario toda la informacion que nos de el usuario
aspirante = {
    "nombre" : nombre,

    "edad" : edad,

    "carrera" : carrera,

    "seleccionado": False
}
#Le pedimos al usuario que ingrese sus calificaciones y sacamos su promedio final
print("\nIngresa tu boleta final: ")

cal_1 = float (input("Calificación uno: "))
cal_2 = float (input("Calificación dos: "))
cal_3 = float (input("Calificación tres: "))
cal_4 = float (input("Calificación cuatro: "))
cal_5  =float (input("Calificación cinco: "))


list = [cal_1, cal_2, cal_3, cal_4, cal_5 ]


promedio = sum(list)/len(list)
print("\nSu promedio final ah sido de ", promedio)

if promedio <7: 
    print("\nUsted no ah sido seleccionado")
else:
    print("\nUsted ah sido admitido para presentar nuestro examen de admisión\n") 
    
    
#Se le aplicara al usuario un cuestionario de 3 preguntas, si acierta dos oh mas sera aceptdado, de lo contrareo terminara el programa
    print("\nA continuación se le aplicara un examen de 3 preguntas")
    print("Porfavor ingrese el numero que crea correcto")

    print("\n¿que es python?\n")
    respuesta_1= int(input('(1- es un tipo de serpiente) (2- es un compilador de codigo) (3- es un lenguaje de programacion): '))
    print("¿Quien fue el creador de python\n")
    respuesta_2 = int(input("(1- Mark Zukerberg) (2- Guido van Rossum) (3- Dennis Ritchie): "))
    print("¿Cúal de estos no es un lenguaje de programación?\n")
    respuesta_3 = int(input("(1-Facebook) (2-python) (3-Java): "))

#En esta parte se analiza la respuesta del usuario, dependiendo si es correcta o incorrecta se le ira agregando el puntuaje a dos variables
    correcta = 0
    incorrecta = 0

    if respuesta_1 == 3:
        correcta += 1
    else:
        incorrecta +=1

    if respuesta_2 == 2:
        correcta += 1
    else:
        incorrecta +=1

    if respuesta_3 == 1:
        correcta += 1
    else:
        incorrecta +=1


    if incorrecta >=2: 
        print("\nUsted ah reprobado el examen de admisión")

    else: 
        
        print('Este es su puntaje: ', correcta)
        print(f"\nFelicidades, usted ah sido aceptado en la carrera de {carrera} . BIENVENIDO!!\n")
        aspirante["seleccionado"] = True
        
        

print(aspirante)





    

