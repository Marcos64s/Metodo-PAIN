from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


def sub2ind(array_shape, rows, cols):
    return rows * array_shape[1] + cols


uniform = 0
circle = 1

w, h = 1024, 1024
if uniform is 1:
    data = np.random.random((h, w))
if circle is 1:
    n = w
    factor=500

    x = np.random.normal(w/16,10,size=n*factor)  # radius
    y = np.random.normal(h/16,10,size=n*factor) # angle


    #x = np.intc((np.sqrt(r) * np.cos(theta)) * n/2 + n/2)
    #y = np.intc((np.sqrt(r) * np.sin(theta)) * n/2 + n/2)
    print(x)
    data = np.zeros((h, w))
    data[np.intc(x),np.intc(y)] = 1
    print(data)

img = Image.fromarray(data, 'L')

img.save('C:/Users/asus/PycharmProjects/Projeto 2/compared.png')
img.show()
