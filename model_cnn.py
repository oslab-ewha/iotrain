from keras.layers import Flatten
from keras.layers import Conv2D
from keras.layers import Dense
from model_base import TrainModelBase
import conf

class TrainModelCNN(TrainModelBase):
    def __init__(self, arg):
        super().__init__(arg)

    def setup_layers(self, n_inputs):
        kernel_width = int(conf.width / 2)
        kernel_height = int(conf.height / 2)
        n_filters = int(n_inputs/10)
        self.model.add(Conv2D(n_filters, kernel_size = (kernel_width, kernel_height),
                              input_shape=(conf.width, conf.height, 1), activation='relu'))
        self.model.add(Flatten())
        self.model.add(Dense(n_filters * 2, activation='relu'))
