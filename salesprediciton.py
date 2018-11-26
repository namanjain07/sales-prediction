import pandas as pd
import matplotlib.pyplot as plt
from scipy import stats
from tkinter import *

root = Tk()
data = pd.read_csv("advert.csv")
root.geometry("300x200")

lblTitle = Label(root,text="Sales Predictor")
lblTitle.pack()

T = data["TV"].values
R = data["Radio"].values
N = data["Newspaper"].values
Y = data["Sales"].values

"""TV SALES 0.7-296 """
data = stats.linregress(T,Y)
b1 = data[0]
b0 = data[1]

Y1 = []

for x in T:
    y = b0 + (b1*x)
    Y1.append(y)

"""RADIO SALES  0-49.6"""
data1 = stats.linregress(R,Y)
b1 = data[0]
b0 = data[1]

Y2 = []

for x in R:
    y = b0 + (b1*x)
    Y2.append(y)

"""NEWS SALES  0.3-114"""
data2 = stats.linregress(N,Y)
b1 = data[0]
b0 = data[1]

Y3 = []

for x in N:
    y = b0 + (b1*x)
    Y3.append(y)




def onClick():
    print("=====PREDICTED TV SALES VALUES==============")
    print(Y1)
    print("============================================")
    plt.xlabel('TV')
    plt.ylabel('Sales')
    plt.grid(True)
    # plt.plot(X, Y, "ro")
    plt.plot(T, Y, "o", T, Y1)
    plt.show()



def onClick1():
    print("=====PREDICTED RADIO SALES VALUES===========")
    print(Y2)
    print("============================================")
    plt.xlabel('Radio')
    plt.ylabel('Sales')
    plt.grid(True)
    # plt.plot(X, Y, "ro")
    plt.plot(R, Y, "o", R, Y2)
    plt.show()


def onClick2():
    print("=====PREDICTED NEWSPAPER SALES VALUES=======")
    print(Y3)
    print("============================================")
    plt.xlabel('Newspaper')
    plt.ylabel('Sales')
    plt.grid(True)
    # plt.plot(X, Y, "ro")
    plt.plot(N, Y, "o", N, Y3)
    plt.show()


btnSubmit = Button(root,text="TV",padx=30,pady=10,command=onClick)
btnSubmit.pack()

btnSubmit = Button(root,text="Radio",padx=20,pady=10,command=onClick1)
btnSubmit.pack()

btnSubmit = Button(root,text="Newspaper",padx=20,pady=10,command=onClick2)
btnSubmit.pack()

root.mainloop()