#!/usr/bin/env python3
import matplotlib.pyplot as plt
import networkx as nx

import recommendation

n = input("Enter the number of users: ")
if not n.isdigit():
    print("Not a number!")
    quit()

n = int(n)
if n <= 0:
    quit()

g = nx.Graph()
print("Now enter the names of the users")
# entering the nodes
for i in range(n):
    user = input("Enter the name: ")
    g.add_node(user)

n = len(g.nodes)
# entering the edges
for i in g.nodes.items():
    m = input(f"Enter the number of friends of {i[0]}: ")
    if not m.isdigit():
        print("Not a number!")
        quit()
    print("Now enter the names of the friends")
    for j in range(int(m)):
        friend = input("Enter the name: ")
        g.add_edge(i[0], friend)

print("The graph has been created")
print("The graph is being displayed...")
# showing the graph
nx.draw(g, with_labels=True)
plt.draw()
plt.show()

# recommending friends
n = input("How many users do you want to find the friends for: ")
if not n.isdigit():
    print("Not a number!")
    quit()
for i in range(int(n)):
    user = input("Enter the name of the user: ")
    if user not in g:
        print("Not in graph!")
        continue
    if not recommendation.recommend_by_common_friends(g, user):
        print("Could not recommend any friends for selected user!")
        continue
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
