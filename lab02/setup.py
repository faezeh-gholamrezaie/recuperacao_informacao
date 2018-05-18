#coding: utf-8
import function.index as inverted_index
import model.binary_representation as b
import model.TF as tf
import model.TF_IDF as tfidf
import pandas as p
import numpy as np

import sys
reload(sys)
sys.setdefaultencoding('utf8')

data = p.read_csv("data-set/estadao_noticias_eleicao.csv", encoding = "utf-8")
data = data.replace(np.NAN, "")
inverted_index =  inverted_index.build(data)


b.binary_representation(inverted_index, "segundo turno")
# tf.TF(inverted_index, "segundo turno")
# tfidf.TF_IDF(inverted_index, "segundo turno")