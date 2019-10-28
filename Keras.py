import numpy as np
from keras.models import Sequential
from keras.layers.core import Dense, Activation
from keras import optimizers

# 1. create pseudo data y = 2*x0 + 3*x1 + 4
X = np.random.rand(100, 2)
y =  2* X[:,0] + 3 * X[:,1] + 4 + .2*np.random.randn(100) # noise added

# 2. Build model
model = Sequential([Dense(1, input_shape = (2,), activation='linear')])

# 3. gradient descent optimizer and loss function
sgd = optimizers.SGD(lr=0.1)
model.compile(loss='mse', optimizer=sgd)

# 4. Train the model
model.fit(X, y, epochs=100, batch_size=2)
