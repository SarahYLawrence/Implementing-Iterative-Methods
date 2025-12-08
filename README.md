# Implementing-Iterative-Methods
This project implements three iterative solvers for linear systems of the form

<h1 align="center">𝐴𝑥 = 𝑏</h1>

where A is a symmetric positive definite matrix and b is an n-dimensional vector.
Each method is implemented as a function that takes inputs (A, b) and returns the approximate solution and its residual history.
# Method 1: Conjugate Gradient
Conjugate Gradient solves Ax=b by generating A-conjugate search directions, ensuring efficient progress and typically converging in far fewer than n iterations.

# Method 2: GMRES
GMRES (Generalized Minimal Residual) builds a Krylov subspace and computes the solution that minimizes the residual norm at each step using least-squares over that subspace.

# Method 3: BiCGSTAB
BiCGSTAB (Bi-Conjugate Gradient Stabilized) is designed for general nonsymmetric matrices and improves stability by combining bi-conjugacy ideas with an additional smoothing step.

# Research Phase
This has all the LaTeX files for the project. 
Final_Latex_PDF has the final LaTeX pdf. Files include:
- 574_Masters_Project.pdf
Full_Latex_files has all of the raw LaTeX files. Files include: 
- bicgstab_residuals.png     -> gotten from "Project Code"
- cg_residuals.png           -> gotten from "Project Code"
- gmres_residuals.png        -> gotten from  "Project Code"
- main.tex
- Positive_definite.png      -> gotten from "Research Code"
- quadratic_forms.png        -> gotten from "Research Code"
- refs-style.bst
- refs.bib
All of the LaTeX is qriten in overleaf. 


