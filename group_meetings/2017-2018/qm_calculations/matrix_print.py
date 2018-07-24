import numpy as np
import sys
write = sys.stdout.write

def matrix_print_1d(array, m, n, ncols, title):
        """ printing a rectangular matrix, ncols columns per batch """

        write(title+':\n')
        nbatches = int(n/ncols)
        if nbatches * ncols < n: nbatches += 1
        for k in range(0, nbatches):
                write('    ')
                j1 = ncols*k
                j2 = ncols*(k+1)
                if k == nbatches-1: j2 = n
                for j in range(j1, j2):
                        write('   %7d  ' % (j+1))
                write('\n')
                for i in range(0, m):
                        write(' %2d -' % (i+1))
                        for j in range(j1, j2):
                                write(' %11.7f' % array[i+j*m])
                        write('\n')

def matrix_print_2d(array, ncols, title):
        """ printing a rectangular matrix, ncols columns per batch """

        #write(title+': (need to double check the order)\n')
        write(title+':\n')
        m = array.shape[1]
        n = array.shape[0]
        #write('m=%d n=%d\n' % (m, n))
        nbatches = int(n/ncols)
        if nbatches * ncols < n: nbatches += 1
        for k in range(0, nbatches):
                write('    ')
                j1 = ncols*k
                j2 = ncols*(k+1)
                if k == nbatches-1: j2 = n
                for j in range(j1, j2):
                        write('   %7d  ' % (j+1))
                write('\n')
                for i in range(0, m):
                        write(' %2d -' % (i+1))
                        for j in range(j1, j2):
                                write(' %11.6f' % array[j,i])
                        write('\n')


