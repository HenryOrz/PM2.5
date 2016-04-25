import numpy
import time
from numpy import *
import matplotlib.pyplot as plt
from PIL import Image
import colorsys


def hsv(filename):
    img = Image.open(filename)
    if isinstance(img, Image.Image):
        r, g, b = img.split()
        h_dat = []
        s_dat = []
        v_dat = []
        h_chart = [0 for i in range(256)]
        s_chart = [0 for i in range(256)]
        v_chart = [0 for i in range(256)]
        for rd, gn, bl in zip(r.getdata(), g.getdata(), b.getdata()):
            h, s, v = colorsys.rgb_to_hsv(rd / 255., gn / 255., bl / 255.)
            h = int(h * 255)
            s = int(s * 255)
            v = int(v * 255)
            h_dat.append(h)
            s_dat.append(s)
            v_dat.append(v)
            h_chart[h] += 1
            s_chart[s] += 1
            v_chart[v] += 1
        r.putdata(h_dat)
        g.putdata(s_dat)
        b.putdata(v_dat)
        return Image.merge('RGB', (r, g, b)), h_dat, s_dat, v_dat, h_chart, s_chart, v_chart


def save_hsv_chart(h_chart, s_chart, v_chart, filename):
    x = numpy.arange(len(h_chart))
    fig_h = plt.subplot(131)
    fig_s = plt.subplot(132)
    fig_v = plt.subplot(133)
    fig_h.bar(x, h_chart, alpha=.5, color='r')
    fig_s.bar(x, s_chart, alpha=.5, color='g')
    fig_v.bar(x, v_chart, alpha=.5, color='b')
    # plt.show()
    plt.savefig(filename)


def save_hsv_mat(hsv_im, filename):
    hsv_im.save(filename)


def test():
    start = time.clock()
    filename = 'test.jpg'
    hsv_im, h_data, s_data, v_data, h_chart, s_chart, v_chart = hsv('./in/'+filename)
    save_hsv_chart(h_chart, s_chart, v_chart, './chart/hsv/'+filename)
    save_hsv_mat(hsv_im, './out/hsv/'+filename)
    end = time.clock()
    print('Running time: %s Seconds' % (end - start))


# test()
