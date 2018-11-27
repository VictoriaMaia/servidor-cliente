import time
s_low = "0"
s_high = "1"
s_out = "out"
s_in = "in"
pino0 = "66" #P8_07 
pino1 = "67" #P8_08 
pino2 = "69" #P8_09 
pino3 = "68" #P8_10 
pino4 = "45" #P8_11 
pino5 = "44" #P8_12  
pino6 = "23" #P8_13 
pino7 = "26" #P8_14 

teclado = [["1","2","3","A"],["4","5","6","B"],["7","8","9","C"],["*","0","#","D"]]

def criarGPIO(pino):
    export_file = open('/sys/class/gpio/export', 'w')
    export_file.write(pino)
    export_file.close

def confDir(pino, Dir):
    caminho = "/sys/class/gpio/gpio" + pino + "/direction"
    io_direction = open(caminho, "w")
    io_direction.write(Dir)
    io_direction.close

def readHigh(pino):
    caminho = "/sys/class/gpio/gpio" + pino + "/value"
    io_read = open(caminho, "r")
    value = io_read.read()
    io_read.close
    return int(value)

def confValue(pino, value):
    caminho = "/sys/class/gpio/gpio" + pino + "/value"    
    io_value = open(caminho, "w")
    io_value.write(value)
    io_value.close

def verificaColuna(pinoHigh, i, texto):
    confValue(pino0, s_low)
    confValue(pino1, s_low)
    confValue(pino2, s_low)
    confValue(pino3, s_low)
    confValue(pinoHigh, s_high)
    
    if(readHigh(pino4) == 1):
        if(teclado[i][0] == "*"):
            return True
        texto.append(teclado[i][0])
        while(readHigh(pino4) == 1):
            print(teclado[i][0])
            time.sleep(0.5)
    elif(readHigh(pino5) == 1):
        texto.append(teclado[i][1])
        while(readHigh(pino5) == 1):
            print(teclado[i][1])
            time.sleep(0.5)
    elif(readHigh(pino6) == 1):
        texto.append(teclado[i][2])
        while(readHigh(pino6) == 1):
            print(teclado[i][2])
            time.sleep(0.5)
    elif(readHigh(pino7) == 1):
        texto.append(teclado[i][3])
        while(readHigh(pino7) == 1):
            print(teclado[i][3])
            time.sleep(0.5)

def iniciar():
    criarGPIO(pino0)
    criarGPIO(pino1)
    criarGPIO(pino2)
    criarGPIO(pino3)
    criarGPIO(pino4)
    criarGPIO(pino5)
    criarGPIO(pino6)
    criarGPIO(pino7)

    confDir(pino0, s_out)
    confDir(pino1, s_out)
    confDir(pino2, s_out)
    confDir(pino3, s_out)
    confDir(pino4, s_in)
    confDir(pino5, s_in)
    confDir(pino6, s_in)
    confDir(pino7, s_in)


def lerTeclado():
    texto = []
    while True:
        verificaColuna(pino0, 0, texto)
        verificaColuna(pino1, 1, texto)
        verificaColuna(pino2, 2, texto)
        if(verificaColuna(pino3, 3, texto) == True):
            break
    
    return ''.join(texto)

    


