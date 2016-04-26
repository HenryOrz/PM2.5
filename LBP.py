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
    for i in range(int(height / cell_size)):
        for j in range(int(width / cell_size)):
            cell = lbp_mat[i * cell_size: (i + 1) * cell_size][j * cell_size: (j + 1) * cell_size]
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
    if mode == 'none':
        return lbp_val
    if mode == 'lbprot':
        lbp_rot = {255: 255, 0: 0,
                   127: 127, 191: 127, 223: 127, 239: 127, 247: 127, 251: 127, 254: 127, 253: 127,
                   63: 63, 126: 63, 252: 63, 243: 63, 249: 63, 231: 63, 207: 63, 159: 63,
                   31: 31, 62: 31, 124: 31, 248: 31, 241: 31, 227: 31, 199: 31, 143: 31,
                   15: 15, 30: 15, 60: 15, 120: 15, 240: 15, 225: 15, 195: 15, 135: 15,
                   7: 7, 14: 7, 28: 7, 56: 7, 112: 7, 224: 7, 193: 7, 131: 7,
                   3: 3, 6: 3, 12: 3, 24: 3, 48: 3, 96: 3, 192: 3, 129: 3,
                   1: 1, 2: 1, 4: 1, 8: 1, 16: 1, 32: 1, 64: 1, 128: 1,
                   95: 95, 190: 95, 125: 95, 250: 95, 245: 95, 235: 95, 215: 95, 175: 95,
                   111: 111, 222: 111, 189: 111, 123: 111, 246: 111, 237: 111, 219: 111, 183: 111,
                   119: 119, 238: 119, 221: 119, 187: 119,
                   47: 47, 94: 47, 188: 47, 121: 47, 242: 47, 229: 47, 203: 47, 151: 47,
                   61: 61, 158: 61, 79: 61, 122: 61, 244: 61, 233: 61, 211: 61, 167: 61,
                   55: 55, 110: 55, 220: 55, 185: 55, 115: 55, 230: 55, 205: 55, 155: 55,
                   87: 87, 174: 87, 93: 87, 186: 87, 117: 87, 234: 87, 213: 87, 171: 87,
                   59: 59, 206: 59, 157: 59, 103: 59, 118: 59, 236: 59, 217: 59, 179: 59,
                   91: 91, 182: 91, 109: 91, 218: 91, 181: 91, 107: 91, 214: 91, 173: 91,
                   23: 23, 46: 23, 92: 23, 184: 23, 113: 23, 226: 23, 197: 23, 139: 23,
                   39: 39, 78: 39, 156: 39, 57: 39, 114: 39, 228: 39, 201: 39, 147: 39,
                   29: 29, 142: 29, 71: 29, 58: 29, 116: 29, 232: 29, 209: 29, 163: 29,
                   27: 27, 54: 27, 108: 27, 216: 27, 177: 27, 99: 27, 198: 27, 141: 27,
                   43: 43, 86: 43, 172: 43, 89: 43, 178: 43, 101: 43, 202: 43, 149: 43,
                   45: 45, 150: 45, 75: 45, 90: 45, 180: 45, 105: 45, 210: 45, 165: 45,
                   51: 51, 102: 51, 204: 51, 153: 51,
                   53: 53, 166: 53, 77: 53, 154: 53, 83: 53, 106: 53, 212: 53, 169: 53,
                   85: 85, 170: 85,
                   11: 11, 22: 11, 44: 11, 88: 11, 176: 11, 97: 11, 194: 11, 133: 11,
                   19: 19, 38: 19, 76: 19, 152: 19, 49: 19, 98: 19, 196: 19, 137: 19,
                   25: 25, 70: 25, 140: 25, 35: 25, 50: 25, 100: 25, 200: 25, 145: 25,
                   13: 13, 134: 13, 67: 13, 26: 13, 52: 13, 104: 13, 208: 13, 161: 13,
                   21: 21, 42: 21, 84: 21, 168: 21, 81: 21, 162: 21, 69: 21, 138: 21,
                   37: 37, 74: 37, 148: 37, 41: 37, 82: 37, 164: 37, 73: 37, 146: 37,
                   5: 5, 10: 5, 20: 5, 40: 5, 80: 5, 160: 5, 65: 5, 130: 5,
                   9: 9, 18: 9, 36: 9, 72: 9, 144: 9, 33: 9, 66: 9, 132: 9,
                   17: 17, 34: 17, 68: 17, 136: 17,
                   }
        return lbp_rot[lbp_val]
    if mode == 'uniform':
        uniform = {}
        return uniform[lbp_val]


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


def save_lbp_chart(chart, filename):
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
    lbp_matrix = calc_lbp('./in/' + fn, mode='none')
    save_lbp_mat(lbp_matrix, './out/lbp/' + fn)
    save_lbp_chart(lbp_chart(lbp_matrix), './chart/lbp/' + fn)
    end = time.clock()
    print('Running time: %s Seconds' % (end - start))

# test()
