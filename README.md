# Optimal Selection

## Overview

This project demonstrates how algorithm design can transform abstract mathematical reasoning into practical decision-making tools. You will implement, compare, and critically evaluate multiple algorithmic strategies to solve the classic knapsack optimization problem. We often run into problems where we have a finite amount of one or more resources and must find the best possible solution given our constraints.

# Features

## Greedy Algorithms:
Three greedy strategies are used in this project and each one sorts by a single rule: 

- **Highest Rating**
- **Lightest Weight** 
- **Best Rating-per-kg** 

It then keeps adding items in that each those respective rules so long as they fit the condition. The idea is to show greedy algorithms makes choices that on a local level look like the best at each step and never reconsiders whether or not it is the most optimal in the grander scheme of things. The algorithm is not meant to look ahead to whether a different combination would score higher overall.

## Brute Forcing
This checks all 4096 possible subsets, guaranteeing us to find the true optimum. This brute force strategy acts as the most definitive answer that can be used to compare/grade the greedy results against. 

# Comparison
The main part of the project after implementing the greedy strategies and brute force method. Showing us which greedy rules landed the closest to the optimum and which ones fell short.



# Project Structure

```text
CS2430_Project3/
├── src/
│   ├── project_driver.py
│   └── main.py
├── docs/
│   ├── Blank diagram (1).png
│   └── ProjectPlan.md
│   └── Pseudo-Code.md
└── .gitignore
└── README.md
```

## Requirements

- Python 3.10 or newer recommended.
- No third-party Python packages are required.

## How to Run

Clone or download the repository and open a terminal in the project root directory.

### Run the demonstration

```bash
python main.py
```

### Run the test driver

```bash
python src/project_driver.py
```

The test driver checks the results of the implemented operations against predefined expected results.

## Testing Results

The test driver was executed with the following result:

```text

```

## Learning Objectives
