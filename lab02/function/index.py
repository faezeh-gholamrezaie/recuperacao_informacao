# coding: utf-8
import nltk as n
import math
from collections import Counter

inverted_index = {}
def build(data):
    data["noticia"] = data.titulo + " " + data.subTitulo + " " + data.conteudo
    for index, doc in data.iterrows():
        doc.noticia = doc.noticia.lower()
        words = [str(word) for word in n.word_tokenize(doc.noticia)]
        freq_words = Counter(words)
        for word in words:
            inverted_index.setdefault(word, []).append((doc.idNoticia, freq_words[word]))

    for word in inverted_index.keys():
        inverted_index[word] = set(inverted_index[word])

    inverted_index_aux = {}
    M = len(data.noticia)
    for word in inverted_index.keys():
        k = len(list(inverted_index[word]))
        v_idf = idf(M, k)
        for i in range(len(list(inverted_index[word]))):
            inverted_index_aux.setdefault(word, []).append({
                "docId": list(inverted_index[word])[i][0],
                "tf": list(inverted_index[word])[i][1] ,
                "idf": v_idf
            })

    return inverted_index_aux


def idf(M, k): return  math.log((M + 1) / k)
