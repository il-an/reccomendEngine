import networkx as nx


def friends(graph: nx.Graph, user: str) -> set:
    """Returns the set of friends of a given user
    :param graph: graph
    :param user: user
    :return: set of friends of a given user
    """
    return set(graph.neighbors(user))


def friends_of_friends(graph: nx.Graph, user: str) -> set:
    """Returns friends of friends of a given user
    :param graph: graph
    :param user: user
    :return: set of friends of friends of a given user
    """
    user_friends = friends(graph, user)
    user_friends_of_friends = set()

    for friend in user_friends:
        user_friends_of_friends.update(friends(graph, friend) - user_friends)

    return user_friends_of_friends - {user}


def common_friends(graph: nx.Graph, user1: str, user2: str) -> set:
    """Returns the set of friends user1 and user2 share
    :param graph: graph
    :param user1: user1
    :param user2: user2
    :return: set of friends user1 and user2 share"""
    return friends(graph, user1).intersection(friends(graph, user2))


def number_of_common_friends_map(graph: nx.Graph, user: str) -> dict:
    """Returns a common friends map from the given user to every other user
    :param graph: graph
    :param user: user
    :return: common friends map
    """
    common_friends_map = {}
    user_friends = friends_of_friends(graph, user)

    for friend in user_friends:
        length = len(common_friends(graph, user, friend))
        if length >= 1:
            common_friends_map[friend] = length

    return common_friends_map


def number_map_to_sorted_list(friend_map: dict) -> list:
    """Returns the friend map as a sorted list
    :param friend_map: map
    :return: sorted list
    """
    return [v[0] for v in sorted(friend_map.items(), key=lambda kv: (-kv[1], kv[0]))]


def recommend_by_common_friends(graph: nx.Graph, user: str) -> list:
    """Returns a common friend list for the user
    :param graph: graph
    :param user: user
    :return: common friend list
    """
    return number_map_to_sorted_list(number_of_common_friends_map(graph, user))


def influence_map(graph: nx.Graph, user: str) -> dict:
    """Returns a map from each user (who has common friends with the given user) to the friend influence
    :param graph: graph
    :param user: user
    :return: friend influence map
    """
    user_friends_of_friends = friends_of_friends(graph, user)
    friend_influence_map = {}

    for friend in user_friends_of_friends:
        user_common_friends = common_friends(graph, user, friend)
        if len(user_common_friends) >= 1:
            friend_influence_map[friend] = sum([1 / len(friends(graph, val)) for val in user_common_friends])

    return friend_influence_map


def recommend_by_influence(graph: nx.Graph, user: str) -> list:
    """Returns a list of friend recommendations for the given user based on friend influence
    :param graph: graph
    :param user: user
    :return: friend recommendations list
    """
    return number_map_to_sorted_list(influence_map(graph, user))
