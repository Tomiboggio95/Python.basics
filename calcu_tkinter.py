from tkinter import *

ventana = Tk()
ventana.title("Calculadora")

i = 0 #Para que cada click del boton no empiece en el índice 0

#Entrada
e_texto = Entry(ventana, font= ('ComicSans 20'))
e_texto.grid (row = 0, column = 0, columnspan = 4, padx = 50, pady = 5) #padx espacio de 50 en eje x. #pady = espacio de 5 en el eje y

#funciones
def click_button (valor):
    global i
    e_texto.insert(i, valor)
    i += 1

def borrar ():
    e_texto.delete (0, END)
    i = 0

def hace_operacion ():
    ecuacion = e_texto.get ()
    resultado = eval(ecuacion)
    e_texto.delete (0, END)
    e_texto. insert (0, resultado)
    i = 0


 #i = 0 para volver a 0
#fx eval resuelve operaciones en string y arroja el rdo

#botones
#boton = Button (ventana, text = '', widht = 5, height = 2)

boton1 = Button (ventana, text = '1', width = 5, height = 2, command = lambda: click_button(1))
boton2 = Button (ventana, text = '2', width = 5, height = 2,  command = lambda: click_button(2))
boton3 = Button (ventana, text = '3', width = 5, height = 2,  command = lambda: click_button(3))
boton4 = Button (ventana, text = '4', width = 5, height = 2,  command = lambda: click_button(4))
boton5 = Button (ventana, text = '5', width = 5, height = 2,  command = lambda: click_button(5))
boton6 = Button (ventana, text = '6', width = 5, height = 2,  command = lambda: click_button(6))
boton7 = Button (ventana, text = '7', width = 5, height = 2,  command = lambda: click_button(7))
boton8 = Button (ventana, text = '8', width = 5, height = 2, command = lambda: click_button(8))
boton9 = Button (ventana, text = '9', width = 5, height = 2, command = lambda: click_button(9))
boton0 = Button (ventana, text = '0', width = 20, height = 2, command = lambda: click_button(0))

#lambda: click_button introduce ese valor en el argumento de la función
boton_borrar = Button (ventana, text = '⌫', width = 5, height = 2,  command = lambda: borrar())
boton_parentesis1 = Button (ventana, text = '(', width = 5, height = 2,  command = lambda: click_button('('))
boton_parentesis2 = Button (ventana, text = ')', width = 5, height = 2, command = lambda: click_button(')'))
boton_punto = Button (ventana, text = '.', width = 5, height = 2, command = lambda: click_button('.'))

boton_division = Button (ventana, text = '÷', width = 5, height = 2, command = lambda: click_button('/'))
boton_multipl = Button (ventana, text = '×', width = 5, height = 2,  command = lambda: click_button('*'))
boton_suma = Button (ventana, text = '+', width = 5, height = 2,  command = lambda: click_button('+'))
boton_resta = Button (ventana, text = '-', width = 5, height = 2, command = lambda: click_button('-'))
boton_igual = Button (ventana, text = '=', width = 5, height = 2,  command = lambda: hace_operacion ())

#agregrar botones en pantalla
#boton.grid (row = , column = , padx = 5 , pady = 5 )
boton_borrar.grid (row = 1 , column = 0 , padx = 5 , pady = 5 )
boton_parentesis1.grid (row = 1 , column = 1 , padx = 5 , pady = 5 )
boton_parentesis2.grid (row = 1 , column = 2 , padx = 5 , pady = 5 )
boton_division.grid (row = 1 , column = 3 , padx = 5 , pady = 5 )

boton7.grid (row = 2 , column = 0, padx = 5 , pady = 5 )
boton8.grid (row = 2, column = 1, padx = 5 , pady = 5 )
boton9.grid (row = 2 , column = 2, padx = 5 , pady = 5 )
boton_multipl.grid (row = 2, column = 3 , padx = 5 , pady = 5 )

boton4.grid (row = 3 , column = 0, padx = 5 , pady = 5 )
boton5.grid (row = 3, column = 1, padx = 5 , pady = 5 )
boton6.grid (row = 3, column = 2, padx = 5 , pady = 5 )
boton_suma.grid (row = 3, column = 3, padx = 5 , pady = 5 )

boton1.grid (row = 4, column = 0, padx = 5 , pady = 5 )
boton2.grid (row = 4, column = 1, padx = 5 , pady = 5 )
boton3.grid (row = 4, column = 2, padx = 5 , pady = 5 )
boton_resta.grid (row = 4, column = 3, padx = 5 , pady = 5 )

boton0.grid (row = 5, column = 0, columnspan = 2, padx = 5 , pady = 5 )
boton_igual.grid (row = 5, column = 3, padx = 5 , pady = 5 )
boton_punto.grid (row = 5, column = 2, padx = 5 , pady = 5 )


#boton.grid (row = , column = , padx = 5 , pady = 5 )

ventana.mainloop()
