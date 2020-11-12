from keras.models import Sequential
from keras.layers import Dense

class TrainModel:
    def __init__(self, arg):
        if type(arg) is int:
            self.model = Sequential()
            n_data = arg
            self.model.add(Dense(int(n_data / 4), input_dim = n_data))
            self.model.add(Dense(3))

            self.model.compile(loss='categorical_crossentropy', optimizer = 'adam')
        else:
            import keras.models
            path = arg
            self.model = keras.models.load_model(path)

    def fit(self, input):
        for data, labels in input:
            self.model.fit(data, labels)

    def save(self, path):
        self.model.save(path)

    def test(self, input_test):
        for data, labels in input_test:
            r = self.model.evaluate([data], [labels])
            print(r)
