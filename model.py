from keras.models import Sequential
from keras.layers import Dense

class TrainModel:
    def __init__(self, input):
        self.input = input
        self.model = Sequential()
        self.model.add(Dense(input.n_data, input_dim = input.n_data))
        self.model.add(Dense(3))

        self.model.compile(loss='categorical_crossentropy', optimizer = 'adam')
        self.model.summary()

    def fit(self):
        for data, labels in self.input:
            self.model.fit(data, labels)
