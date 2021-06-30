population = [int(x) for x in input().split(", ")]
minimum_wealth = int(input())
no_way_distribution = False

for wealth in range(len(population)):
    if no_way_distribution:
        break
    max_wealth = max(population)
    index_max_wealth = population.index(max_wealth)
    if population[wealth] < minimum_wealth:
        diff = minimum_wealth - population[wealth]
        population[wealth] += diff
        population[index_max_wealth] -= diff
    if population[index_max_wealth] < minimum_wealth:
        no_way_distribution = True
        print("No equal distribution possible")
        break

if not no_way_distribution:
    print(population)
