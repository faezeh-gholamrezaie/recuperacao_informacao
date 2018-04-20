#coding: utf-8
import function.inverted_index as inverted_index
import pandas as p

import sys
reload(sys)
sys.setdefaultencoding('utf8')

data = p.read_csv("data-set/noticias_estadao.csv", encoding = "utf-8")

inverted_index.build(data)

# Sanity Check

# Campina AND Grande
assert len(inverted_index.search("Campina AND Grande")) == 12
assert len(inverted_index.search("Campina OR Grande")) == 1656
assert inverted_index.search("Campina AND Grande") == [1068, 1370, 1770, 1952, 1987, 2763, 2777, 2779, 4802, 5382, 5870, 6694]
assert len(inverted_index.search("Campina OR Grande")) == len(inverted_index.search("Campina")) + len(inverted_index.search("Grande")) - len(inverted_index.search("Campina AND Grande"))

# debate, presidenciável (AND e OR)

assert len(inverted_index.search("debate OR presidencial")) == 1770

assert len(inverted_index.search("debate AND presidencial")) == 201

# presidenciáveis, corruptos (AND e OR)

assert len(inverted_index.search("presidenciáveis OR corruptos")) == 164

assert len(inverted_index.search("presidenciáveis AND corruptos"))== 0

# Belo, Horizonte (AND e OR)

assert len(inverted_index.search("Belo OR Horizonte")) == 331

assert len(inverted_index.search("Belo AND Horizonte")) == 242
