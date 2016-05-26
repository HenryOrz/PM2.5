import numpy
import time
import os
import shutil
from numpy import *
from PIL import Image
import colorsys


def hsv(filename):
    img = Image.open(filename)
    if isinstance(img, Image.Image):
        print img.size
        h, w = img.size
        step = int((h/800)*(w/1000))
        if step <= 0:
            step = 1
        print step
        r, g, b = img.split()
        h_chart = [0 for i in range(256)]
        s_chart = [0 for i in range(256)]
        v_chart = [0 for i in range(256)]
        for rd, gn, bl in zip(r.getdata(), g.getdata(), b.getdata())[::step]:

            h, s, v = colorsys.rgb_to_hsv(rd / 255., gn / 255., bl / 255.)
            h = int(h * 255)
            s = int(s * 255)
            v = int(v * 255)

            h_chart[h] += 1
            s_chart[s] += 1
            v_chart[v] += 1

        return h_chart, s_chart, v_chart


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


def test2(in_dir, out_dir, label):
    # start = time.clock()
    jpg_list = [x for x in os.listdir(in_dir) if os.path.splitext(x)[-1] == '.jpg']
    len_list = len(jpg_list)
    count = 1.0
    for fn in jpg_list:
        print 'processing ', str(count*100/len_list)+'%', '\t'+in_dir + '\\' + fn
        h_chart, s_chart, v_chart = hsv(in_dir + '\\' + fn)
        save_hsv_chart(h_chart, s_chart, v_chart, out_dir, label)
        count += 1
    # end = time.clock()
    # print('Running time: %s Seconds' % (end - start))



# test2(r'C:\Users\Henry.Z\Desktop\PM2.5.TEST\in', r'C:\Users\Henry.Z\Desktop\PM2.5.TEST\out\hsvchart', 0)


test2("D:\DataSet\Test\\0", "D:\DataOut\hsv", 0)
shutil.copyfile("D:/DataOut/hsv/h_chart.txt", "D:/DataOut/hsv/bak/0/h_chart.txt")
shutil.copyfile("D:/DataOut/hsv/s_chart.txt", "D:/DataOut/hsv/bak/0/s_chart.txt")
shutil.copyfile("D:/DataOut/hsv/v_chart.txt", "D:/DataOut/hsv/bak/0/v_chart.txt")
# print 'processing 1'
# test2("D:\DataSet\Test\\1", "D:\DataOut\hsv", 1)
# shutil.copyfile("D:/DataOut/hsv/h_chart.txt", "D:/DataOut/hsv/bak/1/h_chart.txt")
# shutil.copyfile("D:/DataOut/hsv/s_chart.txt", "D:/DataOut/hsv/bak/1/s_chart.txt")
# shutil.copyfile("D:/DataOut/hsv/v_chart.txt", "D:/DataOut/hsv/bak/1/v_chart.txt")
# print 'processing 2'
# test2("D:\DataSet\Test\\2", "D:\DataOut\hsv", 2)
# shutil.copyfile("D:/DataOut/hsv/h_chart.txt", "D:/DataOut/hsv/bak/2/h_chart.txt")
# shutil.copyfile("D:/DataOut/hsv/s_chart.txt", "D:/DataOut/hsv/bak/2/s_chart.txt")
# shutil.copyfile("D:/DataOut/hsv/v_chart.txt", "D:/DataOut/hsv/bak/2/v_chart.txt")
# print 'processing 3'
# test2("D:\DataSet\Test\\3", "D:\DataOut\hsv", 3)
# shutil.copyfile("D:/DataOut/hsv/h_chart.txt", "D:/DataOut/hsv/bak/3/h_chart.txt")
# shutil.copyfile("D:/DataOut/hsv/s_chart.txt", "D:/DataOut/hsv/bak/3/s_chart.txt")
# shutil.copyfile("D:/DataOut/hsv/v_chart.txt", "D:/DataOut/hsv/bak/3/v_chart.txt")
# print 'processing 4'
# test2("D:\DataSet\Test\\4", "D:\DataOut\hsv", 4)
# shutil.copyfile("D:/DataOut/hsv/h_chart.txt", "D:/DataOut/hsv/bak/4/h_chart.txt")
# shutil.copyfile("D:/DataOut/hsv/s_chart.txt", "D:/DataOut/hsv/bak/4/s_chart.txt")
# shutil.copyfile("D:/DataOut/hsv/v_chart.txt", "D:/DataOut/hsv/bak/4/v_chart.txt")
# print 'processing 5'
# test2("D:\DataSet\Test\\5", "D:\DataOut\hsv", 5)
# shutil.copyfile("D:/DataOut/hsv/h_chart.txt", "D:/DataOut/hsv/bak/5/h_chart.txt")
# shutil.copyfile("D:/DataOut/hsv/s_chart.txt", "D:/DataOut/hsv/bak/5/s_chart.txt")
# shutil.copyfile("D:/DataOut/hsv/v_chart.txt", "D:/DataOut/hsv/bak/5/v_chart.txt")
