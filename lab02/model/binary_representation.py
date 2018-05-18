#coding: utf-8
def binary_representation(inverted_index, term, k = 5):
    term_search = term.split()
    result = []
    for word_term in term_search:
        if inverted_index.has_key(word_term):
            docId_word_term = []
            for i in range(len(inverted_index[word_term])):
                docId_word_term.append(inverted_index[word_term][i]["docId"])
            result.append(docId_word_term)

    i = set(result[0])
    for x in result[1:]:
        i = i & set(x)

    return list(i)[:k]