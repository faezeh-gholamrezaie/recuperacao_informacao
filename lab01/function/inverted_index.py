#coding: utf-8
def build(data):
    inverted_index = {}
    for row in data:
        doc = row[1].split()
        doc_id = row[2]
        list_doc_id = []
        for word in doc:
            print word + doc_id
            inverted_index[word] = list_doc_id.append(doc_id)
        list_doc_id = []
    return inverted_index