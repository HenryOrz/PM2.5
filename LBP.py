import numpy
import time
from numpy import *
from scipy import misc
import matplotlib.pyplot as plt


def lbp(filename, cell_size=16, mode='none'):
    chart_list = []
    lbp_mat = calc_lbp(filename, mode)
    height = len(lbp_mat)
    width = len(lbp_mat[1])
    for i in range(int(height/cell_size)):
        for j in range(int(width/cell_size)):
            cell = lbp_mat[i*cell_size: (i+1)*cell_size][j*cell_size: (j+1)*cell_size]
            cell_chart = lbp_chart(cell, mode)
            chart_list.append(cell_chart)
    return chart_list


# return type = list[][]
def calc_lbp(filename, mode='none'):
    compare_dict = {True: '1', False: '0'}
    im_mat = mat(misc.imread(filename, mode='L'))
    height, width = im_mat.shape
    lbp_mat = [[0 for j in range(width)] for i in range(height)]
    num = ['0' for i in range(8)]
    for i in range(1, height - 1):
        for j in range(1, width - 1):
            center = im_mat[i, j]
            num[0] = compare_dict[im_mat[i - 1, j - 1] > center]
            num[1] = compare_dict[im_mat[i - 1, j] > center]
            num[2] = compare_dict[im_mat[i - 1, j + 1] > center]
            num[3] = compare_dict[im_mat[i, j - 1] > center]
            num[4] = compare_dict[im_mat[i, j + 1] > center]
            num[5] = compare_dict[im_mat[i + 1, j - 1] > center]
            num[6] = compare_dict[im_mat[i + 1, j] > center]
            num[7] = compare_dict[im_mat[i + 1, j + 1] > center]
            lbp_bin = ''.join(num)
            lbp_val = int(lbp_bin, 2)
            mode_val = lbp_mode(lbp_val, mode)
            lbp_mat[i][j] = mode_val
    return lbp_mat


def lbp_mode(lbp_val, mode='none'):
    lbp_rot = {255: 255,
               127: 127, 191: 127, 233: 127, 239: 127, 247: 127, 251: 127, 254: 127, 253: 127,
               63: 63, 126: 63, 252: 63, 243: 63, 249: 63, 231: 63, 207: 63, 159: 63,
               31: 31, 62: 31, 124: 31, 248: 31, 241: 31, 227: 31, 199: 31, 143: 31,
               15: 15, 30: 15, 60: 15, 120: 15, 240: 15, 225: 15, 195: 15, 135: 15,
               7: 7, 14: 7, 28: 7, 56: 7, 112: 7, 224: 7, 193: 7, 131: 7}
    uniform = {}
    return {'none': lbp_val, 'lbprot': lbp_rot[lbp_val, 'uniform': uniform[lbp_val]]}[mode]


def lbp_chart(cell, mode='none'):
    if mode == 'none':
        chart = [0 for i in range(256)]
        for line in cell:
            for item in line:
                chart[item] += 1
        return chart
    if mode == 'lbprot':
        chart = [0 for i in range(36)]
        return chart
    if mode == 'uniform':
        chart = [0 for i in range(59)]
        return chart


def save_chart(chart, filename):
    chart = chart[1:256]  # except chart[0]
    x = numpy.arange(len(chart))
    fig_h = plt.subplot(111)
    fig_h.bar(x, chart, alpha=.5, color='r')
    # plt.show()
    plt.savefig(filename)


def save_lbp_mat(lbp_mat, filename):
    nd_arr = array(lbp_mat)
    misc.imsave(filename, nd_arr)


def test():
    start = time.clock()
    fn = 'test.jpg'
    lbp_matrix = calc_lbp('./in/' + fn)
    save_lbp_mat(lbp_matrix, './out/' + fn)
    save_chart(lbp_chart(lbp_matrix), './chart/' + fn)
    end = time.clock()
    print('Running time: %s Seconds' % (end - start))

