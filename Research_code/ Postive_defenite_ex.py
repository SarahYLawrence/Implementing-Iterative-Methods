import numpy as np
import matplotlib.pyplot as plt
import numpy as np
import scipy.sparse as sp
import matplotlib.pyplot as plt

fig, axs = plt.subplots(1, figsize=(5, 4))

# Positive definite example
B = np.random.randn(20, 20)
B = B.T @ B
axs.imshow(B, cmap="Oranges")
axs.set_title("Positive Definite Matrix")


# # Sparse matrix example
# S = sp.rand(20, 20, density=0.05)
# # axs[1].spy(S, markersize=8)
# axs[1].imshow(S.toarray(), cmap="pink")
# axs[1].set_title("Sparse Matrix")


plt.savefig("Positive_definite.png", dpi=300, bbox_inches='tight')
plt.show()
