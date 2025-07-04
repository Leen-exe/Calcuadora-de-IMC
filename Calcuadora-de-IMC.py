# MODO 1:
print("""¡Hola muy buenas!, en esté momento se te hará un encuesta 
para la recaudación de tus datos y la calculación de tu I.M.C. 
Podrias decirme""")

nom = (input("¿Cuál es tu nombre? "))
apeP = input("¿Cuál es tu apellido paterno? ")
apeM = input("¿Cuál es tu apellido materno? ")
edad = int(input("¿Cuál es tu edad? "))
peso = int(input("¿Cuál es tu peso en kilogramos? "))
estat = float(input("¿Cuál es tu estatura en metros? ")) 
imc = peso / estat ** 2 


print("tu nombres es: " + nom, apeP, apeM)
print("Tu peso es: " + str(peso),  "Kilos")
print("Tu estatura es: " + str(estat),  "Metros")
print("tienes: " + str(edad),  "años")
print("Tu I.M.C es: " + str(round(imc,2)))

######################################################################################################################
# MODO 2:

# print("""¡Hola muy buenas!, en esté momento se te hará un encuesta 
# para la recaudación de tus datos y la calculación de tu I.M.C. 
# Podrias decirme""")

# nom = (input("¿Cuál es tu nombre? "))
# apeP = (input("¿Cuál es tu apellido paterno? "))
# apeM = (input("¿Cuál es tu apellido materno? "))
# edad = int(input("¿Cuál es tu edad? "))
# peso = int(input("¿Cuál es tu peso en kilogramos? "))
# estat = float(input("¿Cuál es tu estatura en metros? ")) 
# imc = peso / estat ** 2 

# print(f"""Tu nombre es: {nom} {apeP} {apeM} \n
# Tienes: {edad} años \n
# Pesas: {peso} kilos \n
# Mides: {estat} metros \n
# Tu Indise de Masa Corporal es de: {imc:.2f}""")