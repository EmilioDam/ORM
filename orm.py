import tkinter as tk
import random
import math
import json

personas = []
numeropersonas = 20

class Persona:
    def __init__(self):
        self.posx = random.randint(0, 1024)
        self.posy = random.randint(0, 1024)
        self.radio = 30
        self.direccion = random.randint(0, 360)
        self.color = "blue"
        self.entidad = ""

    def dibuja(self):
        self.entidad = lienzo.create_oval(
            self.posx - self.radio / 2,
            self.posy - self.radio / 2,
            self.posx + self.radio / 2,
            self.posy + self.radio / 2,
            fill=self.color)

    def mueve(self):
        lienzo.move(
            self.entidad,
            math.cos(self.direccion),
            math.sin(self.direccion))
        self.posx += math.cos(self.direccion)
        self.posy += math.sin(self.direccion)
        self.colisiona()
    def colisiona(self):
        if self.posx < 0 or self.posx > 1024 or self.posy < 0 or self.posy >1024:
            self.direccion += math.pi
def guardarPersonas():
    print ("Guardo a los jugadores")
    cadena = json.dumps([vars(persona) for persona in personas])
    print(cadena)
    
# Creo una ventana
raiz = tk.Tk()
	
# En la ventana creo un lienzo
lienzo = tk.Canvas(raiz,width=1024, height=700)
lienzo.pack()

#Botón de guardar
boton = tk.Button(raiz, text= "Guarda", command=guardarPersonas)
boton.pack()

# En la colección introduzco instancias de personas
for i in range(0, numeropersonas):
    personas.append(Persona())

# Para cada una de las personas en la colección las pinto
for persona in personas:
    persona.dibuja()

# Creo un bucle que se repite cada 1000 milisegundos
def bucle():
    # Para cada persona en la colección
    for persona in personas:
        persona.mueve()
    raiz.after(10, bucle)

# Ejecuto el bucle
bucle()

raiz.mainloop()


			
	
