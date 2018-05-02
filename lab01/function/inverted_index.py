#coding: utf-8
import nltk as n
import operator as o

inverted_index = {}
def build(data):
    data["noticia"] = data.titulo + " " + data.conteudo
    for index, doc in data.iterrows():
        doc.noticia = doc.noticia.lower()
        words = [str(word) for word in n.word_tokenize(doc.noticia)]
        for word in words:
            inverted_index.setdefault(word, []).append(doc.idNoticia)


    for word in inverted_index.keys():
        inverted_index[word] = set(inverted_index[word])

    return inverted_index

def search(term):
    term = n.word_tokenize(term)

    if len(term) == 1:
        return _search_one_term(term[0])
    elif len(term) == 3 and term[1].upper() == "AND":
        return _search_and(term[0], term[2])
    elif len(term) == 3 and term[1].upper() == "OR":
        return _search_or(term[0], term[2])


def _search_one_term(term):
    if inverted_index.has_key(term.lower()):
        return sorted(list(inverted_index[term.lower()]))
    else:
        return "Você quis dizer %s" % (_word_proximity(term))

def _search_and(first_term, second_term):
    if inverted_index.has_key(first_term.lower()) and inverted_index.has_key(second_term.lower()):
        return sorted(list(inverted_index[first_term.lower()] & inverted_index[second_term.lower()]))
    else:
        return None

def _search_or(first_term, second_term):
    if inverted_index.has_key(first_term.lower()) and inverted_index.has_key(second_term.lower()):
        return sorted(list(inverted_index[first_term.lower()] | inverted_index[second_term.lower()]))
    elif inverted_index.has_key(first_term.lower()):
        return sorted(list(inverted_index[first_term.lower()]))
    elif inverted_index.has_key(second_term.lower()):
        return sorted(list(inverted_index[second_term.lower()]))
    else:
        return None

def _word_proximity(search_word):
    distance = {}
    for word in inverted_index.keys():
        distance[word] = n.edit_distance(search_word, word)

    sorted_list = sorted(distance.items(), key = o.itemgetter(1))
    return sorted_list[0]