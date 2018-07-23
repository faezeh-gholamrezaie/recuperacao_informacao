import numpy as np
import pandas as p
import nltk as n
import matplotlib.pyplot as plt
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from collections import Counter
from sklearn.cluster import KMeans
from wordcloud import WordCloud
from sklearn.manifold import TSNE
from unicodedata import normalize

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

data = p.read_csv("data-set/estadao_noticias_eleicao.csv", encoding = "utf-8")[:100]
data = data.replace(np.NAN, "")

documents = build(data)

# documents = ["This little kitty came to play when I was eating at a restaurant",
#              "Merley has the best squooshy kitten belly",
#              "Google Translate app is incredible",
#              "If you open 100 tab in google you get a smiley face",
#              "Best cat photo I've ever taken",
#              "Climbing ninja cat",
#              "Impressed with google map feedback",
#              "Key promoter extension for Google Chrome"]

vectorizer = TfidfVectorizer(stop_words='english')
vector = vectorizer.fit_transform(documents)

km = KMeans(n_clusters= 2, init='k-means++', max_iter=10000, n_init=100)
km.fit(vector.toarray())
o = km.fit_transform(vector)

labels = km.fit_predict(vector.toarray())
centroids = np.array(km.cluster_centers_)

groups_dic = {}
groups_term_freq = {}

for i in range(len(documents)):
    groups_dic.setdefault(labels[i], []).append(documents[i])

for group in groups_dic.keys():
    groups_dic[group] = ' '.join(groups_dic[group])
    words = [word.lower() for word in n.word_tokenize(groups_dic[group])]
    freq_words = Counter(words)
    groups_term_freq[group] = freq_words.most_common()

    wordcloud = WordCloud(background_color='white', max_font_size=40).generate(groups_dic[group])
    plt.figure()
    plt.imshow(wordcloud, interpolation="bilinear")
    plt.title('Word Cloud do grupo ' + str(group))
    plt.axis("off")

for group in groups_term_freq.keys():
    s = groups_term_freq[group][:4]
    y = []
    x = []
    for i in range(len(s)):
        x.append(s[i][0])
        y.append(s[i][1])

    plt.figure()
    plt.barh(x, y, color="blue")
    plt.xlabel('Número de ocorrências')
    plt.title('Palavras com a maior frequência no grupo '+ str(group))


tsne_init = 'pca'  # could also be 'random'
tsne_perplexity = 20.0
tsne_early_exaggeration = 4.0
tsne_learning_rate = 1000
random_state = 1
model = TSNE(n_components=2, random_state=random_state, init=tsne_init, perplexity=tsne_perplexity,
         early_exaggeration=tsne_early_exaggeration, learning_rate=tsne_learning_rate)


transformed_centroids = model.fit_transform(centroids)
plt.figure()
plt.title('Grupos criados pelo algoritmo Kmeans')
plt.scatter(transformed_centroids[:, 0], transformed_centroids[:, 1], marker='x')

plt.show()

