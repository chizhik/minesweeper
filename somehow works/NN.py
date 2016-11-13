from keras.models import Model, Sequential
from keras.layers import Convolution2D, Flatten, Dense, Input
from keras import backend as K
import keras.callbacks
import numpy as np


class NN:
    def __init__(self, bsize = (4, 4), gamma = 0.99):
        self.model = Sequential()
        self.model.add(Dense(250, activation='relu', init='uniform', input_dim=250))
        self.model.add(Dense(250, activation='relu', init='uniform'))
        #self.model.add(Dense(100, activation='linear', init='uniform'))
        self.model.add(Dense(1, activation='sigmoid', init='uniform'))
        opt = keras.optimizers.Adam(lr=0.001)
        self.model.compile(loss='mean_squared_error', optimizer=opt)
        self.model.summary()
        #self.tb = keras.callbacks.TensorBoard(log_dir='/tmp/NN/logs', write_graph=True)
        self.bsize = bsize
        self.gamma = gamma

    def predict(self, state):
        q = self.model.predict(state)
        return q

    def train(self, x, y):
        #self.model.train_on_batch(x, y)
        self.model.fit(x, y, nb_epoch=1)#, callbacks=[self.tb])

    def save(self, fpath = 'model.hdf'):
        self.model.save_weights(fpath)

    def load(self, fpath = 'model.hdf'):
        self.model.load_weights(fpath, by_name = False)