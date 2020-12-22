import sys, re, itertools

try:
    with open(sys.argv[1]) as file:
        raw = file.read()
except IndexError:
    raw = sys.stdin.read()

table = []

for line in raw.splitlines():
    m = re.match(r"([a-z ]+) \(contains ([a-z ,]+)\)", line)
    ingredients = m.group(1).split()
    allergens   = m.group(2).split(', ')
    table.append((ingredients, allergens))

all_allergens = {
    allergen
    for ingr_list, aller_list in table
    for allergen in aller_list
}

all_ingredients = {
    ingredient
    for ingr_list, aller_list in table
    for ingredient in ingr_list
}

candidates = {allergen: set(all_ingredients) for allergen in all_allergens}

for ingr_list, aller_list in table:
    for allergen in aller_list:
        candidates[allergen] &= set(ingr_list)

ruled_out_ingredients = all_ingredients - set.union(*candidates.values())

def count(ingredient):
    return sum(
        ingr_list.count(ingredient)
        for ingr_list, _ in table
    )

print("Ruled out ingredients:")
print('\n'.join(
    f"    {ing} occurs {count(ing)} times"
    for ing in ruled_out_ingredients
))

print(f"Total occurrences: {sum(count(ing) for ing in ruled_out_ingredients)}")

for i in range(100):
    for aller1, ingset1 in candidates.items():
        for aller2, ingset2 in candidates.items():
            if aller1 != aller2 and len(ingset1) == 1:
                ingset2 -= ingset1

contained_by = {aller: ing for aller, (ing,) in candidates.items()}

print()
print(f"Known allergens:")
print('\n'.join(
    f"    {aller} occurs in {ing}"
    for aller, ing in contained_by.items()
))

print("Dangerous ingredient list:", ','.join(
    contained_by[aller]
    for aller in sorted(all_allergens)
))

