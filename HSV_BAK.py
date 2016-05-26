import numpy
import time
import os
import shutil
from numpy import *
import matplotlib.pyplot as plt
from PIL import Image
import colorsys


def hsv(filename):
    img = Image.open(filename)
    if isinstance(img, Image.Image):
        r, g, b = img.split()
        # h_dat = []
        # s_dat = []
        # v_dat = []
        h_chart = [0 for i in range(256)]
        s_chart = [0 for i in range(256)]
        v_chart = [0 for i in range(256)]
        for rd, gn, bl in zip(r.getdata(), g.getdata(), b.getdata()):
            h, s, v = colorsys.rgb_to_hsv(rd / 255., gn / 255., bl / 255.)
            h = int(h * 255)
            s = int(s * 255)
            v = int(v * 255)
            # h_dat.append(h)
            # s_dat.append(s)
            # v_dat.append(v)
            h_chart[h] += 1
            s_chart[s] += 1
            v_chart[v] += 1
        # r.putdata(h_dat)
        # g.putdata(s_dat)
        # b.putdata(v_dat)

        return h_chart, s_chart, v_chart
        # return Image.merge('RGB', (r, g, b)), h_dat, s_dat, v_dat, h_chart, s_chart, v_chart


def save_hsv_chart(h_chart, s_chart, v_chart, out_dir, label):
    with open(out_dir + '\\h_chart.txt', 'a') as fh:
        fh.write(str(label) + ' ')
        i = 1
        for x in h_chart:
            fh.write(str(i)+':'+str(x) + ' ')
            i += 1
        fh.write('\n')
    with open(out_dir + '\\s_chart.txt', 'a') as fh:
        fh.write(str(label) + ' ')
        i = 1
        for x in s_chart:
            fh.write(str(i)+':'+str(x) + ' ')
            i += 1
        fh.write('\n')
    with open(out_dir + '\\v_chart.txt', 'a') as fh:
        fh.write(str(label) + ' ')
        i = 1
        for x in v_chart:
            fh.write(str(i)+':'+str(x) + ' ')
            i += 1
        fh.write('\n')


def save_hsv_chart_fig(h_chart, s_chart, v_chart, filename):
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
    hsv_im, h_data, s_data, v_data, h_chart, s_chart, v_chart = hsv('./in/' + filename)
    save_hsv_chart(h_chart, s_chart, v_chart, './chart/hsv/' + filename)
    save_hsv_mat(hsv_im, './out/hsv/' + filename)
    end = time.clock()
    print('Running time: %s Seconds' % (end - start))


def test2(in_dir, out_dir, label):
    start = time.clock()
    for fn in os.listdir(in_dir):
        if os.path.splitext(fn)[-1] == '.jpg':
            h_chart, s_chart, v_chart = hsv(in_dir + '\\' + fn)
            save_hsv_chart(h_chart, s_chart, v_chart, out_dir, label)
    end = time.clock()
    print('Running time: %s Seconds' % (end - start))


print 'processing 0'
test2("D:\DataSet\Test\\0", "D:\DataOut\hsv", 0)
shutil.copyfile("D:/DataOut/hsv/h_chart.txt", "D:/DataOut/hsv/bak/0/h_chart.txt")
shutil.copyfile("D:/DataOut/hsv/s_chart.txt", "D:/DataOut/hsv/bak/0/s_chart.txt")
shutil.copyfile("D:/DataOut/hsv/v_chart.txt", "D:/DataOut/hsv/bak/0/v_chart.txt")
print 'processing 1'
test2("D:\DataSet\Test\\1", "D:\DataOut\hsv", 1)
shutil.copyfile("D:/DataOut/hsv/h_chart.txt", "D:/DataOut/hsv/bak/1/h_chart.txt")
shutil.copyfile("D:/DataOut/hsv/s_chart.txt", "D:/DataOut/hsv/bak/1/s_chart.txt")
shutil.copyfile("D:/DataOut/hsv/v_chart.txt", "D:/DataOut/hsv/bak/1/v_chart.txt")
print 'processing 2'
test2("D:\DataSet\Test\\2", "D:\DataOut\hsv", 2)
shutil.copyfile("D:/DataOut/hsv/h_chart.txt", "D:/DataOut/hsv/bak/2/h_chart.txt")
shutil.copyfile("D:/DataOut/hsv/s_chart.txt", "D:/DataOut/hsv/bak/2/s_chart.txt")
shutil.copyfile("D:/DataOut/hsv/v_chart.txt", "D:/DataOut/hsv/bak/2/v_chart.txt")
print 'processing 3'
test2("D:\DataSet\Test\\3", "D:\DataOut\hsv", 3)
shutil.copyfile("D:/DataOut/hsv/h_chart.txt", "D:/DataOut/hsv/bak/3/h_chart.txt")
shutil.copyfile("D:/DataOut/hsv/s_chart.txt", "D:/DataOut/hsv/bak/3/s_chart.txt")
shutil.copyfile("D:/DataOut/hsv/v_chart.txt", "D:/DataOut/hsv/bak/3/v_chart.txt")
print 'processing 4'
test2("D:\DataSet\Test\\4", "D:\DataOut\hsv", 4)
shutil.copyfile("D:/DataOut/hsv/h_chart.txt", "D:/DataOut/hsv/bak/4/h_chart.txt")
shutil.copyfile("D:/DataOut/hsv/s_chart.txt", "D:/DataOut/hsv/bak/4/s_chart.txt")
shutil.copyfile("D:/DataOut/hsv/v_chart.txt", "D:/DataOut/hsv/bak/4/v_chart.txt")
print 'processing 5'
test2("D:\DataSet\Test\\5", "D:\DataOut\hsv", 5)
shutil.copyfile("D:/DataOut/hsv/h_chart.txt", "D:/DataOut/hsv/bak/5/h_chart.txt")
shutil.copyfile("D:/DataOut/hsv/s_chart.txt", "D:/DataOut/hsv/bak/5/s_chart.txt")
shutil.copyfile("D:/DataOut/hsv/v_chart.txt", "D:/DataOut/hsv/bak/5/v_chart.txt")
