#!/usr/bin/env python3
import networkx as nx
import networkx_viewer
import time
import recommendation

n = input("Enter the number of users: ")

g = nx.Graph()
print("Now enter the names of the users")
# entering the nodes
for i in range(int(n)):
    user = input("Enter the name: ")
    g.add_node(user)

# entering the edges
for i in range(int(n)):
    m = input(f"Enter the number of friends of {list(g.nodes)[i]}: ")
    print("Now enter the names of the friends")
    for j in range(int(m)):
        friend = input("Enter the name: ")
        g.add_edge(list(g.nodes)[i], friend)

print("The graph has been created")
print("The graph is being displayed...")
print("To continue close the window")
# showing the graph
time.sleep(5)
app = networkx_viewer.Viewer(g)
app.mainloop()
# recommending friends
n = input("How many users do you want to find the friends for:")
for i in range(int(n)):
    user = input("Enter the name of the user: ")
    print("By common friends we can recommend the following friends for you: ", end="")
    cnt = 0
    for friend in recommendation.recommend_by_common_friends(g, user):
        if cnt == 5:
            break
        print(friend, end=", ")
        cnt += 1
    print()
    print("By friend influence we can recommend the following friends for you: ", end="")
    cnt = 0
    for friend in recommendation.recommend_by_influence(g, user):
        if cnt == 5:
            break
        print(friend, end=", ")
        cnt += 1
    print()

