from collections import defaultdict
def findItinerary(tickets):
    targets = defaultdict(list)
    for a, b in sorted(tickets)[::-1]:
        targets[a] += b,
    route, stack = [], ['JFK']
    print(targets)
    print(route)
    print(stack)
    while stack:
        while targets[stack[-1]]:
            stack += targets[stack[-1]].pop(),
        route += stack.pop(),
        print('---')
        print(route)
        print(stack)
    print(route[::-1])
    return route[::-1]

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
findItinerary(tickets)