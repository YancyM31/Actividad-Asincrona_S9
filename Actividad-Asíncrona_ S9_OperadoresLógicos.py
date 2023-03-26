#Benvenida del programa
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Bienvenido a este programa")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~ \n")

#Toma de datos al usuario desde el teclado:
print("TOMA DE DATOS DEL USUARIO \n")
nombre= input("Ingrese su Nombre: " )
apellido= input("Ingrese su Apellido: " )
edad= int (input("Ingrese su Edad: " ))
sexo= input("Ingrese su Sexo (Masculino o Femenino) : ").lower()
print("")
print("Los datos del usuario son : ")
print("")
print("Nombre : ", nombre)
print("Apellido : ", apellido)
print("Edad : ", edad, "años") 
print("Sexo : ", sexo)
print("")

#Esta es la estructura Anidada y con operadores lógicos para el sexo Masculino.
if sexo == "masculino".lower():
    if edad == 1 <=2:
     print ("El Niño" , nombre , apellido , "Se encuentras en la etapa de: Bebé") 
    elif edad >= 3 and edad <= 5:
        print("El Niño" , nombre , apellido , "Se encuentra en la etapa de: Infancia")
    elif edad >= 6 and edad  <= 11:
        print("El Niño" , nombre, apellido, "Se encuentra en la etapa de: Niñez")
    elif edad >= 12 and edad <= 18:
        print("El Joven", nombre , apellido,"Se encuentra en la etapa de: Adolecencia")
    elif edad >= 19 and edad <= 26:
        print("El Joven", nombre , apellido, "Se encuentra en la etapa de: Juventud")
    elif edad >= 27 and edad <= 40:
        print("El Caballero", nombre , apellido, "Se encuentra en la etapa de: Adultez Joven")
    elif edad >= 41 and edad <= 55:
        print ("El Señor"), nombre , apellido,"Se encuentra en la etapa de: Adultez"
    elif edad >= 56 and edad <= 65:
        print("El Señor", nombre , apellido,"Se encuentra en la etapa de: Persona Mayor")
    elif edad >= 66 :
        print ("El Abuelo", nombre ,apellido ,"Se encuentra en la etapa de: Vejez ")
    else:
        print("El genero ingresado no está disponible")
else:   
    #Esta es la estructura Anidada y con operadores lógicos para el sexo femenino.
    if sexo =="femenino".lower():
       if edad == 1 <=2:
         print ("La Niña" , nombre ,apellido , "Se encuentras en la etapa de: Bebé") 
       elif edad >= 3 and edad <= 5:
          print("La Niña" , nombre ,apellido , "Se encuentra en la etapa de: Infancia")
       elif edad >= 6 and edad  <= 11:
            print("La Niña " ,nombre,apellido, "Se encuentra en la etapa de: Niñez")
       elif edad >= 12 and edad <= 18:
            print("La Señorita",nombre,apellido,"Se encuentra en la etapa de: Adolecencia")
       elif edad >= 19 and edad <= 26:
            print("La Chica",nombre,apellido, "Se encuentra en la etapa de: Juventud")
       elif edad >= 27 and edad <= 40:
            print("La Dama",nombre ,apellido, "Se encuentra en la etapa de: Adultez Joven")
       elif edad >= 41 and edad <= 55:
            print ("La Señora"),nombre,apellido,"Se encuentra en la etapa de: Adultez"
       elif edad >= 56 and edad <= 65:
            print("La Señora ",nombre,apellido,"Se encuentra en la etapa de: Persona Mayor")
       elif edad >= 66:
            print ("La abuela" ,nombre,apellido,"Se encuentra en la etapa de: Vejez \n")
    else: 
     print("El genero ingresado no esta disponible")   
#En este apartado definiremos si la edad es par o impar.
Par= edad % 2 
if Par == 0:
    print("La edad de " ,nombre ,apellido, "es: Par \n" )
else:
    print("La edad de", nombre ,apellido , "es: Impar \n" ) 
   #Este mensaje indica el fin del programa.
print("~~~~~~~~~~~~~~~~~~")  
print("FIN DEL PROGRAMA")
print("~~~~~~~~~~~~~~~~~~")  