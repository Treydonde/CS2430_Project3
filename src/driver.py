# This is a test driver for the following code in main.
#
# The driver will test for consistency with the program and make sure that we
# are getting the right output.  The input will be a tuple array with the input
# being [Item Name, Weight, Rating, dependency] this will be [String, int, int, String]
# To run all the functions we will be importing all the functions that we made in
# main.
#
# @author Benjamin Shaw

from main import (greedy_pack, highest_rating_first,
                  best_rating_to_weight_ratio, lightest_first, brute_force, EXPERIMENTS, CAPACITY)

def main():
    # these are the names of the greedy strategies
    names = [
        "Highest Rating First",
        "Lightest First",
        "Best Rating to Weight Ratio"
    ]
    # starting iterator at 0
    i = 0

    print(f"\n---------- Part 1 Greedy Strategies ----------------------------------------")

    # printing the experiments of the greedy strategies
    for items, load_weight, load_rating in (highest_rating_first(EXPERIMENTS, CAPACITY),
                                            lightest_first(EXPERIMENTS, CAPACITY),
                                            best_rating_to_weight_ratio(EXPERIMENTS, CAPACITY)):

        # printing the name of the strategy
        print(f"This is the {names[i]}:")

        # printing the organization for the experiments to be printed
        print("-------------------------------------------------")
        print(f"{"Item Name":<30} {"Weight":<10} {"Rating":<10}")
        print("-------------------------------------------------")

        # printing each individual experiment
        for item, weight, rating in items:
            print(f"{item:<30} {weight:<10} {rating:<10}")

        # printing the weight and rating of the greedy strategies payloads
        print(f"\nLoad Weight: {load_weight:<17} Load Rating: {load_rating}")
        print(f"\n")

        i += 1




    print(f"\n---------- Part 2 Brute Force ----------------------------------------------")

    # printing the experiments of brute force
    for rank, (load_rating, items) in enumerate(brute_force(EXPERIMENTS, CAPACITY), start=1):
      
        weight_of_brute_force = 0

        print("\n\n-------------------------------------------------")
        print(f"#{rank}" + ("  <-- OPTIMAL" if rank == 1 else ""))
        print(f"{"Item Name":<30} {"Weight":<10} {"Rating":<10}")
        print("-------------------------------------------------")

        # printing each individual experiment
        for item, weight, rating in items:
            print(f"{item:<30} {weight:<10} {rating:<10}")

            # getting the total weight of the brute force experiments
            weight_of_brute_force += weight

        # printing the weight and rating of the brute force payloads
        print(f"\nLoad Weight: {weight_of_brute_force:<17} Load Rating: {load_rating}")

    print(f"\n---------- Part 3 Comparison Summary ----------------------------------------")

    # Getting the rating and experiments of the optimal payload
    brute_force_optimal_rating, brute_force_optimal_experiments = brute_force(EXPERIMENTS, CAPACITY)[0]
    brute_force_optimal_weight = 0

    # getting the total weight of the optimal payload
    for name, weight, rating in brute_force_optimal_experiments: brute_force_optimal_weight += weight

    # this is to iterate through the names array
    i = 0

    print()
    print("-" * 70)
    print(f"{"Strategy":<30} {"Weight":<10} {"Rating":<10} {"Optimal?"}")
    print("-" * 70)

    # looking through all the payloads
    for items, load_weight, load_rating in (highest_rating_first(EXPERIMENTS, CAPACITY),
                                            lightest_first(EXPERIMENTS, CAPACITY),
                                            best_rating_to_weight_ratio(EXPERIMENTS, CAPACITY)):

        print(f"{names[i]:<30} {load_weight:<10} {load_rating:<10} {"Matches" if load_rating == brute_force_optimal_rating else f"Below by {brute_force_optimal_rating - load_rating}"}")

        i += 1

    # printing the optimal payload
    print(f"{"Brute Force Optimal":<30} {brute_force_optimal_weight:<10} {brute_force_optimal_rating:<10} {"-"}")

    # printing the summary
    print("\nSummary:")
    print(f"  The optimal payload has a total rating of {brute_force_optimal_rating} "
          f"at {brute_force_optimal_weight} kg.")

if __name__ == "__main__":
    main()
