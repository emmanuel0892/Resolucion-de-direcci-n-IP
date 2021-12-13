from os import system
import re

class resolverIP():
    
    ip      = ""
    mascara = 0
    
    def __init__(self):
        pass
    
    def direccionIP(self):
        system("cls")
        try:
            print("Ejemplo: 192.168.0.1")
            print("*******************************")
            self.ip = input("Ingrese una dirección IP:\n ")
            assert len(self.ip.strip()) <= 15 and len(self.ip.strip()) >= 9
            return self.ip
        except AssertionError:
            system("cls")
            print("Error, la ip ingresada no es valida!!!")
            system("pause")
            system("cls")
            self.menu()
    
    def mascaraIP(self):
        system("cls")
        try:
            print("Ejemplo: 24")
            print("*******************************")
            self.mascara = int(input("Ingrese la mascara:\n "))
            assert self.mascara <= 32 and self.mascara >= 1
            return self.mascara
        except AssertionError:
            system("cls")
            print("Error, la mascara ingresada no es valida!!!")
            system("pause")
            system("cls")
        except ValueError:
            system("cls")
            print("No se permite texto en este campo, solo numeros, intente nuevamente!!!")
            system("pause")
            system("cls")
    
    def cantPisos(self):
        system("cls")
        try:
            print("Ejemplo: 3")
            print("*******************************")
            pisos = int(input("Ingrese la cantidad de pisos para calcualar las sub redes:\n "))
            assert pisos <= 100 and pisos >= 1
            return pisos
        except AssertionError:
            system("cls")
            print("Error, la cantidad de pisos ingresada no es valida!!!")
            system("pause")
            system("cls")
        except ValueError:
            system("cls")
            print("No se permite texto en este campo, solo numeros, intente nuevamente!!!")
            system("pause")
            system("cls")
    
    def cantHost(self):
        system("cls")
        try:
            print("Ejemplo: 12")
            print("*******************************")
            host = int(input("Ingrese la cantidad de Host:\n "))
            assert host <= 100 and host >= 1
            return host
        except AssertionError:
            print("Error, la cantidad de host ingresada no es valida!!!")
            system("pause")
            system("cls")
        except ValueError:
            print("No se permite texto en este campo, solo numeros, intente nuevamente!!!")
            system("pause")
            system("cls")
    
    def resolucionIP(self):
        system("cls")
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
        
        
    def conversionBinario(self, octeto1, octeto2, octeto3, octeto4):
        try:
            # Se almacenan los octetos en una variable y se transforman a tipo numérico (int)
            # para convertirlos en binario.
            octeto1 = bin(int(octeto1))
            octeto2 = bin(int(octeto2))
            octeto3 = bin(int(octeto3))
            octeto4 = bin(int(octeto4))
            
            # Se almacenan los datos en binario dentro de otra variable
            # convirtiendolas en string y omitiendo sus dos primeros caracteres.
            oct1    = str(octeto1[2:10])
            oct2    = str(octeto2[2:10])
            oct3    = str(octeto3[2:10])
            oct4    = str(octeto4[2:10])
                          
            print(oct1)
            print(oct2)
            print(oct3)
            print(oct4)
            system('pause')
            octetos = (oct1+oct2+oct3+oct4)
            
            lista = []
            
        except:
            print("Error De conversion!!!")
            system('pause')
            system('cls')
        
        for x in octetos:
            lista.append(x)
        
        print(lista)
        system('pause')
  
        
        compOct = self.completarOctetos(oct1,oct2,oct3,oct4)
        
        self.menu()
        
            
    def completarOctetos(self, var1, var2, var3, var4):
        
        while True:
            if len(var1) < 8:
                 var1 = "0"+var1
        
        
    def menu(self):
        system('cls')
        opc = 0
        while opc <= 0 or opc >= 4:
            print("DIRECCION IP: " + self.ip + "        MASCARA: " + str(self.mascara))
            print()

            print("==========================================")
            print("=                  MENU                  =")
            print("==========================================")
            print("= 1- Ingreso de dirección IP y Mascara   =")
            print("= 2- Ver la resolucion de una IP         =")
            print("= 3- Ingresar otra IP y Mascara          =")
            print("==========================================\n")
            try:
                opc = int(input("Selecione una opcion:\n--> "))
                assert opc >= 1 and opc <= 3

            except AssertionError:
                system("cls")
                print("Error en la opcion seleccionada, vuelva a intentarlo!!!")
                system("pause")
                system("cls")
            
            except ValueError:
                system("cls")
                print("Error en la opcion seleccionada, vuelva a intentarlo!!!")
                system("pause")
                system("cls")
            
        if opc == 1:
            self.resolucionIP()
            opc = 0
        else:
            print()    
        
        
    
    def ejecucion(self):
        self.menu()
    
principal = resolverIP()
principal.ejecucion()