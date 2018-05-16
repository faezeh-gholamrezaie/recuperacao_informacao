#coding: utf-8
import nltk as n

def binary_representation(data, term):
    term_search = term.split()
    vector_binary = {}
    data["noticia"] = data.titulo + " " + data.subTitulo + " " + data.conteudo
    for index, doc in data.iterrows():
        doc.noticia = doc.noticia.lower()
        words = [str(word) for word in n.word_tokenize(doc.noticia)]
        vector = []
        for word in words:
            for word_term in term_search:
                if word_term == word:
                    vector.append(1)
                elif len(vector) != 0:
                    vector.append(0)
        vector_binary[doc.idNoticia] = sum(vector)

    print vector_binary
