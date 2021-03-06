# helper data preprocessor
from src.reader import fetch_data
# custom PCA transformer
from src.pca import PCA
# custom One-Versus-Rest SVM
from src.ovr import OVR

M = 121
standard = True

data = fetch_data(ratio=0.8)

X_train, y_train = data['train']

D, N = X_train.shape

pca = PCA(n_comps=M, standard=standard)

W_train = pca.fit(X_train)

X_test, y_test = data['test']
I, K = X_test.shape

W_test = pca.transform(X_test)

params = {'C': 1, 'gamma': 2e-4, 'kernel': 'linear'}

ovr = OVR(**params)
ovr.fit(W_train, y_train)
acc = ovr.score(W_test, y_test)
print('Accuracy = %.2f%%' % (acc * 100))
