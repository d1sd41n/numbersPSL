
class Numbers():
    """Esta clase contiene un algoritmo que transforma numeros en ascii.
       En el constructor se ingresan las siguientes variables:
            size:tamaño que van a tener los numeros.
            number:cadena con los numeros, ejemplo:"123456"

       Variables:
            col y row : contienen los caracteres con los que se dibuja el numero
            data : Almacena cada numero dibujado en ascci
            fill : Variable auxiliar en el dibujo del numero, contiene la medida de las
                columnas menos dos(los bordes)

        metodos:
            manager : filtra los numeros repetidos de la cadena que ingreso el usuario
                y luego llama la funcion getNumber y le pasa cada numero que queda,
                el resultado lo almacena en data.
            getNumber : Convierte el numero que se le pasa en ascii y devuelve el resultado.
            transpose : hace transposicion a la lista.
            getAllNumbers : devuelve una lista con todos los numeros que ingreso el usuario
                en su orden debido, todo dentro de una lista.

        """

    col = '|'
    row = '_'
    data = {}
    fill = 0

    def __init__(self, size, number):
        self.number = str(number)
        self.col_size = size+2
        self.row_size = 2*size+1
        self.fill = self.col_size-2
        self.manager()
    
    def manager(self):
        nums = list(set(list(self.number))) # Se eliminan numeros repetidos
        for x in nums:
            self.data[x] = self.getNumber(x)
    
    def transpose(self, numbers):
        rows = len(numbers)
        cols = len(numbers[0])
        return [[numbers[x][y] for x in range(rows)] for y in range(cols)]
    
    def getNumber(self, num):
        patterns = {
        "a" : " ",
        "b" : self.col,
        "c" : " "+self.fill*self.row+" ",
        "d" : self.col+self.fill*" "+self.col,
        "e" : self.col+self.fill*self.row+self.col,
        "f" : " "+self.fill*" "+self.col,
        "g" : " "+self.fill*self.row+self.col,
        "h" : self.col+" "+self.fill*" ",
        "i" : self.col+self.fill*self.row+" ",
        "j" : (2+self.fill)*" ",
        "k" : self.col+self.fill*self.row+self.col,
         }
        recipes = {
            "0" : ["c","d","d","d","e"],
            "1" : ["a","b","b","b","b"],
            "2" : ["c","f","g","h","i"],
            "3" : ["c","f","g","f","g"],
            "4" : ["j","d","k","f","f"],
            "5" : ["c","h","i","f","g"],
            "6" : ["c","h","i","d","e"],
            "7" : ["c","f","f","f","f"],
            "8" : ["c","d","k","d","e"],
            "9" : ["c","d","k","f","g"],
        }
        number = []
        num = recipes[num]
        number.append(patterns[num[0]])
        aux = int((self.row_size-2)/2)
        for x in range(aux):
            number.append(patterns[num[1]])
        number.append(patterns[num[2]])
        for x in range(aux):
            number.append(patterns[num[3]])
        number.append(patterns[num[4]])
        return number
    
    def getAllNumbers(self):
        numbers = []
        for x in self.number:
            numbers.append(self.data[x])
        return self.transpose(numbers)