import networkx as nx
import networkx as nx_2
from tkinter import *
import matplotlib.pyplot as plt

# Initial operations before start the coloring. Change path and wait_time if you want.
edge_path = "C:/Users/ÖZGE ELİBOL/Desktop/ozge.txt"
my_graph = nx.Graph()
colors = []
colors_of_nodes = {}
wait_time = 2
iteration = []
# GUI operations
root = Tk()
root.title('COLORS')
root.geometry("500x500")

root_2 = Tk()
root_2.title('EDGES')
root_2.geometry("500x500")

listbox = Listbox(root, width=40, height=10, selectmode=MULTIPLE)
label = Label(root, text="Colors")
listbox.insert(1, "blue")
listbox.insert(2, "orange")
listbox.insert(3, "green")
listbox.insert(4, "red")
listbox.insert(5, "purple")
listbox.insert(6, "brown")
listbox.insert(7, "pink")
listbox.insert(8, "gray")
listbox.insert(9, "olive")
listbox.insert(10, "cyan")


def selected_item():
    for i in listbox.curselection():
        colors.append(listbox.get(i))
        print(listbox.get(i))


def button_click():
    iteration.append(e1.get())
    print(iteration)


def close_colors():
    root.destroy()


listbox.pack()
btn = Button(root, text='Select', command=selected_item)
btn.pack(pady=20)
l1 = Label(root, text="Choose Iteration Time. If You Would Lıke To See Whole Steps Write -1")
l1.pack(pady=20)
e1 = Entry(root)
e1.pack(pady=20)
enter_button = Button(root, text="Enter", command=button_click)
enter_button.pack(pady=20)
close_button = Button(root, text="Exit", command=close_colors)
close_button.pack(pady=20)


def open_edges_txt():
    text_file = open(edge_path, 'r')
    stuff = text_file.read()
    my_text_2.insert(END, stuff)
    text_file.close()


def save_edges_txt():
    text_file = open(edge_path, 'w')
    text_file.write(my_text_2.get(1.0, END))
    text_file.close()


def close_edges():
    root_2.destroy()


my_text_2 = Text(root_2, width=40, height=10, font=("helvetica", 16))
my_text_2.pack(pady=20)
open_button = Button(root_2, text="Open Text File", command=open_edges_txt)
open_button.pack(pady=20)
save_button = Button(root_2, text="Save Text File", command=save_edges_txt)
save_button.pack(pady=20)
exit_button = Button(root_2, text="Exit", command=close_edges)
exit_button.pack(pady=20)


# Coloring operations
def promising(node, color):
    for neighbor in list(my_graph.neighbors(node)):
        color_of_neighbor = colors_of_nodes.get(neighbor)
        if color_of_neighbor == color:
            return False
    return True


def get_color_for_node(node):
    for color in colors:
        if promising(node, color):
            return color


# Main method
def main():
    root_2.mainloop()
    edges = nx.read_edgelist(edge_path)
    my_graph.add_edges_from(edges.edges())
    pos = nx.spring_layout(my_graph, seed=3113794652)
    nx.draw_networkx(my_graph, pos=pos, with_labels=True, node_color="burlywood")
    plt.title("Before Colorized")
    plt.show(block=False)
    plt.pause(wait_time)
    plt.close()
    new_graph = nx_2.Graph()
    new_graph.add_edges_from(edges.edges())
    node_colors = ["burlywood" for node in new_graph.nodes()]
    x = 0
    state = True
    for node in new_graph.nodes:
        if iteration[0] == str(x):
            plt.xlabel('The process has stopped because of the choose that you did in Step {}'.format(x))
            state = False
            break
        colors_of_nodes[node] = get_color_for_node(node)
        given_color = str(colors_of_nodes[node])
        new_graph.add_node(node, style='filled')
        node_colors[x] = given_color
        if node_colors[x] == 'None':
            plt.xlabel("Not enough color for the next steps")
            state = False
            node_colors[x] = "burlywood"
            break
        nx_2.draw_networkx(new_graph, pos=pos, node_color=node_colors, with_labels=True)
        plt.title('Step {}'.format(x + 1))
        plt.show(block=False)
        plt.pause(wait_time)
        plt.close()
        x += 1

    nx_2.draw_networkx(new_graph, pos=pos, node_color=node_colors, with_labels=True)
    plt.title("Final Version is {}".format(state))
    plt.show()
    # plt.show(block=False)
    # plt.pause(wait_time * 2)
    plt.close()


if __name__ == '__main__':
    main()