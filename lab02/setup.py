#coding: utf-8
import function.index as inverted_index
import pandas as p

import sys
reload(sys)
sys.setdefaultencoding('utf8')

data = p.read_csv("data-set/estadao_noticias_eleicao.csv", encoding = "utf-8")
inverted_index.build(data)
