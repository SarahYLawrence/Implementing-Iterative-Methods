# Implementing-Iterative-Methods
---
This project implements three iterative solvers for linear systems of the form

<h1 align="center">𝐴𝑥 = 𝑏</h1>

where A is a symmetric positive definite matrix and b is an n-dimensional vector.
Each method is implemented as a function that takes inputs (A, b) and returns the approximate solution and its residual history.
# Method 1: Conjugate Gradient
---
Conjugate Gradient solves Ax=b by generating A-conjugate search directions, ensuring efficient progress and typically converging in far fewer than n iterations.

# Method 2: GMRES
---
GMRES (Generalized Minimal Residual) builds a Krylov subspace and computes the solution that minimizes the residual norm at each step using least-squares over that subspace.

# Method 3: BiCGSTAB
---
BiCGSTAB (Bi-Conjugate Gradient Stabilized) is designed for general nonsymmetric matrices and improves stability by combining bi-conjugacy ideas with an additional smoothing step.

# Code Phase
---
This has all the code files for the project 
project code:
- lauange: Julia
- Writen in: colab
Has all of the:
- methods
- plots
- numbers for final results

research code:
- lauange: python
has the examples of the
- diffrent matrix digram
- heatmap for the positive definite matrix

# Run
---
Run the project code:
Go to project code in colab and run the following inorder 
- function spd_matrix
- function conjugate_gradient
- function gmres_residuals
- function bicgstab_residuals

If you want to see the plots run the follwing after each function:
- using Plots

Results:
- bicgstab_residuals.png
- cg_residuals.png
- gmres_residuals.png

This will store the plots and display them.
If you want to see the evaluation run the follwing after each function
- Random.seed
- Then run the last three code blocks

Results:
- method resudials
- method time

---
To run the research code 
Open vscode
- Python 3.11.4 - was used for these experments
- pip install -r requirements.txt
- hit run
Results:
- Positive_definite.png
- quadratic_forms.png


