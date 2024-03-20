# SVD

Automated, data files and images are saved to local folder

# Gauss-Jacobi, Gauss-Seidel, and Conjugate Gradient Algorithms

The user is prompted to enter

m to produce a matrix of ones of size mxm,

a constant to populate the diagonals d\_{ii},

and 0, 1, or 2 to indicate whether they'd like to run the Jacobi, Gauss-Seidel, or Conjugate Gradient Algorithm respectively.

for each user input, the converging algorithms will produce a csv in the local directory with the naming convention:
"Errors\_" + AlgorithmName + "\_D=" + D + ".csv"

In addition, the converging algorithm will be plotted and saved to the local direcorty with the naming convention:
"errors_D=" + D + ".jpg"

## Code Description

Question parts are labeled in the comments on the driver file
Inputs and Outputs are labeled in the corresponding function file

Note: by default, the Conjugate Gradient Algorithm is without preconditioning, there is another function "ConjugateGradientpc" used to compute the Conjugate Gradient algorithm with preconditioning.

Note2: The final bullet points of b1 and b2 are commented out for clarity. b1 is listed as lines 71-84, and b2 is listed as lines 87-99
