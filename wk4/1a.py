import networkx as nx

from networkx.algorithms.flow import ford_fulkerson

G = nx.DiGraph()
G.add_node('s', pos=(0,1))
G.add_node('1', pos=(1,2))
G.add_node('2', pos=(1,0))
G.add_node('3', pos=(2,2))
G.add_node('4', pos=(2,0))
G.add_node('t', pos=(3,1))

G.add_edge('s','1', capacity=2, flow='0/2')
G.add_edge('s','2', capacity=5, flow='5/5')
G.add_edge('s','3', capacity=3, flow='3/3')

G.add_edge('1','2', capacity=9, flow='0/9')

G.add_edge('2','3', capacity=6, flow='2/6')
G.add_edge('2','4', capacity=3, flow='3/3')

G.add_edge('3','1', capacity=4, flow='0/4')
G.add_edge('3','t', capacity=5, flow='5/5')

G.add_edge('4','1', capacity=1, flow='0/1')
G.add_edge('4','t', capacity=4, flow='3/4')
G.add_edge('4','3', capacity=2, flow='0/2')


R = ford_fulkerson(G, 's','t')
flow_value, flow_dict = nx.maximum_flow(G, 's', 't', flow_func=ford_fulkerson)
print(flow_value)
print(flow_dict)


labels = {}
import pylab as plt
for source_node in flow_dict:
    for dest_node in flow_dict[source_node]:
        labels[(source_node, dest_node)] = flow_dict[source_node][dest_node]

# pos = nx.shell_layout(G)
pos = nx.get_node_attributes(G, 'pos')
flow = nx.get_edge_attributes(G, 'flow')
nx.draw(G, pos)
# nx.draw_networkx_edge_labels(G, pos, labels, label_pos=0.6)
nx.draw_networkx_edge_labels(G, pos, flow, label_pos=0.6)
nx.draw_networkx_labels(G, pos)
plt.show()

