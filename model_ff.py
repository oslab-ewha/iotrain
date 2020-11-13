from keras.layers import Dense
from model_base import TrainModelBase

class TrainModelFF(TrainModelBase):
    def __init__(self, arg):
        super().__init__(arg)

    def setup_layers(self, n_inputs):
        self.model.add(Dense(int(n_inputs / 4), input_dim = n_inputs, activation='relu'))
