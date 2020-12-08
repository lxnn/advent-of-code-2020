import sys, re, collections, pprint

GRAPH = collections.defaultdict(set)

with open(sys.argv[1]) as file:
    for line in file:
        container, _, contained = line.partition(' bags contain ')
        if contained == 'no other bags.':
            pass
        else:
            GRAPH[container] = set(
                re.findall(r"[0-9]+ ([a-z ]+?) bags?[.,]", contained)
            )

REVERSE_GRAPH = collections.defaultdict(set)
for key, values in GRAPH.items():
    for value in values:
        REVERSE_GRAPH[value].add(key)

start = 'shiny gold'
visited = {start}
frontier = [start]

while frontier:
    node = frontier.pop()
    unvisited_containers = REVERSE_GRAPH[node] - visited
    frontier.extend(unvisited_containers)
    visited |= unvisited_containers

print(len(visited) - 1)

