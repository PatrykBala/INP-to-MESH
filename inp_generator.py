import json
import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import Delaunay, delaunay_plot_2d

#funkcja do generowania danych siatki na podstawie danych wprowadzonych przez użytkownika
#zwraca listę wierzchołków oraz elementów
def generate_inp_data(name, width, height, nodes_count):
    
    #generowanie wierzchołków na krawędziach
    nodes = []
    nodes.append( [1, 0, 0] )
    node_id = 2
    for i in range(nodes_count):
        node = [ node_id, width*(i+1)/(nodes_count+1), 0 ]
        nodes.append(node)
        node_id += 1
    nodes.append( [node_id, width, 0] )
    node_id += 1
    for i in range(nodes_count):
        node = [ node_id, width, height*(i+1)/(nodes_count+1) ]
        nodes.append(node)
        node_id += 1
    nodes.append( [node_id, width, height] )
    node_id += 1
    for i in range(nodes_count):
        node = [ node_id, width - width*(i+1)/(nodes_count+1) , height ]
        nodes.append(node)
        node_id += 1
    nodes.append( [node_id, 0, height] )
    node_id += 1
    for i in range(nodes_count):
        node = [ node_id, 0, height - height*(i+1)/(nodes_count+1) ]
        nodes.append(node)
        node_id += 1
    nodes = np.array(nodes)

    #triangulacja przestrzeni
    tri = Delaunay(nodes[:,1:])
    fig = delaunay_plot_2d(tri)

    #generowanie obrazka .png z podglądem wyniku
    ax = fig.get_axes()
    ax[0].set_aspect("equal") 
    fig.savefig("outputPreview.png")

    #tworzenie listy z opisem elementów, które stworzyliśmy triangulacją
    elements = np.append(np.array([ [node_id+i] for i in range(len(tri.simplices))]), tri.simplices+1, axis=1)

    return nodes, elements

#funkcja do generowania pliku .inp na podstawie wygenerowanych danych
def generate_inp_file(name, nodes, elements):
    output = "*Heading\n"
    output +="*Preprint, echo=NO, model=NO, history=NO, contact=NO\n"
    output += "** PARTS\n"
    output += "*Part, name={} \n".format(name)
    output += "*Node\n"
    for node in nodes:
        output += "{}, {}, {}\n".format(round(node[0]), node[1], node[2])
    output += "*Element, type=CPS3\n"
    for el in elements:
        output += "{}, {}, {}, {}\n".format(round(el[0]), el[1], el[2], el[3])
    output += "*End Part"
    f = open(name+".inp", "w+")
    f.write(output)
    f.close()

# PROGRAM GŁÓWNY
#pobranie danych wejściowych z pliku JSON
try:
    data = json.load( open("input.json", "r") )
    name = data["name"]
    width = data["width"] 
    height = data["height"]
    nodes_count = data["nodes_count"]
except:
    print("Error with reading file.")
finally:
    nodes, elements = generate_inp_data(name, width, height, nodes_count)
    generate_inp_file(name, nodes, elements)