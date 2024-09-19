text1 = "Fundamentos con "
text3 = "Python"
result = text1 + text3
print(result)


name = "Andres"
lastName = 'Correa'
fullname = name + " " + lastName
print(fullname)

#Format string

price = 5000
text3 = f'The price is {price:.4f} dollars'
print(text3)


#Math operation

text4 = f'la multiplicacion es {80 * 25} '
print(text4)

#Strin capitalize

text5 = 'python es un lenguaje de alto nivel de programacion '
result1 = text5.capitalize()
print(result1)

#String casefold()

title = 'Cien Años de Soledad'

titleConvert = title.casefold()
print(titleConvert)

#String center ()

fruit = ' Banana '
textCenter = fruit.center(20, ':')
print(textCenter)

#String count()

title1 = 'I love apples, apple are you my favorite fruit'
result2 = title1.count('apples')
print(result2)

#String endswith
text6 = 'Curso, fundamentos con python'
result3 = text6.endswith('.')
print(result3)


#String expandtabs

letter = "A\tN\tD\tR\tE\tS"
letterSpaces = letter.expandtabs(2)
print(letterSpaces)

#String find

text7 = 'Hola, bienvenidos a colombia.'
resul4 = text7.find("bienvenidos")
print(resul4)

#Funciom tittle

text8 = "Welcome to my word"
result5 = text8.title()
print(result5)

#Funcion isalnum

alphanumeric = "Python312"
result6 = alphanumeric.isalnum()
print(result6)

#Funcion isalpha
letters = "aeiou "

result7 = letters.isalpha()
print(result7)