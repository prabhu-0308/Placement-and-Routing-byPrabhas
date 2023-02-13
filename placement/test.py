from solver import Solver
from visualizer import Visualizer
from problem import Problem

# Define a problem
problem = Problem(rectangles=[
    [1, 1, 2],  # Format: [width, height] as list. Default rotatable: False
    [1, 1, 8]
])
print("problem:", problem)

# Find a solution
print("\n=== Solving without width/height constraints ===")
solution = Solver().solve(problem=problem)
print("solution:", solution)

# Visualization (to floorplan.png)
Visualizer().visualize(solution=solution, path="./figs/floorplan.png")

# [Other Usages]
# We can also give a solution width (and/or height) limit, as well as progress bar and random seed
print("\n=== Solving with width/height constraints ===")
solution = Solver().solve(problem=problem, seed=1111)
print("solution:", solution)
Visualizer().visualize(solution=solution, path="./figs/floorplan_limit.png")
