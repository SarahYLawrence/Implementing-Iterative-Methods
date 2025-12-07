import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D   # Needed for 3D plotting

# ---- Define 4 example matrices ----
A_posdef = np.array([[4, 1],
                     [1, 3]])            # Positive definite
A_negdef = -A_posdef                     # Negative definite
A_possemidef = np.array([[1, 0],
                         [0, 0]])         # Positive semidefinite
A_indef = np.array([[0, 1],
                    [1, 0]])             # Indefinite (saddle)

matrices = {
    "(a) Positive Definite": A_posdef,
    "(b) Negative Definite": A_negdef,
    "(c) Positive Semidefinite": A_possemidef,
    "(d) Indefinite": A_indef
}

# ---- Create grid for surface plot ----
x = np.linspace(-3, 3, 200)
y = np.linspace(-3, 3, 200)
X, Y = np.meshgrid(x, y)

# ---- Create 2x2 subplot figure ----
fig = plt.figure(figsize=(12,10))

for i, (title, M) in enumerate(matrices.items(), 1):
    ax = fig.add_subplot(2, 2, i, projection='3d')  # 2 rows, 2 columns
    Z = M[0,0]*X**2 + (M[0,1] + M[1,0])*X*Y/2 + M[1,1]*Y**2
    ax.plot_surface(X, Y, Z, color='orange', alpha=0.8, edgecolor='k') 
    ax.set_title(title)
    ax.set_xlabel("x")
    ax.set_ylabel("y")
    ax.set_zlabel("z = xᵀAx")

plt.tight_layout()  # adjust spacing so titles and labels don't overlap
plt.savefig("quadratic_forms.png", dpi=300, bbox_inches='tight')
plt.show()
