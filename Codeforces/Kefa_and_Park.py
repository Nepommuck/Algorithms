# https://codeforces.com/problemset/problem/580/C


def restaurants_to_visit(vertex, cats_at_the_moment, children, cat_at, max_cats):
    cats_at_the_moment += cat_at[vertex]
    if cats_at_the_moment > max_cats:
        return 0

    # We arrived succesfully at the restaurant
    if len(children[vertex]) == 0:
        return 1

    # The journey is not yet finished
    if cat_at[vertex] == 0:
        cats_at_the_moment = 0
    res = 0
    for child in children[vertex]:
        res += restaurants_to_visit(child, cats_at_the_moment, children, cat_at, max_cats)
    return res


def remove_parents_from_neibours(vertex, parent, neibours):
    if parent is not None:
        neibours[vertex].remove(parent)
    for child in neibours[vertex]:
        remove_parents_from_neibours(child, vertex, neibours)


if __name__ == "__main__":
    n, max_cats = [int(x) for x in input().split()]
    cat_at = [int(x) for x in input().split()]
    neibours = [[] for _ in range(n)]

    for _ in range(n - 1):
        a, b = [int(x) - 1 for x in input().split()]
        neibours[a].append(b)
        neibours[b].append(a)

    remove_parents_from_neibours(0, None, neibours)
    print(restaurants_to_visit(0, 0, neibours, cat_at, max_cats))
