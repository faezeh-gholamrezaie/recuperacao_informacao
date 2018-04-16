import function.reader_csv as csv
import function.inverted_index as inverted_index

data = csv.get_data('data-set/noticias_estadao.csv')
dic = inverted_index.build(data)
print dic
