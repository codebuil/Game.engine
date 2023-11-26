import tkinter as tk
import random
import time

class CirculoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Circulo App")

        # Caixas de texto
        self.caixa_texto_x = tk.Entry(root)
        self.caixa_texto_x.pack()

        self.caixa_texto_y = tk.Entry(root)
        self.caixa_texto_y.pack()

        self.caixa_texto_decimal = tk.Entry(root)
        self.caixa_texto_decimal.pack()

        # Canvas para desenhar
        self.canvas = tk.Canvas(root, width=400, height=400, bg="brown")
        self.canvas.pack()

        # Chama a função de desenho a cada 2 segundos
        self.desenhar_circulo()

    def desenhar_circulo(self):
        # Limpa o canvas
        self.canvas.delete("all")

        # Obtém valores aleatórios
        zyx=[]
        for n  in range(6):
            x = random.randint(0, 10) - 5
            y = random.randint(0, 10) - 5
            z = random.randint(1, 10)
            index=n
            zyx=zyx+[(z,y,x,index)]
        zyx.sort()
        xx=[]
        yy=[]
        zz=[]
        index=[]
        for n in zyx:
            i=0
            for m in n:
               if i==0:
                   zz=zz+[0.0+m]
               if i==1:
                   yy=yy+[0.0+m]
               if i==2:
                   xx=xx+[0.0+m]
               if i==3:
                   index=index+[m]
               i+=1
        # Exibe os valores nas caixas de texto
        self.caixa_texto_x.delete(0, tk.END)
        self.caixa_texto_x.insert(0, f"zyx0: {zyx[0]}")

        self.caixa_texto_y.delete(0, tk.END)
        self.caixa_texto_y.insert(0, f"zyx1: {zyx[1]}")

        self.caixa_texto_decimal.delete(0, tk.END)
        self.caixa_texto_decimal.insert(0, f"zyx2: {zyx[2]}")

        # Desenha as linhas de divisão
        self.canvas.create_line(0, 200, 400, 200, fill="black")
        self.canvas.create_line(200, 0, 200, 400, fill="black")

        # Calcula as coordenadas do círculo
 
        # Desenha o círculo
        for n in range(3):
            self.canvas.create_oval(200.00+(20.00*(1.00/zz[n])*xx[n]), 200.00+(20.00*(1.00/zz[n])*yy[n]),200.00+(20.00*(1.00/zz[n])*(xx[n]+1.00)), 200.00+(20.00*(1.00/zz[n])*(yy[n]+1.00)), outline="yellow")

        # Agendar a próxima chamada após 2 segundos
        self.root.after(2000, self.desenhar_circulo)

# Criação da janela principal
root = tk.Tk()
root.configure(bg="brown", width=800, height=600)  # Define a cor de 
app = CirculoApp(root)
root.mainloop()

