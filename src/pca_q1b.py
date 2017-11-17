import numpy as np
import matplotlib.pyplot as plt
from src.reader import fetch_data

SHAPE = (46, 56)

data = fetch_data()

X_train, y_train = data['train']

N = X_train.shape[0]

# mean face
mean_face = X_train.mean(axis=0)

plt.imshow(mean_face.reshape(SHAPE).T)
plt.savefig('data/out/mean_face_q1.eps', format='eps', dpi=1000)
plt.show()

A = X_train - mean_face

S = (1 / N) * np.dot(A.T, A)

# Calculate eigenvalues `w` and eigenvectors `v`
_w, _v = np.linalg.eig(S)

# Indexes of eigenvalues, sorted by value
_indexes = np.argsort(np.abs(_w))

# TODO
# threshold w's

# Sorted eigenvalues and eigenvectors
w = _w[_indexes]
v = _v[:, _indexes]

plt.plot(np.abs(w[::-1]))
plt.savefig('data/out/eigenvalues_q1b.eps', format='eps', dpi=1000)
