from os import system
import re

class resolverIP():
    
    ip      = ""
    mascara = 0
    
    def __init__(self):
        pass
    
    def direccionIP(self):
        try:
            print("Ejemplo: 192.168.0.1")
            print("*******************************")
            self.ip = input("Ingrese una dirección IP:\n ")
            assert len(self.ip.strip()) <= 15 and len(self.ip.strip()) >= 9
            return self.ip
        except Exception:
            print("Error, la ip ingresada no es valida!!!")
    
    def mascaraIP(self):
        try:
            print("Ejemplo: 24")
            print("*******************************")
            self.mascara = int(input("Ingrese la mascara:\n "))
            assert self.mascara <= 32 and self.mascara >= 1
            return self.mascara
        except Exception:
            print("Error, la mascara ingresada no es valida!!!")
        except ValueError:
            print("No se permite texto en este campo, solo numeros, intente nuevamente!!!")
    
    def cantPisos(self):
        try:
            print("Ejemplo: 3")
            print("*******************************")
            pisos = int(input("Ingrese la cantidad de pisos para calcualar las sub redes:\n "))
            assert pisos <= 100 and pisos >= 1
            return pisos
        except Exception:
            print("Error, la cantidad de pisos ingresada no es valida!!!")
        except ValueError:
            print("No se permite texto en este campo, solo numeros, intente nuevamente!!!")
    
    def cantHost(self):
        try:
            print("Ejemplo: 12")
            print("*******************************")
            host = int(input("Ingrese la cantidad de Host:\n "))
            assert host <= 100 and host >= 1
            return host
        except Exception:
            print("Error, la cantidad de host ingresada no es valida!!!")
        except ValueError:
            print("No se permite texto en este campo, solo numeros, intente nuevamente!!!")
    
    def resolucionIP(self):
        resIp     = self.direccionIP()
        resMas    = self.mascaraIP()
        cantPisos = self.cantPisos()
        cantHost  = self.cantHost()
        # Se divide la cadena de texto para obtener los octetos
        sepOct = re.split(r'[;,.\s]\s*', resIp)
        cont = 0
        for ip in sepOct:
            print(ip)
            cont = cont + 1
            if cont == 1:
                oct1 = ip
            elif cont == 2:
                oct2 = ip
            elif cont == 3:
                oct3 = ip
            else:
                oct4 = ip

        print("Octeto 1: "+ oct1)
        print("Octeto 2: "+ oct2)
        print("Octeto 3: "+ oct3)
        print("Octeto 4: "+ oct4)
        
        convercion = self.conversionBinario(oct1,oct2,oct3,oct4)
        self.menu()
        
    def conversionBinario(self, octeto1, octeto2, octeto3, octeto4):
        try:
            # Se almacenan los octetos en una variable y se transforman a tipo numérico (int)
            octeto1 = bin(int(octeto1))
            octeto2 = bin(int(octeto2))
            octeto3 = bin(int(octeto3))
            octeto4 = bin(int(octeto4))
            print("ip en binario: "+ str(octeto1[2:8]+octeto2[2:8]+octeto3[2:8]+octeto4[2:8]))
        except:
            print("Error De conversion!!!")
            
    def menu(self):
        system('cls')
        print()
        try:
            if self.ip == "" and self.mascara == 0:
                print("IP: "  "   Mascara: \n" )
            else:
                print("IP: " + self.ip + "   Mascara: " + self.mascara +"\n")
            print("==========================================")
            print("=                  MENU                  =")
            print("==========================================")
            print("=                                        =")
            print("= 1- Ingreso de dirección IP y Mascara   =")
            print("= 2- Ver la resolucion de una IP         =")
            print("= 3- Ingresar otra IP y Mascara          =")
            print("==========================================\n")

            opc = int(input("Selecione una opcion:\n--> "))
            assert opc >= 1 and opc <= 3
            
            if opc == 1:
                self.resolucionIP()
            
        except Exception:
            print("Error en la opcion seleccionada, vuelva a intentarlo!!!")
        except ValueError:
            print("No se permite texto en este campo, solo numeros, intente nuevamente!!!")
        
    
    def ejecucion(self):
        self.menu()
    
principal = resolverIP()
principal.ejecucion()