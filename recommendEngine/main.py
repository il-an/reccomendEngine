#!/usr/bin/env python3
import networkx as nx
import networkx_viewer

n = input("Enter the number of users: ")

g = nx.Graph()
print("Now enter the names of the users")
for i in range(int(n)):
    user = input("Enter the name: ")
    g.add_node(user)

for i in range(int(n)):
    m = input(f"Enter the number of friends of {list(g.nodes)[i]}: ")
    print("Now enter the names of the friends")
    for j in range(int(m)):
        friend = input("Enter the name: ")
        g.add_edge(list(g.nodes)[i], friend)

print("The graph has been created")
app = networkx_viewer.Viewer(g)
app.mainloop()

