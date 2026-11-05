CAPACITY = 700


## List: Item Name, Weight, Rating.
EXPERIMENTS = [
    ("Cloud Patterns", 36, 5),
    ("Solar Flares", 264, 9),
    ("Solar Power", 188, 6),
    ("Binary Stars", 203, 8),
    ("Seed Viability", 7, 4),
    ("Sun Spots", 90, 2),
    ("Mice Tumors", 65, 8),
    ("Microgravity Plant Growth", 75, 5),
    ("Micrometeorites", 170, 9),
    ("Cosmic Rays", 80, 7),
    ("Cosmic Rays", 10, 5, ),
    ("Yeast Fermentation", 27, 4),
]

def main():
    print("This is the best rating to weight:")
    for item in best_rating_to_weight_ratio(EXPERIMENTS, CAPACITY): print(item)


# best_rating_to_weight_ratio gets the best rating to weight ratio of the
# given experiments and capacity.  The experiments are given as an array
# of tuples and the capacity they are laid out as follows:
# experiment: (experiment_name, weight, rating)...
# capacity: int
#
# @param experiments
# @param capacity
# @return picked_experiments
# @author Benjamin Shaw
def best_rating_to_weight_ratio(experiments, capacity):

    # Gets best rating to weight of the experiments
    best_rating_to_weight = [(rating / weight) for item_name, weight, rating in experiments]

    # sorts the best rating to weight experiments
    sorted_best_rating_to_weight, sorted_experiments = (
        zip(*sorted(zip(
            best_rating_to_weight, experiments.copy()), reverse=True)))


    # Both of these variables are being initialized before we run the for loop to
    # get the best rating to weight for the experiments
    total_weight = 0
    picked_experiments = []


    # This for loop iterates through all the sorted experiments to pick the best
    # experiments to have the best rating to weight ratio
    for item, weight, rating in sorted_experiments:

        if total_weight + weight <= capacity:
            picked_experiments.append((item, weight, rating))
            total_weight += weight

    return picked_experiments



if __name__ == "__main__":
    main()