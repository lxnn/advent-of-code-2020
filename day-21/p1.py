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
