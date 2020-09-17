global lista
global listaR
listaR=list()

lista=list()
import os
import webbrowser
from Ruta  import *
from Errores import *
class JS :
  estado=0
  lex=""
  def init(self):
      print("efe")
  def analizadorJS (cadena):
            estado=0
            lex=""
            alv=0
            columna=0
            Ubicacion=""
            Traduccion=""
            fila=0
            lexA=""
            valID=0
            valMulti=0
            valNOrmal=0
         
            i=0
            while (i<len(cadena)):
              char =cadena[i]
              
              if estado==0:
  
                if char.isalpha():
                    print("estado1")
                    columna=columna+1
                    Traduccion+=char
                    estado=1
                    lex+=char
                    i=i+1

                elif char.isdigit():
                    lex+=char
                    columna=columna+1
                    Traduccion+=char
                    estado=2   
                    i=i+1
                elif char is "\"":
                    estado=3
                    Traduccion+=char
                    columna=columna+1
                    i=i+1
                    
                    
                elif char is "\'":
                    Traduccion+=char
                    estado=18
                    columna=columna+1 
                    i=i+1
    
                elif char==";":
                    print("punto y coma")
                    Traduccion+=char
                    estado=0
                    columna=columna+1
                    i=i+1  
                elif char =="\t":
                            
                    estado=0
                    columna=columna+1
                    Traduccion+=char
                    n=n+1   
                elif char =="\r":
                            
                    estado=0
                    columna=columna+1
                    Traduccion+=char
                    n=n+1             
                elif char==":":
                    Traduccion+=char 
                    print("dos puntos")
                    estado=0
                    columna=columna+1 
                    i=i+1 
                elif char==".":
                    Traduccion+=char   
                    estado=0
                    columna=columna+1
                    i=i+1
                    print("punto")
                elif char==",":
                    Traduccion+=char
                    print("coma") 
                    estado=0
                    i=i+1
                    columna=columna+1  
                elif char=='/':
                    Traduccion+=char
                    estado=10
                    i=i+1
                    print("a estado 10")
                    columna=columna+1
                    
                elif char==" ":
                    Traduccion+=char
                    columna=columna+1
                    i=i+1
                elif char=="\n":
                    fila=fila+1
                    Traduccion+=char
                    columna=0
                    i=i+1
                elif char=="+":
                    lex+=char
                    estado=6
                    Traduccion+=char
                    columna=columna+1
                    i=i+1
                elif char==">":
                    estado=8
                    i=i+1
                    columna=columna+1
                    Traduccion+=char
                elif char=="<":
                    estado=9
                    i=i+1
                    columna=columna+1
                    Traduccion+=char
                elif char=="|":
                    estado=16
                    i=i+1
                    columna=columna+1
                    Traduccion+=char
              
                elif char=="=":
                    Traduccion+=char    
                    estado=17
                    i=i+1
                    columna=columna+1
                      
                elif char=="*":
                    Traduccion+=char
                    i=i+1
                    print("asterisco ")
                    columna=columna+1
      
                elif char=="-":
                    lex+=char
                    columna=columna+1
                    estado=7
                    i=i+1
                    Traduccion+=char
  
                elif char=="!":
                    lex+=char
                    Traduccion+=char
                    estado=4
                    i=i+1
                    columna=columna+1
                elif char=="&":
                    Traduccion+=char  
                    estado==15
                    columna=columna+1
                    i=i+1
                elif char=="[":
                    Traduccion+=char
                    estado=0
                    i=i+1 
                    columna=columna+1  
                elif char=="]":
                    Traduccion+=char
                    estado=0
                    i=i+1
                    columna=columna+1
                elif char=="(":
                    Traduccion+=char
                    estado=0
                    i=i+1
                    columna=columna+1
                elif char==")":
                    Traduccion+=char
                    estado=0
                    columna=columna+1
                    i=i+1
                      
                elif char=="{":
                    Traduccion+=char
                    estado=0
                    i=i+1
                    columna=columna+1   
                elif char=="}":
                    Traduccion+=char
                    estado=0
                    i=i+1
                    columna=columna+1   
                else : 
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
                    
              elif  estado==1:
                  
               if char.isalpha():
                  lex+=char
                  estado=1
                  i=i+1
                  Traduccion+=char
                  columna=columna+1
                  print(lex)
               elif lex=="if" :
                  print("if")
                  lex=""
                  estado=0
                  columna=columna+1
       
               elif "else" ==lex :
                  print("efe")
                  estado=0
                  lex=""
                  columna=columna+1   

               elif "var"==lex:
                    print("efe")
                    estado=0 
                    columna=columna+1
                    lex=""
                  
               elif "int"==lex :
                    print("I N T")
                    estado=0
                    columna=columna+1
                    lex=""
                   
               elif "string"==lex :
                    print("STRING")
                    estado=0
                    columna=columna+1
                    lex=""
                  
               elif "char"==lex :
                    print("CHAR")
                    estado=0
                    columna=columna+1
                    lex=""
                  
       
               elif "float"==lex :
                    print("float")
                    estado=0
                    columna=columna+1
               elif "boolean"==lex :
                    print("booolean")
                    estado=0
                    columna=columna+1
                    lex=""
                  
        
               elif "while"==lex :
                    print("while")
                    estado=0
                    columna=columna+1
                    lex=""
                  
         
               elif "do"==lex :
                    print("DO")
                    estado=0
                    columna=columna+1
                    lex=""
                  
         
               elif "break"==lex :
                    print("break")
                    estado=0
                    columna=columna+1
                    lex=""
                  
        
               elif "continue"==lex :
                    print("efe")
                    estado=0
                    columna=columna+1
                    lex=""
                  
       
               elif "return"==lex :
                  print("efe")
                  estado=0
                  columna=columna+1
                  lex=""
                  
         

               elif "false"==lex :
                    print("efe")
                    columna=columna+1
                    estado=0
                    lex=""
                  
               elif "true"==lex :
                    print("efe")
                    estado=0
                    columna=columna+1
                    lex=""
                   
               elif "function"==lex :
                    print("efe")
                    estado=0
                    columna=columna+1
                    lex=""       
               elif "class"==lex :
                    print("efe")
                    estado=0
                    columna=columna+1
                    lex=""
               elif "constructor"==lex :
                    print("efe")
                    estado=0
                    columna=columna+1
                    lex=""

               elif "this"==lex :
                      print("efe")
                      lex=""
                      estado=0
                      columna=columna+1
               elif char=="_":
                     estado=1
                     columna=columna+1
                     i=i+1
                     lex+=char 
               elif char.isdigit():
                     estado=1
                     columna=columna+1
                     i=i+1
                     lex+=char           
                      
               else:
                    print("encontrando id")
                    estado=0
                    valID=1
                    columna=columna+1
                    lex=""
             
              elif estado==2:
               if char.isdigit():
                    lex+=char
                    estado=2
                    Traduccion+=char
                    columna=columna+1
                    i=i+1
               elif char ==".":
                    estado=20
                    i=i+1
                    Traduccion+=char
                    columna=columna+1                      
               else:
                  print("token  digito")
                  estado=0
                  Traduccion+= char 
              elif estado==20:
                if char.isdigit():
                    print("digitos para decimal")
                    Traduccion+=char
                    columna=columna+1
                    i=i+1
                else :
                    print("digitos")
                    Traduccion+=char
                    estado=0        
              elif estado==3: 
                if char=="\"":
                  print("comillas")
                  lex+=char
                  Traduccion+=char
                  columna=columna+1
                  i=i+1
                  estado=0
                else:
                  lex+=char
                  Traduccion+=char
                  columna=columna+1
                  i=i+1
                  estado=3
              elif estado==4:
                if char =="=" :
                    print("!=")
                    Traduccion+=char
                    estado=0
                    columna=columna+1
                    i=i+1
                else:
                  print("diferente")
                  estado=0
              elif estado==6:
                if char =="=":
                    print("+=")
                    estado=0
                    Traduccion+=char
                    columna=columna+1
                    i=i+1 
                elif char=="+":
                    print("++")
                    estado=0
                    Traduccion+=char
                    i=i+1 
                    columna=columna+1
                else :
                    print("+")
                    estado=0
                    i=i+1 
                    columna=columna+1     
              elif estado==7:
                if char =="=":
                    print("-=")
                    estado=0
                    i=i+1
                    columna=columna+1
                    Traduccion+=char
                elif char=="-":
                    print("--") 
                    estado=0
                    i=i+1
                    columna=columna+1
                else:
                    print("-")
                    estado=0
                    i=i+1 
                    columna=columna+1     
              elif estado==8:
                  if char=="=":
                      print("menor o igual")
                      estado=0
                      Traduccion+=char
                      i=i+1 
                      columna=columna+1
                  else :
                      print("menor")
                      estado=0
                      i=i+1 
                      columna=columna+1
            
              elif estado==9:
                if char=="=":
                    print("mayor o igual")
                    i=i+1 
                    columna=columna+1
                    
                else :
                    print("mayor")
                    columna=columna+1
                    estado=0
                    i=i+1
              elif estado==10:
                
                if char=='*':
                    estado=11
                    Traduccion+=char
                    i=i+1 
                    columna=columna+1
                    print ("a estado11"+char )
                elif char=='/':
                    estado=14
                    Traduccion+=char
                    i=i+1 
                    columna=columna+1
                    
              elif estado==11:
                if char=="*":
                    estado=12
                    Traduccion+=char
                    i=i+1
                    print("a estado12"+char) 
                    columna=columna+1
                  
                else :
                    estado=11
                    lex+=char
                    i=i+1 
                    print("en estado 11"+"char")
                    columna=columna+1
                    Traduccion+=char
                    
                  
              elif estado==12:
                if char=="/":
                    print("comentario multi")
                    valMulti=3
                    Traduccion+=char
                    i=i+1 
                    columna=columna+1
                    estado=0
                    
                else:
                    estado=11
                    Traduccion+=char
                    i=i+1 
                    print("retorno estado 11"+"-"+char)
                    columna=columna+1
                  
              elif estado==14:
                if char=="\n":
                    print("comentario normal")
                    estado=0
                    valNOrmal=5
                    Traduccion+=char
                    alv=80
                    
                    i=i+1 
                    columna=columna+1
                else : 
                    lex+=char
                    Ubicacion+=char
                    estado=14
                    if alv==0:
                        lexA+=char
                    
                    Traduccion+=char  
                    i=i+1 
              elif estado==16:
                if char=="|":
                    print("or")
                    estado=0
                    Traduccion+=char
                    i=i+1 
                    columna=columna+1
                else :
                    print("error"+char)    
              elif estado==15:
                  if char=="&":
                      print("operador y")
                      estado=0
                      Traduccion+=char
                      i=i+1 
                      columna=columna+1
              elif estado==17:
                  if char=="=":
                      print("==")
                      estado=0
                      Traduccion+=char
                      columna=columna+1
                      i=i+1
                  else: 
                      print("=")
                      estado=0 
                              
              elif estado==18:
                  if char is "\'":                  
                    estado=0
                    print ("comillas")
                    Traduccion+=char
                    columna=columna+1
                    i=i+1
                  else:
                    estado=18
                    Traduccion+=char
                    columna=columna+1
                    i=i+1 
                    
            suma=valID+valMulti+valNOrmal
            print(str(suma)+"-----------------------------------------------------------------------")
            if suma==9:
                    webbrowser.open_new_tab("3er.Html")
            elif suma==4:
                    webbrowser.open_new_tab("id_Multi.html")
            elif suma==6:
                    webbrowser.open_new_tab("Id_Normal.html")
            elif suma==8:
                    webbrowser.open_new_tab("Comentarios.html")
            elif suma==1:
                    webbrowser.open_new_tab("ID.html")
            elif suma==3:
                    webbrowser.open_new_tab("Multi.html")
            elif suma==5:
                    webbrowser.open_new_tab("Normal.html")
                    
                    
                    
                            
                    
                
            
            print(lexA) 
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
                 elif lex=="PATHL":
                    aux=3
                    print("encontrada")
                    
                    
                    
             elif aux==2:
                if char==":":
                    aux=3
                    
             elif aux==3:
                if char==" ":
                    print("fin-----")
                    
                else :    
                    root+=char
                    
                    estado=3
                    
         print("ruta"+"------"+root)    
                
         os.mkdir(root)          
         a=open(root+'/'+'Re.js','w')
         a.writelines(listaR[0].Contenidop)                                                 
  def graficarE():
      codigoHtml=""
      print("Errores")
      reporte=open("ReporteJS.html","w")
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
                  
    
    
     
    
    
                    