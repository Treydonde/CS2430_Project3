CAPACITY = 700

EXPERIEMENTS = [
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
    ("Yeast Fermentation", 27, 4),
]

def greedy_pack(experiments, capacity, sort_key):
    """Go through experiements in sort_key order, adding each one or anything that still fits
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

    
def highest_rating_first(experiements, capacity=CAPACITY):
    # Showing the higest rating first with ties being broken by the lighther weight
    return greedy_pack(experiements, capacity, sort_key=lambda e: (-e[2], e[1]))


if __name__ == "__main__":
    main()