# CVRP (Capacitated Vehicle Routing Problem) with Disruption Points (DP)

## Description
This project implements a solution approach for the Capacitated Vehicle Routing Problem (CVRP) with an added complexity of disruption points using dynamic programming (DP) to optimize routes, considering both demand satisfaction and disruption risks.

The script includes two main parts:
- `CVRPDP`: A class implementing the dynamic programming approach for solving the CVRP with disruption points.
- `experim - CVRPDP`: A script to run experiments using the `CVRPDP` class.

## Features
- Optimization of vehicle routes for demand satisfaction under capacity constraints.
- Incorporation of disruption risks in the routing problem.
- Use of dynamic programming for efficient computation.

## Requirements
- Python
- SciPy
- NumPy
- Matplotlib (for plotting results)

## Usage
To use this script, you will need to:
1. Define the problem parameters including the number of nodes, demand and values at each node, vehicle capacity, and incident matrix.
2. Create an instance of the `INPUT` class with these parameters.
3. Initialize an instance of the `CVRPDP` class with the `INPUT` instance.
4. Call the `DP()` method to solve the CVRP with the given parameters.
5. Optionally, execute the provided experimental script to run multiple scenarios and visualize the probability of demand satisfaction.

## Example
```python
data = INPUT()
ans = CVRPDP(data)
print(ans.DP())
 
