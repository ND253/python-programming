import networkx as nx
import matplotlib.pyplot as plt


G = nx.DiGraph()


def calculate_lists(user_input):
    """ Calculates the number of occurences of certain character in a string."""
    input_list = []
    for i in user_input:
        input_list.append(i)

    occurence_list = []
    for i in set(input_list):
        occurence_list.append((i, user_input.count(i)))

    sorted_by_first = sorted(occurence_list, key=lambda tup: tup[1])
    sorted_list = list(reversed(sorted_by_first))

    propability_list = []
    for i in range(len(sorted_list)):
        propability_list.append(sorted_list[i][1])

    print("Input list is: ", input_list)
    print("Input list is: ", input_list)
    print("Occurence list: ", occurence_list)
    print("Sorted list is: ", sorted_list)
    print("Probility list is: ", propability_list)
    return huffman_algorithm(propability_list)


def huffman_algorithm(prob_list):
    node_list = []
    while len(prob_list) != 1:
        first_minimum = min(float(s) for s in prob_list)
        print("First minimum", first_minimum)
        prob_list.remove(first_minimum)
        second_minimum = min(float(s) for s in prob_list)
        print("Second minimum", second_minimum)
        prob_list.remove(second_minimum)
        node_list.append([first_minimum, second_minimum])
        print("new value: ", first_minimum+second_minimum)
        new_value = int(first_minimum+second_minimum)
        prob_list.append(new_value)
    print("Finished: ", prob_list)
    labels = {}
    edge_list = []
    count = 1
    for i in node_list:
        print(count)
        print("Nodes: ", tuple(i))
        labels[count] = i[0]
        count += 1
        labels[count] = i[1]
        count += 1
        labels[count] = i[0] + i[1]
        edge_list.append((count-2, count))
        edge_list.append((count-1, count))
    print("Node list: ", node_list)
    print("Edge List: ", edge_list)
    G.add_nodes_from(labels.keys())
    G.add_edges_from(edge_list)
    print("Nodes: ", G.nodes())
    pos = nx.spring_layout(G)
    nx.draw(G, pos)
    nx.draw_networkx_labels(G, pos, labels)
    plt.savefig("graph1.png")
    plt.show()


def main():
    #user_input = str(input("Please enter a text: "))
    user_input ="aaaaabbbbcccdde"
    calculate_lists(user_input)


if __name__ == "__main__":
    main()
