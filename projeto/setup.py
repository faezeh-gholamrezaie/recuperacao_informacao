import nltk as n
import numpy as np
import pandas as p
import re
import matplotlib.pyplot as plt
from unicodedata import normalize
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.manifold import TSNE

def build(data):
    data["noticia"] = data.titulo + " " + data.subTitulo + " " + data.conteudo
    docs = []

    for index, doc in data.iterrows():
        doc.noticia = doc.noticia.lower()
        docs.append(clear_text(doc.noticia))

    return docs

def clear_text(text):
    pattern = re.compile('[^a-zA-Z0-9 ]')
    text = normalize('NFKD', text).encode('ASCII', 'ignore').decode('ASCII')

    return pattern.sub(' ', text)

data = p.read_csv("data-set/estadao_noticias_eleicao.csv", encoding = "utf-8")[:200]
data = data.replace(np.NAN, "")

docs = build(data)
vectorizer = TfidfVectorizer()
vector = vectorizer.fit_transform(docs)

# K-means
km = KMeans(n_clusters=6, init='k-means++', max_iter=300, n_init=10)
km = km.fit(vector.toarray())
labels = km.fit_predict(vector.toarray())
centroids = np.array(km.cluster_centers_)

print(vector.toarray())
print(labels)
print(centroids)

# tsne_init = 'pca'  # could also be 'random'
# tsne_perplexity = 20.0
# tsne_early_exaggeration = 4.0
# tsne_learning_rate = 1000
# random_state = 1
# model = TSNE(n_components=3, random_state=random_state, init=tsne_init, perplexity=tsne_perplexity,
#          early_exaggeration=tsne_early_exaggeration, learning_rate=tsne_learning_rate)
#
#
# transformed_centroids = model.fit_transform(centroids)
# plt.scatter(centroids[:, 0], centroids[:, 1], marker='x')
# plt.show()
