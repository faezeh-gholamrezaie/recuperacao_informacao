# coding: utf-8
import nltk as n
import re
import math
import ast
from unicodedata import normalize
from collections import Counter

def build(data):
    inverted_index = {}
    data["noticia"] = data.titulo + " " + data.subTitulo + " " + data.conteudo
    for index, doc in data.iterrows():
        doc.noticia = doc.noticia.lower()
        words = [clear_text(word) for word in n.word_tokenize(doc.noticia)]
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

def clear_text(text):
    pattern = re.compile('[^a-zA-Z0-9 ]')
    text = normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')
    return pattern.sub(' ', text)

def convert_str_in_lst(lista):
    return ast.literal_eval(lista)