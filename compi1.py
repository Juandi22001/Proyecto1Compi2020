#!/usr/bin/env python3

#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF#
#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF#
#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF#
#F                                     F#   
#F                                     F#
#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF#
#F                                     F#
#F                                     F# 
#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF#
#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF#
#FFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFFF#


from tkinter import *
from tkinter import ttk
from tkinter.filedialog import askopenfilename
from tkinter import messagebox
from JS import *
from CSS import *
from HTML import *
from Expresiones import *
from tkinter.filedialog import asksaveasfile 
import os
alv =""
class Compi:     
    def __init__(self, window):
        self.ventana = window
        self.ventana.title("Proyecto1")
        self.valor=0
        
       
        frame = LabelFrame(self.ventana, text = '')
        frame.grid(row=0,column=0,columnspan=20,pady=20)

        #############################################_MENU_#############################################
        self.cargar = Button(frame, text ="Cargar", command = self.fileMenu)
        self.cargar.grid(row=0,column=0)
        
        self.guardar = Button(frame, text ="guardar" )
        
        self.guardar.grid(row=0,column=8)
        self.guardar.config(command= self.file_save)
        self.ejecutar = Button(frame, text ="Ejecutar", command = self.analizar)
        self.ejecutar.grid(row=0,column=1)

        self.salir = Button(frame, text ="Salir", command = self.terminar)
        self.salir.grid(row=0,column=2)

        ############################################_ENTRADA_############################################
        Label(frame,text='Archivo de Entrada:').grid(row=3,column=5)
        self.entrada = Text(frame, height=30, width=60)
        self.entrada.grid(row=4,column=5)
        Label(frame,text='   =>   ').grid(row=4,column=15)
        Label(frame,text='Resultado:').grid(row=3,column=16)
        self.salida = Text(frame, height=30, width=60)
        self.salida.grid(row=4,column=16)

        Label(frame,text='              ').grid(row=3,column=20)
    #END


    def fileMenu(self):
        filename = askopenfilename()
        alv=filename.split('.')[1]
        alv2=filename.split('/')
        aux=alv2[len(alv2)-1].split('.')[0]
        
        if alv=="js":
            print("Siuu")
            JS.ayudaName(aux)
            self.valor=1
        elif alv=="css":
            CSS.ayudaName(aux)
            self.valor=2
        elif alv=="html":
            print("se encontro un archivo HTML")
            HTML.ayudaName(aux)
            self.valor=3
        elif alv=="rmt":
            self.valor=4            
        
        auxs=2
        archivo = open(filename,"r")
        
        texto = archivo.read()
        archivo.close()
       
        self.entrada.insert(INSERT,texto)
         
        return
    #END
    
    def file_save(self):
    
          files = [('All Files', '*.*'),  
          ('Python Files', '*.js'), 
          ('Text Document', '*.txt')]
          name=asksaveasfile(mode='w', filetypes=files,defaultextension=files)
          text2save=(self.entrada.get(1.0,END))
          name.write(text2save)
          name.close()
         
        
    def analizar(self):
        texto = self.entrada.get("1.0",END)
        
        print("analizando: "+texto)
        if self.valor==1:
            JS.analizadorJS(texto)
            JS.ReubicaionJs()
            JS.graficarE()
            messagebox.showinfo("Analizando", "Javascript:\n")
        elif self.valor==2:
            CSS.analizadorJS(texto)
            CSS.ReubicaionJs()
            CSS.graficarE()
           
            messagebox.showinfo("Analizando", "css:\n")
        elif self.valor==3:
            print("ejecutando un archivo HTML")
            HTML.analizadorJS(texto)
            HTML.ReubicaionJs()
            HTML.graficarE()
            
           
            messagebox.showinfo("Analizando", "Html:\n")
        elif self.valor==4:
            Expresiones.analizadorJS(texto)
            Expresiones.graficarE()
            messagebox.showinfo("Analizando", "de expresiones:\n")
            
         
        #Expresiones.analizadorJS(texto)
        #Expresiones.graficarE()
        
        
        self.printSalida()
    #END


    def printSalida(self):
        texto = "Finalizo el analisis"
        self.salida.insert(INSERT,texto)

        messagebox.showerror("Error", "Texto a mostrar:\n")
    #END

    def terminar(self):
        self.ventana.destroy()
        return
    #END
#END

###################################################################################################
if __name__ == '__main__':
    window = Tk()
    app = Compi(window)
    window.mainloop()
