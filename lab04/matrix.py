# coding: utf-8
import numpy as n
import pandas as p

D = 0.15
COMPLEMENT_D = 1 - D
count = 0

def generate_matrix_a(source, target, nodes):
    numeber_of_transactions = len(source)
    numeber_of_nodes = len(nodes)

    a = n.zeros(shape=(numeber_of_nodes, numeber_of_nodes))

    adjacence_dict = {
        node: [] for node in nodes
    }

    for i in range(numeber_of_transactions):
        origin = source[i]
        destiny = target[i]
        adjacence_dict[origin].append(destiny)

    for i in range(numeber_of_nodes):
        for j in range(numeber_of_nodes):
            origin = nodes[i]
            destiny = nodes[j]
            if destiny in adjacence_dict[origin]: a[j][i] = float(1) / float(len(adjacence_dict[origin]))

    return n.matrix(a)

def pagerank(v):
    global count
    count += 1
    if sum(abs( m * v - v)) > 0.001:
        return pagerank(m * v)

    return m * v

data = p.read_csv('data-set/ratings.csv', encoding='utf-8')
data = data.sort_values(by=['SOURCE', 'TARGET'])

source = list(data.SOURCE)
target = list(data.TARGET)
nodes = list(set(source) | set(list(target)))

numeber_of_nodes = len(nodes)

a = generate_matrix_a(source, target, nodes)
b = (float(1) / float(numeber_of_nodes)) * n.matrix([[1] * numeber_of_nodes for i in range(numeber_of_nodes)])
m = COMPLEMENT_D * a + D * b
v = (float(1) / float(numeber_of_nodes)) * n.matrix([[1] for i in range(numeber_of_nodes)])

result = pagerank(v)
result = [cell.item(0,0) for cell in result]

print (count)
to_data_frame = p.DataFrame({
    'id': nodes,
    'PageRank': result
})
to_data_frame = to_data_frame.sort_values('PageRank', ascending=False)
print (to_data_frame)
to_data_frame.to_csv('data-set/result-PageRank.csv', index=False)
