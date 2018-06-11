#coding: utf-8
import function.index as inverted_index
import model.binary_representation as b
import model.TF as tf
import model.TF_IDF as tfidf
import model.BM25 as bm25
import validation.valid as valid
import pandas as p
import numpy as np
import sys
reload(sys)
sys.setdefaultencoding('utf8')

data = p.read_csv("data-set/estadao_noticias_eleicao.csv", encoding = "utf-8")
data = data.replace(np.NAN, "")

validation_data = p.read_csv("validation/gabarito.csv", encoding= "utf-8")
# inverted_index_values =  inverted_index.build(data)
#
# validation_data.google = validation_data.google.apply(inverted_index.convert_str_in_lst)
# validation_data.busca_binaria = validation_data.busca_binaria.apply(inverted_index.convert_str_in_lst)
# validation_data.tf = validation_data.tf.apply(inverted_index.convert_str_in_lst)
# validation_data.tfidf = validation_data.tfidf.apply(inverted_index.convert_str_in_lst)
# validation_data.bm25 = validation_data.bm25.apply(inverted_index.convert_str_in_lst)
#
# binary_search = [b.binary_representation(inverted_index_values, inverted_index.clear_text(term)) for term in validation_data.str_busca]
# print "Precisão gabarito busca binária: %.3f" % (valid.mapk(validation_data.busca_binaria, binary_search, k=5))
# print "Precisão gabarito busca google: %.3f" % (valid.mapk(validation_data.google, binary_search, k=5))
#
# tf_search = [tf.TF(inverted_index_values, inverted_index.clear_text(term)) for term in validation_data.str_busca]
# print "Precisão gabarito busca TF: %.3f" %(valid.mapk(validation_data.tf, tf_search, k=5))
# print "Precisão gabarito busca google: %.3f" %(valid.mapk(validation_data.google, tf_search, k=5))
#
# tfidf_search = [tfidf.TF_IDF(inverted_index_values, inverted_index.clear_text(term)) for term in validation_data.str_busca]
# print "Precisão gabarito busca TF-IDF: %.3f" %(valid.mapk(validation_data.tfidf, tfidf_search, k=5))
# print "Precisão gabarito busca google: %.3f" %(valid.mapk(validation_data.google, tfidf_search, k=5))
#
# bm25_search = [bm25.BM25(inverted_index_values, inverted_index.clear_text(term)) for term in validation_data.str_busca]
# print "Precisão gabarito busca  BM25: %.3f" %(valid.mapk(validation_data.bm25, bm25_search, k=5))
# print "Precisão gabarito busca google: %.3f" %(valid.mapk(validation_data.google, bm25_search, k=5))
