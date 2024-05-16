import sys
import ast
import numpy as np
import scipy.sparse


def read_array():
    return ast.literal_eval(sys.stdin.readline())

def write_array(arr):
    print(repr(arr.tolist()))


def generate_coocurrence_matrix(texts, vocab_size):
    voc = list(range(0,vocab_size))
    res = np.zeros((vocab_size,vocab_size))

    for i in voc:
        for j in text:
            if i in j:
                temp = []
                for k in voc:
                    if k != i:
                        temp.append(voc[k])
                
                for k in temp:
                    if k in j:
                        res[i][k] += 1
    
    res = np.array(res)
    return res


text = read_array()
vocab_size = int(sys.stdin.readline().strip())

result = generate_coocurrence_matrix(text, vocab_size)

write_array(result)