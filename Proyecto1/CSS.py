global lista
global listaR
listaR=list()

lista=list()
import os
from Ruta  import *
from Errores import *
class CSS :
    def init(self):
       print("efe")
       
       
       
       
   
    def analizadorJS (cadena):
            estado=0
            lex=""
            columna=0
            Ubicacion=""
            Traduccion=""
            fila=0
            i=0
            lexV=0
            lexA=""
            ayuda=0
            print(".")
            n=0
            
            while(n<len(cadena)):
                
                print(str(n)+")")
                char =cadena[n]
                ayuda=0
                
                print(char+"->"+"-----"+str(estado))
                
                if estado==0:
                     print(".")
                     if char.isalpha():
                            print("estado1")
                            columna=columna+1
                            Traduccion+=char
                            n=n+1 
                            estado=1
                            
                            lex+=char
                     elif char==":":
                            print("token encontrado"+char)
                            Traduccion+=char
                            columna=columna+1
                            estado=0
                            n=n+1
                     elif char==",":
                            print("token encontrado"+char)
                            Traduccion+=char
                            columna=columna+1
                            estado=0
                            n=n+1
                     elif char==".":
                            print("token encontrado"+char)
                            Traduccion+=char
                            columna=columna+1
                            estado=0
                            n=n+1
                     elif char=="{":
                            print("token encontrado"+char)
                            Traduccion+=char
                            columna=columna+1
                            n=n+1
                            estado=0
                            
                     elif char=="}":
                            print("token encontrado"+char)
                            Traduccion+=char
                            columna=columna+1
                            estado=0
                            n=n+1
                     elif char=="(":
                            print("token encontrado"+char)
                            Traduccion+=char
                            columna=columna+1
                            estado=0
                            n=n+1
                     elif char ==" ":
                            columna=columna+1
                            estado=0
                            n=n+1
                            Traduccion+=char
                     elif char =="\n":
                            fila=fila+1
                            estado=0
                            columna=0
                            Traduccion+=char
                            n=n+1              
                     elif char==")":
                            print("token encontrado"+char)
                            Traduccion+=char
                            columna=columna+1
                            estado=0
                            n=n+1
                     elif char==":":
                            print("token encontrado"+char)
                            Traduccion+=char
                            columna=columna+1
                            estado=0
                            n=n+1
                     elif char==",":
                            print("token encontrado"+char)
                            Traduccion+=char
                            columna=columna+1
                            estado=0
                            n=n+1
                     elif char=="#":
                            print("token encontrado"+char)
                            Traduccion+=char
                            columna=columna+1
                            estado=0
                            n=n+1
                     elif char=="*":
                            print("token encontrado"+char)
                            Traduccion+=char
                            columna=columna+1
                            estado=0
                            n=n+1
                     elif char==";":
                            print("token encontrado"+char)
                            Traduccion+=char
                            columna=columna+1
                            estado=0
                            n=n+1
                     elif char=="-":
                            print("token encontrado"+char)
                            Traduccion+=char
                            columna=columna+1
                            estado=0
                            n=n+1
                     elif char=="%":
                            print("token encontrado"+char)
                            Traduccion+=char
                            columna=columna+1
                            estado=0
                            n=n+1
                     
                     elif char=="=":
                            print("token encontrado"+char)
                            Traduccion+=char
                            columna=columna+1
                            estado=0
                            n=n+1
                     elif char=="/":
                            print("token encontrado"+char)
                            Traduccion+=char
                            columna=columna+1
                            estado=8
                            n=n+1
                     elif char==",":
                            print("token encontrado"+char)
                            Traduccion+=char
                            columna=columna+1
                            estado=0
                            n=n+1
                     elif char=="+":
                            print("token encontrado"+char)
                            Traduccion+=char
                            columna=columna+1
                            estado=0
                            n=n+1
                     
                     elif char=="\"":
                            print("token encontrado"+char+"->"+" "+"A estado 4")
                            Traduccion+=char
                            columna=columna+1
                            estado=4
                            print(".")
                            n=n+1
                            
                     elif char.isdigit():
                            print("token encontrado"+char+"->"+" "+"A estado2")
                            Traduccion+=char
                            columna=columna+1
                            estado=0
                            print(".")
                            n=n+1
                     elif char=="\'":
                            print("token encontrado"+char+"->"+" "+"A estado5")
                            Traduccion+=char
                            columna=columna+1
                            estado=5
                            n=n+1
                            print(".")
                     elif char=="/":
                            print("token encontrado"+char+"->"+" "+"A estado6")
                            Traduccion+=char
                            columna=columna+1
                            estado=0
                            n=n+1
                     else:
                            print("error")
                            lex+=char
                            print(".")
                            print("error"+char) 
                            a=Errores()
                            a.Lex=lex
                            a.fila=fila
                            a.columna=columna
                            print(str(columna))
                            a.Descripcion="Simbolo no reconocido por el sistema"
                            lista.append(a)
                            lex=""                
                            estado=0
                            n=n+1
                elif estado==1:
                       
                     
                     if char.isalpha():
                            lex+=char
                            print(".")
                            estado=1
                            Traduccion+=char
                            columna=columna+1
                            n=n+1
                            print("concatenanado"+"------>"+lex)
                     elif lex=="color" :
                            print("palabra reservada "+" "+lex)
                            print(",")
                            lex=""
                            
                            estado=0
                            columna=columna+1
                     elif char=="-" :
                            lex+=char
                            estado=1
                            Traduccion+=char
                            columna=columna+1
                            print("concatenanado"+"------>"+lex)
                            n=n+1
                     elif lex=="border" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            print(",")
                            columna=columna+1
                     elif lex=="text-align" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            print(",")
                            columna=columna+1
                     elif lex=="font-weight" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            print(",")
                            columna=columna+1
                     elif lex=="padding-left" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            print(",")
                            columna=columna+1
                     elif lex=="padding-top" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            print(",")
                            columna=columna+1
                     elif lex=="line-height" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            print(",")
                            columna=columna+1
                     elif lex=="margin-top" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            print(",")
                            columna=columna+1
                     elif lex=="margin-left" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            print(",")
                            columna=columna+1
                     elif lex=="display" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            print(",")
                            columna=columna+1
                     elif lex=="top" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            print(",")
                            estado=0
                            columna=columna+1
                     elif lex=="float" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            print(",")
                            estado=0
                            columna=columna+1
                     elif lex=="min-width" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            n=n+1
                            estado=0
                            columna=columna+1
                     elif lex=="background-color" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            print(",")
                            columna=columna+1
                     elif lex=="Opacity" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            print(",")
                            columna=columna+1
                     elif lex=="font-family" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            print(",")
                            columna=columna+1
                     elif lex=="font-size" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            print(",")
                            estado=0
                            columna=columna+1
                     elif lex=="padding-right" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            print(",")
                            estado=0
                            columna=columna+1
                     elif lex=="padding" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            print(",")
                            estado=0
                            columna=columna+1
                     elif lex=="width" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            print(",")
                            estado=0
                            columna=columna+1
                     elif lex=="margin-right" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            print(",")
                            estado=0
                            columna=columna+1
                     elif lex=="margin" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            print(",")
                            columna=columna+1
                     elif lex=="position" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            print(",")
                            estado=0
                            columna=columna+1
                     elif lex=="right" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            print(",")
                            columna=columna+1
                     elif lex=="clear" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            print(",")
                            estado=0
                            columna=columna+1
                     elif lex=="max-height" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            print(",")
                            estado=0
                            columna=columna+1
                     elif lex=="background-image" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            columna=columna+1
                            print(",")
                     elif lex=="background" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            print(",")
                            columna=columna+1
                     elif lex=="font-style" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            columna=columna+1
                            print(",")
                     elif lex=="font" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            columna=columna+1
                            print(",")
                     elif lex=="padding-bottom" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            columna=columna+1
                            print(",")
                     elif lex=="display" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            columna=columna+1
                            print(",")
                     elif lex=="height" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            columna=columna+1
                            print(",")
                     elif lex=="margin-bottom" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            columna=columna+1
                            print(",")
                     elif lex=="border-stlye" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            columna=columna+1
                            print(",")
                     elif lex=="bottom" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            columna=columna+1
                            print(",")
                     elif lex=="left" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            columna=columna+1
                            print(",")
                     elif lex=="max-width" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            columna=columna+1
                            print(",")
                     elif lex=="min-height" :
                            print("palabra reservada "+" "+lex)
                            lex=""
                            estado=0
                            print(",")
                            columna=columna+1
                     elif char.isdigit() :
                            print("IDhtml "+" "+lex)
                            lex=""
                            estado=0
                            
                            print(",")
                            n=n+1

                            columna=columna+1
                     else  :
                            print("id "+" "+lex)
                            lex=""
                            columna=columna+1
                            print(",")
                            estado=0
                            
                            print(char+"char siguiente----------------"+str(n))
                            
              
                elif estado==2:
                     if char.isdigit():
                         print ("Concatenando digitos"+"-->"+char)
                         Traduccion+=char
                         columna=columna+1
                         estado=2
                         n=n+1
                     elif char==".":
                         print("concatenando ."+"->"+"A estado3")
                         Traduccion+=char
                         estado=3
                         n=n+1
                         columna=columna+1
                     else:
                         print("Token encontrado digito")  
                         columna=columna+1
                         print(",")
                         estado=0
                           
                elif estado==3:
                    if char.isdigit():
                            print ("Concatenando digitos para decimal"+"-->"+char)
                            Traduccion+=char
                            columna=columna+1
                            estado=3
                            n=n+1
                    else :
                            print("Token decimal encontrado")
                            columna=columna+1
                            estado=0
                            print(",")
                            Traduccion+=char
                            
                elif estado==4:
                       
                     
                    if char=="\"":
                        print("Token comillas")
                        Traduccion+=char
                        estado=0
                        columna=columna+1
                        n=n+1                                  
                    else:
                        print("concatenando comillas"+"--->"+char)
                        Traduccion+=char
                        estado=4
                        columna=columna+1   
                        n=n+1  
                elif estado==5:
                    if char=="\'":
                        print("TOken comillas simples")
                        Traduccion+=char
                        estado=0
                        
                        n=n+1
                        columna=columna+1                                  
                    else:
                        print("concatenando comillas"+"--->"+char)
                        Traduccion+=char
                        estado=4
                        n=n+1
                        columna=columna+1              
                elif estado==7:
                    if char=="*":
                        print("a estado 8  para comentario multilinea")
                        Traduccion+=char
                        columna=columna+1
                        estado=8
                        n=n+1
                    elif char=="/":
                        Traduccion+=char
                        columna=columna+1
                        estado=10
                        n=n+1
                        print(" A estado 10 para comentario de linea normal")            
                elif estado==8:
                    if char =="*":
                        Traduccion+=char
                        columna=columna+1
                        estado=9
                        n=n+1
                        print("concatenando ---"+char+" "+"A estado 9 para terminar comentario multi")
                    else:
                        Traduccion+=char
                        columna=columna+1
                        estado=8
                        n=n+1
                        if lexV==0:
                                   lexA+=char
                        print("concatenando para comentario multilinea"+"--"+char)           
                elif estado==9:
                    if char=="/":
                        Traduccion+=char
                        columna=columna+1
                        estado=0
                        n=n+1
                        lexv=1
                        print("comentario Multilinea")
                    else :
                        estado=8
                        n=n+1
                        
                        if lexV==0:
                                   lexA+=char
                        Traduccion+=char             
                elif estado==10:
                    if char=="\n":       
                        print("comentario de Linea")
                        estado=0
                        n=n+1
                        Traduccion+=char
                    else:
                        print("concatenando de linea"+"---"+char)   
                        n=n+1
            print("------6666666666666666666666"+lexA) 
            a=Ruta()
            a.Contenidop=Traduccion
            a.ruta=lexA
            listaR.append(a)
           
    def ReubicaionJs():
         cont=0 
         aux=0
         lex=""
         root=""
     
         for a in listaR:
              print("--"+a.ruta)
              for cont in range(len(a.ruta)):
                     char=a.ruta[cont]
                      
                     if aux==0:
                            if char.isalpha():
                                   aux=1
                                   print("a estado1 probando para la ruta")
                                   lex+=char
                            else:
                                   aux=0   
                     elif aux==1:
                            if char.isalpha():
                                   aux=1
                                   print("concatenando la ruta"+char)
                                   lex+=char 
                            elif lex=="PATHW":
                                   aux=3
                    
                    
                            
                   
                     elif aux==3:
                            if char==" ":
                                   print("fin-----")
                    
                            else :    
                                   root+=char
                    
                                   estado=3
                    
         print("ruta"+"------"+root)           
         os.mkdir(root)          
         a=open(root+'/'+'R.css','w')
         a.writelines(listaR[0].Contenidop)                              
    def graficarE():
          codigoHtml=""
          print("Errores")
          reporte=open("ReporteCss.html","w")
          codigoHtml ="<html >"
          codigoHtml+="<head>"+ "<title>Reporte </title>"  + "    </head>" + "    <body>\n"
          codigoHtml+= "    <center>" +""
          codigoHtml+=     "<h4> Reporte  Errores TOkens para JS</h4>"
          codigoHtml+=  "   <table border=4>"
          codigoHtml+="                 <tr>"
          codigoHtml+= "                    <td>#</td>"
          codigoHtml+=   "                    <td>Fila</td>"
          codigoHtml+= "                    <td>Columna</td>"
          codigoHtml+= "                    <td>Token</td>"
          codigoHtml+= "        <td>Descripcion</td>"
          codigoHtml+= "                                     " 
          codigoHtml+= "        </tr> "
          i=0         
          for a in lista:
              i+=1
              parseofila=str(a.fila)
              parseo_c=str(a.columna)
              parseo=str(i)
        
          
              print ("Error:"+" "+a.Lex)
              codigoHtml+= " <tr>\n"
          
              codigoHtml+=       "    <td>" + parseo + "</td>"
              codigoHtml+=       "    <td>" + parseofila + "</td>"
              codigoHtml+=       "    <td>" + parseo_c + "</td>"
              codigoHtml+=       "    <td>" + a.Lex + "</td>"
              codigoHtml+=       "    <td>" + a.Descripcion + "</td>"
              codigoHtml+= "  </tr>"
          codigoHtml += " </Tbody> <t/table>  </table><br<br>"     
          codigoHtml += " </Tbody> <t/table>  </table><br<br>"  
          reporte.writelines(codigoHtml)          
                  
                        
                        