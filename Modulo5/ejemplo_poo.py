from abc import ABC,abstractmethod
#esta clase abstracta define lo minimo que deben tener las clases paras poder estar dentro del programa
#y minimo de atributos y metodos de la cada clase
class figura(ABC):
    def __init__(self,nombre):
        self.nombre=nombre
    #end __init__ constructor de la clase abtracta
    @abstractmethod
    def area(self):
        pass    
    #end area
    def perimetro(self):
        pass
    #end perimetro            
#end class figura abstracta  

class rectangulo(figura):
    def __init__(self,nombre,base,altura):
        super().__init__(nombre)
        self.base=base
        self.altura=altura
    #end constructor      
    def area(self):
        return self.base*self.altura
    #end area
    def perimetro(self):
        return (self.base+self.altura)*2
    #end perimetro
#end class rectangulo  

#se instancian los objetos sin necesidad de la setencia new
rect=rectangulo("Rectangulo",3.0,2.0)
cuad=rectangulo("Cuadradro unitario",2.0,2.0)
print("El rectangulo "+rect.nombre+" tiene un area de: "+str(rect.area())+" y un perimetro de: "+str(rect.perimetro()))
print("El rectangulo "+cuad.nombre+" tiene un area de: "+str(cuad.area())+" y un perimetro de: "+str(cuad.perimetro())) 
    