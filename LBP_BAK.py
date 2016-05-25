import numpy
import time
from numpy import *
from scipy import misc
import matplotlib.pyplot as plt


def lbp(filename, cell_size=16, mode='none'):
    chart_list = []
    lbp_mat = calc_lbp_cell(filename, mode)
    height = len(lbp_mat)
    width = len(lbp_mat[1])
    for i in range(int(height / cell_size)):
        for j in range(int(width / cell_size)):
            cell = lbp_mat[i * cell_size: (i + 1) * cell_size][j * cell_size: (j + 1) * cell_size]
            print size(lbp_mat)
            cell_chart = lbp_chart(cell, mode)
            chart_list.append(cell_chart)
    return chart_list


# return type = list[][]
def calc_lbp_cell(filename, mode='none'):
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


# return type = list[][]
def calc_lbp_all(filename, mode='none'):
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
        uniform = {0: 0, 1: 1, 2: 2, 3: 3, 4: 4, 5: 58, 6: 5, 7: 6, 8: 7, 9: 58, 10: 58,
                   11: 58, 12: 8, 13: 58, 14: 9, 15: 10, 16: 11, 17: 58, 18: 58, 19: 58, 20: 58,
                   21: 58, 22: 58, 23: 58, 24: 12, 25: 58, 26: 58, 27: 58, 28: 13, 29: 58, 30: 14,
                   31: 15, 32: 16, 33: 58, 34: 58, 35: 58, 36: 58, 37: 58, 38: 58, 39: 58, 40: 58,
                   41: 58, 42: 58, 43: 58, 44: 58, 45: 58, 46: 58, 47: 58, 48: 17, 49: 58, 50: 58,
                   51: 58, 52: 58, 53: 58, 54: 58, 55: 58, 56: 18, 57: 58, 58: 58, 59: 58, 60: 19,
                   61: 58, 62: 20, 63: 21, 64: 22, 65: 58, 66: 58, 67: 58, 68: 58, 69: 58, 70: 58,
                   71: 58, 72: 58, 73: 58, 74: 58, 75: 58, 76: 58, 77: 58, 78: 58, 79: 58, 80: 58,
                   81: 58, 82: 58, 83: 58, 84: 58, 85: 58, 86: 58, 87: 58, 88: 58, 89: 58, 90: 58,
                   91: 58, 92: 58, 93: 58, 94: 58, 95: 58, 96: 23, 97: 58, 98: 58, 99: 58, 100: 58,
                   101: 58, 102: 58, 103: 58, 104: 58, 105: 58, 106: 58, 107: 58, 108: 58, 109: 58,
                   110: 58, 111: 58, 112: 24, 113: 58, 114: 58, 115: 58, 116: 58, 117: 58, 118: 58,
                   119: 58, 120: 25, 121: 58, 122: 58, 123: 58, 124: 26, 125: 58, 126: 27, 127: 28,
                   128: 29, 129: 30, 130: 58, 131: 31, 132: 58, 133: 58, 134: 58, 135: 32, 136: 58,
                   137: 58, 138: 58, 139: 58, 140: 58, 141: 58, 142: 58, 143: 33, 144: 58, 145: 58,
                   146: 58, 147: 58, 148: 58, 149: 58, 150: 58, 151: 58, 152: 58, 153: 58, 154: 58,
                   155: 58, 156: 58, 157: 58, 158: 58, 159: 34, 160: 58, 161: 58, 162: 58, 163: 58,
                   164: 58, 165: 58, 166: 58, 167: 58, 168: 58, 169: 58, 170: 58, 171: 58, 172: 58,
                   173: 58, 174: 58, 175: 58, 176: 58, 177: 58, 178: 58, 179: 58, 180: 58, 181: 58,
                   182: 58, 183: 58, 184: 58, 185: 58, 186: 58, 187: 58, 188: 58, 189: 58, 190: 58,
                   191: 35, 192: 36, 193: 37, 194: 58, 195: 38, 196: 58, 197: 58, 198: 58, 199: 39,
                   200: 58, 201: 58, 202: 58, 203: 58, 204: 58, 205: 58, 206: 58, 207: 40, 208: 58,
                   209: 58, 210: 58, 211: 58, 212: 58, 213: 58, 214: 58, 215: 58, 216: 58, 217: 58,
                   218: 58, 219: 58, 220: 58, 221: 58, 222: 58, 223: 41, 224: 42, 225: 43, 226: 58,
                   227: 44, 228: 58, 229: 58, 230: 58, 231: 45, 232: 58, 233: 58, 234: 58, 235: 58,
                   236: 58, 237: 58, 238: 58, 239: 46, 240: 47, 241: 48, 242: 58, 243: 49, 244: 58,
                   245: 58, 246: 58, 247: 50, 248: 51, 249: 52, 250: 58, 251: 53, 252: 54, 253: 55,
                   254: 56, 255: 57}
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
        for line in cell:
            for item in line:
                chart[item] += 1
        return chart
    if mode == 'uniform':
        chart = [0 for i in range(59)]
        return chart


def save_lbp_chart(chart, filename):
    # chart = chart[1:]  # except chart[0]
    print len(chart)
    print chart
    x = numpy.arange(len(chart))
    fig_h = plt.subplot(111)
    fig_h.bar(x, chart, alpha=.5, color='r')
    # plt.show()
    plt.savefig(filename)


def save_lbp_mat(lbp_mat, filename):
    nd_arr = array(lbp_mat)
    misc.imsave(filename, nd_arr)


def test_1():
    start = time.clock()
    fn = 'test.jpg'
    lbp_matrix = calc_lbp_all('./in/' + fn, mode='uniform')
    save_lbp_mat(lbp_matrix, './out/lbp/' + fn)
    save_lbp_chart(lbp_chart(lbp_matrix), './chart/lbp/' + fn)
    end = time.clock()
    print('Running time: %s Seconds' % (end - start))


def test():
    start = time.clock()
    fn = 'test.jpg'
    save_lbp_chart(lbp('./in/' + fn), './chart/lbp/' + fn)
    end = time.clock()
    print('Running time: %s Seconds' % (end - start))


def test_2():
    fn = 'test.jpg'
    lbp_matrix = calc_lbp_all('./in/' + fn, mode='uniform')
    save_lbp_mat(lbp_matrix, './out/lbp/out.bmp')
    read_matrix = misc.imread('./out/lbp/out.bmp')
    print lbp_matrix
    print read_matrix
