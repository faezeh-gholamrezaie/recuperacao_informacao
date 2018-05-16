#coding: utf-8
import function.index as inverted_index
import model.binary_representation as b
import pandas as p
import numpy as np

import sys
reload(sys)
sys.setdefaultencoding('utf8')

data = p.read_csv("data-set/estadao_noticias_eleicao.csv", encoding = "utf-8")[:1]
data = data.replace(np.NAN, "")
# print inverted_index.build(data)
# print b.binary_representation(inverted_index.build(data), "segundo turno")
b.binary_representation(data, "segundo turno")