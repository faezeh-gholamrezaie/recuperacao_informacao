#coding: utf-8
def BM25(inverted_index, term, k = 5):
    term_search = term.split()