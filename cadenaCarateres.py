#1. Teniendo en cuenta las siguientes variables que describen su edad, nombre y comida favorita, genera
#una cadena para presentarse:
name = "Luis"
age = 27
favouriteFood = "Pasta con salsa Boloñesa"
cadena = f"Hola! Mi {name} es Luis. Yo tengo {age} años, y mi comida favorita es {favouriteFood}"
print (cadena)
#2. Crea un código que solicite al usuario su nombre completo. Luego deberá contar el número de letras
#de su nombre, ignorando los espacios. Finalmente, debe saludar al usuario e informarle la longitud de
#su nombre.
fullName = "Luis Alfonso Vejarano"
longitud = len (fullName)
adicion = f"Hola, {fullName}! Tu nombre tienen {longitud} letras, excluyendo los espacios."
print (adicion)
#3. El analista de datos de una prestigiosa empresa láctea de la ciudad de Popayán, calculó las cifras de
#ventas del último trimestre: el porcentaje de aumento de las ventas y crecimiento de ingresos. Genere
#una cadena que le permita mostrar los porcentajes.
increaseSalesPercent = 12.93720081
revenueGrowthPercent = 18.33206078
porcentaje = f"Las ventas de la empresa láctea aumentaron un {increaseSalesPercent: .2f}% y los ingresos crecieron un {revenueGrowthPercent: .2f}%."
print (porcentaje)
#4. Se proporciona un mensaje secreto codificado en una cadena, para decodificar el mensaje: "Omita
#los primeros tres caracteres y luego omita todos los demás caracteres".
secretMessage = "aS!Ir waQm VL!eDafrcnXin=gS .P,yytahgoln.!"
decodificacion = secretMessage[3:4]
deco2 = secretMessage[7:8]
deco3 = secretMessage[9:10]
deco4 = secretMessage[12:13]
deco5 = secretMessage[14:15]
deco6 = secretMessage[16:17]
deco7 = secretMessage[18:19]
deco8 = secretMessage[20:21]
deco9 = secretMessage[22:23]
deco10 = secretMessage[23:24]
deco11 = secretMessage[25:26]
deco12 = secretMessage[29:30]
deco13 = secretMessage[32:33]
deco14 = secretMessage[33:34]
deco15 = secretMessage[35:36]
deco16 = secretMessage[37:38]
deco17 = secretMessage[39:40]
deco18 = secretMessage[41:42]
print (decodificacion, deco2+deco3, deco4+deco5+deco6+deco7+deco8+deco9+deco10+deco11, deco12+deco13+deco14+deco15+deco16+deco17+deco18)
#5. Se proporciona una frase y luego se debe mostrar el número de palabras en esa frase.
text = "El nombre ""Python"" viene dado por la afición de Van Rossum al grupo Monty Python."
resultado = len(text)
print (resultado)
#OTRA OPCIÓN
text = "El nombre 'Python' viene dado por la afición de Van Rossum al grupo Monty Python."
conteoPalabras = len(text.split())
print(f"El número de palabras en la frase es: {conteoPalabras}")
#6. Escriba un programa que tome una cadena como entrada y reemplace todas las apariciones de la letra
#"a" con la letra "e".
word = '"Camila"'
print (word.replace('a','e'))
#7. Dada la siguiente frase, escriba un programa que invierta el orden de las palabras en esa frase.
sentence = "La' historia del lenguaje de programación 'Python"
frase=sentence.split()
fraseInvertida = frase[::-1]
fraseInvertida=' '.join(fraseInvertida)
print(fraseInvertida)