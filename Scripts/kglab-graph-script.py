import kglab

#load file in .ttl format
kg=kglab.KnowledgeGraph().load_rdf("public repo/OAI5GC-KB/KB5.ttl") #add your path to the .ttl file

#measure number of nodes and edges
measure=kglab.Measure()
measure.measure_graph(kg)
print("Number of edges:{}\n".format(measure.get_edge_count()))
print("Number of nodes:{}\n".format(measure.get_node_count()))

#style of the graph
VIS_STYLE = {
    "netw": {
        "color":"green",
        "size" : 30,
    },
    "base":{
        "color":"blue",
        "size":60,
    }
}

#creating the graph
subgraph = kglab.SubgraphTensor(kg)
pyvis_graph=subgraph.build_pyvis_graph(notebook=True, style=VIS_STYLE)
pyvis_graph.force_atlas_2based()
pyvis_graph.show_buttons(filter_=['physics'])

#save graph in .html format
pyvis_graph.show("public repo/OAI5GC-KB/KGraph5.html")  #add your path to the .html file
