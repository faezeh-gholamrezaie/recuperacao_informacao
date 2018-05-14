#coding: utf-8
import nltk as n

inverted_index = {}
def build(data):
    data["noticia"] = data.titulo + " " + data.subTitulo + " " + data.conteudo
    for index, doc in data.iterrows():
        doc.noticia = doc.noticia.lower()
        words = [str(word) for word in n.word_tokenize(doc.noticia)]
        
        for word in words:
            inverted_index.setdefault((word, 1), []).append(doc.idNoticia)


    for word in inverted_index.keys():
        inverted_index[(word, 1)] = set(inverted_index[word])

    return inverted_index

def frequency(words, docId):
	for word in words:
		print word
		print docId
