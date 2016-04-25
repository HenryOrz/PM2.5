import numpy
from numpy import *
import matplotlib.pyplot as plt
from PIL import Image
import colorsys


def hsv_color(img):
    if isinstance(img, Image.Image):
        r, g, b = img.split()
        i = 0
        h_dat = []
        s_dat = []
        v_dat = []
        h_arr = [0 for i in range(256)]
        s_arr = [0 for i in range(256)]
        v_arr = [0 for i in range(256)]
        for rd, gn, bl in zip(r.getdata(), g.getdata(), b.getdata()):
            h, s, v = colorsys.rgb_to_hsv(rd / 255., gn / 255., bl / 255.)
            h = int(h * 255)
            s = int(s * 255)
            v = int(v * 255)
            h_dat.append(h)
            s_dat.append(s)
            v_dat.append(v)
            h_arr[h] += 1
            s_arr[s] += 1
            v_arr[v] += 1
        r.putdata(h_dat)
        g.putdata(s_dat)
        b.putdata(v_dat)
        return Image.merge('RGB', (r, g, b)), h_arr, s_arr, v_arr

im = Image.open('./in/5.jpg')
hsv_im, h_data, s_data, v_data = hsv_color(im)
x = numpy.arange(len(h_data))
fig_h = plt.subplot(131)
fig_s = plt.subplot(132)
fig_v = plt.subplot(133)
fig_h.bar(x, h_data, alpha=.5, color='r')
fig_s.bar(x, s_data, alpha=.5, color='g')
fig_v.bar(x, v_data, alpha=.5, color='b')
plt.show()
hsv_im.save('./out/5.jpg')