from os import system
import re

class resolverIP():
    
    def __init__(self):
        pass
    
    def direccionIP(self):
        try:
            ip = input("Ingrese una dirección IP:\n ")
            assert len(ip.strip()) <= 15 and len(ip.strip()) >= 9
            return ip
        except Exception:
            print("Error, la ip ingresada no es valida!!!")
    
    def mascara(self):
        try:
            print("Ejemplo: 24")
            print("*******************************")
            mascara = int(input("Ingrese la mascara:\n "))
            assert len(ip.strip()) <= 15 and len(ip.strip()) >= 9
            return ip
        except Exception:
            print("Error, la ip ingresada no es valida!!!")
    
    def mascaraIP(self):
        pass
    
    def resolucionIP(self):
        resIp = self.direccionIP()
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
            octeto1 = bin(int(octeto1))
            octeto2 = bin(int(octeto2))
            octeto3 = bin(int(octeto3))
            octeto4 = bin(int(octeto4))
            print("ip en binario: "+ str(octeto1[2:8]+octeto2[2:8]+octeto3[2:8]+octeto4[2:8]))
        except:
            print("Error De conversion!!!")
            
    def menu(self):
        try:
            print("================== MENU ==================")
            print("= 1- Ingreso de dirección IP y Mascara   =")
            print("= 2- Ver la resolucion de una IP         =")
        except Exception:
    
    def ejecucion(self):
        self.menu()
        pass
    
principal = resolverIP()
principal.ejecucion()