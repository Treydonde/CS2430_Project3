def greedy_pack()
  takes experiments and sort key as params
  iterates through the experiments and sorts them based
  on whatever param is passed as the sort key

def highest rating first
  calls greedy_pack() and passes a sort key that sorts
  by science rating. returns this sorted tuple

def best rating to weight ratio
  takes experiment and capacity as params
  calculates the weight:rating ratio for all experiments 
  sorts and iterates through all of them adding the best ratio

def brute force
  generates all permutations of subsets of experiments
  discards all subsets where weight > 700
  for remaining values sums the rating value
  returns the top three subsets and their rating 

def main
  calls all our functions, formats the results and prints them
