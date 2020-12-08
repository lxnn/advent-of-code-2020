import sys, re, collections, pprint

GRAPH = collections.defaultdict(dict)

with open(sys.argv[1]) as file:
    for line in file:
        container, _, contained = line.partition(' bags contain ')
        if contained == 'no other bags.':
            pass
        else:
            GRAPH[container] = {
                kind: int(num)
                for num, kind in re.findall(
                    r"([0-9]+) ([a-z ]+?) bags?[.,]",
                    contained
                )
            }

def total_bags(bag):
    return 1 + sum(
        num * total_bags(container)
        for container, num in GRAPH[bag].items()
    )

print(total_bags('shiny gold') - 1)
