#coding: utf-8
def TF(inverted_index, term, k = 5):
    term_search = term.split()
    result_id = []
    result = {}
    for word_term in term_search:
        if inverted_index.has_key(word_term):
            docId_word_term = []
            for i in range(len(inverted_index[word_term])):
                docId_word_term.append(inverted_index[word_term][i]["docId"])
                result.setdefault(inverted_index[word_term][i]["docId"], []).append(inverted_index[word_term][i]["tf"])
            result_id.append(docId_word_term)

    i = set(result_id[0])
    for x in result_id[1:]:
        i = i & set(x)

    z = {}
    for x in i:
        z[x] = sum(result[x])
    return sorted(z, key = z.get, reverse = True)[:k]