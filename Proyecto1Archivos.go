package main

import (
	"fmt"
	"io/ioutil"
	"strings"
	 "strconv"
	"bufio"
	"os"
)
var Mks [10] Mkdisk 
type Mkdisk struct{

	name string
	size int64
	path string
	unit string
	
	
	}
	
func main() {
	
	scanner()
     Creacion()

}

func scanner() {

	data, err := ioutil.ReadFile("./prueba.txt")

	if err != nil {
		fmt.Println("efe")

	}

	cadena := string(data)
	i2 := 0
	parts := strings.Split((cadena), ("\n"))

	for j := 0; j < len(parts); j++ {

		nivel := strings.Split((parts[j]), (" "))
		for i := 0; i < len(nivel); i++ {

			switch i2 {
			case 0:

				if "Mkdisk" == nivel[0] {
					i2 = 1

				} else if "exec" == nivel[0] {
					i2 = 2
				} else if "Fdisk" == nivel[0] {
					i2 = 3
				} else if "Mount" == nivel[0] {

					i2 = 3
				} else if "Pause" == nivel[i] {

					fmt.Print("Pausa presione ENter para continuar...")
					bufio.NewReader(os.Stdin).ReadBytes('\n') 
				}
			case 1:
				nivel2 := strings.Split((nivel[i]), ("->"))
				var Mk Mkdisk 
				for k := 0; k < len(nivel2); k++ {
					if "-path" == nivel2[k] {
                          Mk.path=nivel2[k+1]
						
					}
					if "-name" == nivel2[k] {
						Mk.name =nivel2[k+1]
					
					}
					if "-size" == nivel2[k] {

					n ,err:= strconv.ParseInt(string(nivel2[k+1]),10,32)
					if err != nil {
						panic(err)
					}
					Mk.size=n
			

					}
					if "-unit" == nivel2[k] {
						
						Mk.unit=nivel2[k+1]
					}
			
				}

			
			
			case 2:

				exec2 := strings.Split((nivel[i]), ("->"))

				for k := 0; k < len(exec2); k++ {
					if "-path" == exec2[k] {
						print(exec2[k+1])
					}
				}

			case 3:
				f2 := strings.Split((nivel[i]), ("->"))
				for k := 0; k < len(f2); k++ {
					if "-path" == f2[k] {
						print(f2[k+1])
					}
					if "-name" == f2[k] {
						print(f2[k+1])
					}
					if "-size" == f2[k] {
						print(f2[k+1])
					}
					if "-unit" == f2[k] {
						print(f2[k+1])
					}
					if "-type" == f2[k] {
						print(f2[k+1])
					}
					if "-delete" == f2[k] {
						print(f2[k+1])
					}
					if "-add" == f2[k] {
						print(f2[k+1])
					}

				}

			}

		}

	}

}
func Creacion(  ){
	
	

}
/* efe*/
