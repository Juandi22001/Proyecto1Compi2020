global lista
global listaR
listaR=list()

lista=list()
import os
from Ruta  import *
from Errores import *
class HTML:
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
            while(i<len(cadena)):
                char =cadena[i]
            
                if estado==0:
                    if char=="<":
                        estado=19
                        Traduccion+=char
                        columna=columna+1
                        print("a estado19")
                        ayuda=0
                        i=i+1
                    elif char.isalpha():
                         estado=1
                         Traduccion+=char
                         columna=columna+1
                         ayuda=0
                         i=i+1    
                    elif char==">":
                        if ayuda==20:
                            estado=0
                            Traduccion+=char
                            columna=columna+1
                            i=i+1
                        else:    
                            estado=2
                            Traduccion+=char
                            columna=columna+1
                            i=i+1
                             
                    elif char=="=":
                        Traduccion+=char
                        columna=columna+1
                        
                        i=i+1
                        estado=0
                               
                    elif char=="\"":
                        estado=4
                        columna=columna+1
                        Traduccion+=char
                        i=i+1
                    elif char==" ":
                        estado=0
                        columna=columna+1
                        Traduccion+=char
                        i=i+1
                    elif char=="\n":
                        estado=0
                        columna=0              
                        Traduccion+=char
                        fila=fila+1
                        i=i+1
                    else:
                         print("efe")
                         print("error")
                         lex+=char
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
                         i=i+1  
                elif estado==1:
                    if char.isalpha():
                        lex+=char
                        estado=1
                        Traduccion+=char
                        i=i+1
                    elif lex=="html":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="head":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="body":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif char=="!":
                         Traduccion+=char
                         estado=20
                         i=i+1
                         columna=columna+1     
                    elif lex=="tittle":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="body":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="h1":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="h2":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="h3":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="h4":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="h5":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="h6":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="p":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="img":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="src":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="a":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="href":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="ul":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="li":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="style":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="table":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="th":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="tr":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="td":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="caption":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="colgroup":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="col":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="thead":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="tbody":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                    elif lex=="tfoot":
                         lex+=char
                         estado=0
                         lex=""
                         Traduccion+=char
                                                                                                              
                    elif char.isdigit():
                         lex+=char
                         estado=1
                         i=i+1
                         Traduccion+=char  
                    else:
                        estado=0
                        lex=""
                        Traduccion+=char  
                elif estado==19:
                     if char=="!":
                          Traduccion+=char
                          columna=columna+1
                          estado=20
                          print("en estado 19")
                          i=i+1
                     else :
                         columna=columna+1
                         Traduccion+=char
                         estado=0
                         print("efe")
                         i=i+1                                
                
                elif estado==20:
                     if char=="-":
                          Traduccion+=char
                          columna=columna+1
                          estado=21
                          i=i+1
                     else :
                         columna=columna+1
                         Traduccion+=char
                         estado=0
                         print("efe")
                         i=i+1                                
                         
                elif estado==21:
                     if char=="-":
                          Traduccion+=char
                          columna=columna+1
                          estado=30
                          i=i+1
                          
                     else :
                         columna=columna+1
                         Traduccion+=char
                         estado=0
                         i=i+1
                         print("efe")
                         
                         
                elif estado==30:
                     if char=="-":
                          Traduccion+=char
                          columna=columna+1
                          estado=22
                          i=i+1
                     else :
                         columna=columna+1
                         Traduccion+=char
                         estado=0
                         print("efe")
                         i=i+1                                
                         
                elif estado==22:
                     if char=="-":
                          Traduccion+=char
                          columna=columna+1
                          estado=23
                          i=i+1
                     else :
                         columna=columna+1
                         Traduccion+=char
                         if lexv==0: 
                              lexA+=char
                         estado=22
                         i=i+1
                         print("efe")
                
                elif estado==23:
                     if char=="-":
                          Traduccion+=char
                          columna=columna+1
                          estado=40
                          i=i+1
                     else :
                         columna=columna+1
                         Traduccion+=char
                         estado=0
                         print("efe")
                         i=i+1
                elif estado==40:
                     if char=="-":
                          Traduccion+=char
                          columna=columna+1
                          estado=24
                          i=i+1
                     else :
                         columna=columna+1
                         Traduccion+=char
                         estado=0
                         print("efe")
                         i=i+1                                
                
                elif estado==24:
                     if char==">":
                          Traduccion+=char
                          columna=columna+1
                          estado=0
                          i=i+1
                     else :
                         columna=columna+1
                         Traduccion+=char
                         estado=0
                         print("efe")                  
                         i=i+1                                    
                
                elif estado==2:
                    if char=="<":
                        Traduccion+=char
                        estado=3
                        i=i+1
                        columna=columna+1
                    else:
                        Traduccion+=char
                        estado=2
                        i=i+1
                        columna=columna+1
                elif estado==3:
                    if char=="/":
                        Traduccion+=char
                        estado=1
                        i=i+1
                        columna=columna+1
                        ayuda=20
                    else:
                        estado=2
                        Traduccion+=char
                        columna=columna+1
                        i=i+1
                                          
                elif estado==4:
                     if char=="\"":
                         estado=0
                         columna=columna+1
                         Traduccion+=char
                         i=i+1
                        
                     else:
                         Traduccion+=char
                         estado=4
                         i=i+1
                         
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
          a=open(root+'/'+'R.html','w')
          a.writelines(listaR[0].Contenidop)                         
    def graficarE():
          codigoHtml=""
          print("Errores")
          reporte=open("ReporteHtml.html","w")
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