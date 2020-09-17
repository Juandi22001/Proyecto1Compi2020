global lista
global listaR
listaR=list()

lista=list()
import os
from Sintactic  import *
from Errores import *
class Expresiones:
    def init(self):
        print("efe")
    def analizadorJS(cadena):
            estado=0
            lex=""
            columna=0
            Ubicacion=""
            Traduccion=""
            fila=0
            lexA=""
            lexv=0
            ayuda=0
            i=0
            alv=0
            while(i<len(cadena)):
                char =cadena[i]
                lex+=char
                
                if char=="\n":
                    a=Sintactic()
                    print(lex+"---------------------")
                    a.Expresion=lex
                    if alv==0:
                        a.valor="correcto"
                    else:
                        a.valor="efe"
                    lex=""
                    lista.append(a)
                    alv=0
                elif char=="(":
                        alv=alv+1
                elif  char==")":
                    alv=alv-1    
                    
                i=i+1    
                

                
    def graficarE():
          codigoHtml=""
          print("Errores")
          reporte=open("ReporteExpresiones.html","w")
          codigoHtml ="<html >"
          codigoHtml+="<head>"+ "<title>Reporte </title>"  + "    </head>" + "    <body>\n"
          codigoHtml+= "    <center>" +""
          codigoHtml+=     "<h4> Reporte  Errores TOkens para JS</h4>"
          codigoHtml+=  "   <table border=4>"
          codigoHtml+="                 <tr>"
          codigoHtml+= "                    <td>#</td>"
          codigoHtml+=   "                    <td>Expresion</td>"
          codigoHtml+= "        <td>Descripcion</td>"
          codigoHtml+= "                                     " 
          codigoHtml+= "        </tr> "
          i=0         
          for a in lista:
              i+=1
              parseo=str(i)
        
          
              codigoHtml+= " <tr>\n"
          
              codigoHtml+=       "    <td>" + parseo + "</td>"
              codigoHtml+=       "    <td>" + a.Expresion + "</td>"
              codigoHtml+=       "    <td>" + a.valor + "</td>"
              codigoHtml+= "  </tr>"
                   
          codigoHtml += " </Tbody> <t/table>  </table><br<br>"  
          reporte.writelines(codigoHtml)          
                                               
        
                          
            
                        