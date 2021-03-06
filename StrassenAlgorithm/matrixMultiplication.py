from tkinter import *
from tkinter import filedialog, messagebox
numStrassen = 0
numDef = 0

def getMatrix(path):
    file = open(path, 'r').read().splitlines()
    matrix = []
    for line in file:
        matrix.append(list(map(int,line.split(','))))
    return matrix

def getMatrixOrder(matrix):
    return len(matrix)

def generateMatrix(size):
    return [[0 for i in range(size)] for j in range(size)]

def sumMatrices(a,b):
    order = getMatrixOrder(a)
    c = generateMatrix(order)
    for i in range(order):
        for j in range(order):
            c[i][j] = a[i][j] + b[i][j]
    return c

def substractMatrices(a,b):
    order = getMatrixOrder(a)
    c = generateMatrix(order)
    for i in range(order):
        for j in range(order):
            c[i][j] = a[i][j] - b[i][j]
    return c

def toString(matrix):
    s = ''
    for line in matrix:
        s += "\t".join(list(map(str, line))) + "\n"
    return s

def strassenMethod(a,b):
    global numStrassen

    order = getMatrixOrder(a)
    if(order <= 2):
        c = generateMatrix(order)
        for i in range(order):
            for k in range(order):
                for j in range(order):
                    c[i][j] += a[i][k] * b[k][j]
                    numStrassen += 1
        return c
    else:
        numStrassen += 7
        # dividing matrixC
        size = int(order/2)
        # this for A matrix
        a11 = generateMatrix(size)
        a12 = generateMatrix(size)
        a21 = generateMatrix(size)
        a22 = generateMatrix(size)
        # this for B matrix
        b11 = generateMatrix(size)
        b12 = generateMatrix(size)
        b21 = generateMatrix(size)
        b22 = generateMatrix(size)
        # traverse both matrices and diving them into 4
        for i in range(size):
            for j in range(size):
                a11[i][j] = a[i][j]
                a12[i][j] = a[i][j + size]
                a21[i][j] = a[i + size][j]
                a22[i][j] = a[i + size][j + size]

                b11[i][j] = b[i][j]
                b12[i][j] = b[i][j + size]
                b21[i][j] = b[i + size][j]
                b22[i][j] = b[i + size][j + size]

        m1 = strassenMethod(sumMatrices(a11, a22), sumMatrices(b11, b22))
        m2 = strassenMethod(sumMatrices(a21, a22), b11)
        m3 = strassenMethod(a11, substractMatrices(b12,b22))
        m4 = strassenMethod(a22, substractMatrices(b21, b11))
        m5 = strassenMethod(sumMatrices(a11, a12), b22)
        m6 = strassenMethod(substractMatrices(a21, a11), sumMatrices(b11, b12))
        m7 = strassenMethod(substractMatrices(a12, a22), sumMatrices(b21, b22))

        c11 = substractMatrices(sumMatrices(sumMatrices(m1, m4), m7), m5)
        c12 = sumMatrices(m3, m5)
        c21 = sumMatrices(m2, m4)
        c22 = substractMatrices(sumMatrices(m1,sumMatrices(m3,m6)), m2)

        c = generateMatrix(order)

        for i in range(size):
            for j in range(size):
                c[i][j] = c11[i][j]
                c[i][j + size] = c12[i][j]
                c[i + size][j] = c21[i][j]
                c[i + size][j + size] = c22[i][j]
        return c

def bookMethod(a,b):
    global numDef
    c = generateMatrix(getMatrixOrder(a))
    for i in range(getMatrixOrder(a)):
        for k in range(len(b[0])):
            for j in range(len(b[0])):
                c[i][j] += a[i][k] * b[k][j]
                numDef +=1
    return c

def multiplications():
    file1 = filedialog.askopenfilename(filetypes=(("Text files", "*.txt"), ("all files", "*.*")))
    file2 = filedialog.askopenfilename(filetypes=(("Text files","*.txt"),("all files","*.*")))
    m1 = getMatrix(file1)
    m2 = getMatrix(file2)
    if (getMatrixOrder(m1) == len(m2[0])):
        closeWindow()
        c1 = strassenMethod(m1, m2)
        c2 = bookMethod(m1,m2)
        print(toString(c1))
        print(toString(c2))
        if(getMatrixOrder(m1)<65):
            ventana2 = Tk()
            ventana2.title("Resultados")
            ventana2.geometry('760x600')
            etiqueta6 = Label(ventana2, text="Resultado con el algoritmo de Strassen")
            etiqueta7 = Label(ventana2, text=toString(c1))
            etiqueta8 = Label(ventana2, text="Resultado con el algoritmo de definición de multiplicación de matrices")
            etiqueta9 = Label(ventana2, text=toString(c2))
            etiqueta10 = Label(ventana2, text="Multiplicaciones Strassen: " + str(numStrassen))
            etiqueta11 = Label(ventana2, text="Multiplicationes A. de Definición: " + str(numDef))
            etiqueta6.grid(column=0, row=1)
            etiqueta7.grid(column=0, row=2)
            etiqueta8.grid(column=0, row=3)
            etiqueta9.grid(column=0, row=4)
            etiqueta10.grid(column=0, row=5)
            etiqueta11.grid(column=0, row=6)
            ventana2.mainloop()
    else:
        print("Te equivocaste, ingresa matrices del mismo tamaño")
        messagebox.showerror('Error','Las matrices son de distintos tamaños')
        closeWindow()

def closeWindow():
    ventana.destroy()


ventana = Tk()
ventana.title("Multiplicación de matrices")
ventana.geometry('750x600')
etiqueta1 = Label(ventana,text="Algoritmos de multiplicación de matrices", font=("Arial",30))
etiqueta2 = Label(ventana,text="Desarrollado por Jordan Gonzalez y Eduardo Gallegos", font=("Arial",20))
etiqueta3 = Label(ventana,text="Dale click al botón para comenzar", font=("Arial",15))
etiqueta4 = Label(ventana,text="Escoge las dos matrices a multiplicar en formato .txt", font=("Arial", 15))
etiqueta5 = Label(ventana,text="Y deja que el programa haga el resto", font=("Arial", 15))
#btn1 = Button(ventana, text="Escoge la primer matriz", command=chooseFile1)
#btn2 = Button(ventana, text="Escoge la segunda matriz ", command=chooseFile2)
btn3 = Button(ventana, text="Hacer las multiplicaciones", command=multiplications)
etiqueta1.grid(column=0, row=0)
etiqueta2.grid(column=0,row=1)
etiqueta3.grid(column=0, row=2)
etiqueta4.grid(column=0, row=3)
etiqueta5.grid(column=0, row=4)
#btn1.grid(column=0, row = 3)
#btn2.grid(column=0, row=4)
btn3.grid(column=0, row=5)
ventana.mainloop()
