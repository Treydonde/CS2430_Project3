## List: Item Name, Weight, Rating.
import itertools
import heapq

CAPACITY = 700

EXPERIMENTS = [
    ("Cloud Patterns", 36, 5),
    ("Solar Flares", 264, 9),
    ("Solar Power", 188, 6),
    ("Binary Stars", 203, 8),
    ("Relativity", 104, 8),
    ("Seed Viability", 7, 4),
    ("Sun Spots", 90, 2),
    ("Mice Tumors", 65, 8),
    ("Microgravity Plant Growth", 75, 5),
    ("Micrometeorites", 170, 9),
    ("Cosmic Rays", 80, 7),
    ("Cosmic Rays", 10, 5,),
    ("Yeast Fermentation", 27, 4),
]

def main():
    print("This is the best rating to weight:")
    for item in best_rating_to_weight_ratio(EXPERIMENTS, CAPACITY): print(item)


def greedy_pack(experiments, capacity, sort_key):
    """Go through experiments in sort_key order, adding each one or anything that still fits
    This is essentially the greedy algorithm, because we are sorting by sort_key order which sets
    the priority order, walks through that order, does it know it's ideal? No, but it should be fast and simple
    """
    chosen = []
    total_weight = 0
    total_rating = 0
    for name, weight, rating in sorted(experiments, key=sort_key):
        if total_weight + weight <= capacity:
            chosen.append((name, weight,rating))
            total_weight += weight
            total_rating += rating

    return chosen, total_weight, total_rating

    
def highest_rating_first(experiments, capacity=CAPACITY):
    # Showing the highest rating first with ties being broken by the lighter weight
    return greedy_pack(experiments, capacity, sort_key=lambda e: (-e[2], e[1]))

# best_rating_to_weight_ratio gets the best rating to weight ratio of the
# given experiments and capacity.  The experiments are given as an array
# of tuples and the capacity they are laid out as follows:
#
# experiment: (experiment_name, weight, rating)...
# capacity: int
#
# @param experiments
# @param capacity
# @return picked_experiments
# @author Benjamin Shaw
def best_rating_to_weight_ratio(experiments, capacity=CAPACITY):

    # Gets best rating to weight of the experiments rating/weight first, ties broken by higher rating
 
    return greedy_pack(experiments, capacity, sort_key=lambda e:(-e[2]/e[1], -e[2]))

def lightest_first(experiments, capacity=CAPACITY):
    # Select experiments starting with the lightest ones then sorting by weight in ascending order.
    return greedy_pack(experiments, capacity, sort_key=lambda e: e[1])

# Brute force function
# Generates the powerset of EXPERIMENTS, calculates the weight and sum
# for every generated subset. Ignores the subset if the weight is > WEIGHT
# If the weight is < WEIGHT it uses heappush to keep track of the highest rating
#
def brute_force(experiments, capacity=CAPACITY):
    top_three = []
    num_results = 3 # used to limit result list to just 3 values

    # start at 1 to ignore starting empty combination
    for r in range(1, len(experiments) + 1):
        #generates all combinations of experiments of length r
        for subset in itertools.combinations(experiments, r):
            has_solar_flare = any(experiment[0] == "Solar Flares" for experiment in subset)
            has_solar_power = any(experiment[0] == "Solar Power" for experiment in subset)
            has_sun_spots = any(experiment[0] == "Sun Spots" for experiment in subset)
            has_seed_viability = any(experiment[0] == "Seed Viability" for experiment in subset)
            has_yeast_fermentation = any(experiment[0] == "Yeast Fermentation" for experiment in subset)

            #Checks if for forbidden combination "Shared Solar Instruments Hardware Contention"
            if has_solar_flare and has_solar_power and has_sun_spots:
                continue

            weight = sum(exp[1] for exp in subset)
            if has_seed_viability and has_yeast_fermentation:
                weight = weight - 7
            if weight > capacity:
                continue

            total_rating = sum(exp[2] for exp in subset)

            # pushes a tuple of the summed rating of the subset and the subset
            # onto a heap while retaining sorting
            # keeping the sort while pushing and then popping if len > 3
            #gives us the top 3 best
            heapq.heappush(top_three, (total_rating, subset))
            if len(top_three) > num_results:
                heapq.heappop(top_three)

    return sorted(top_three, reverse=True)

if __name__ == "__main__":
    main()
