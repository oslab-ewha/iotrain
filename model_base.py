from keras.models import Sequential
from keras.layers import Dense
import conf

class TrainModelBase:
    def __init__(self, arg):
        if type(arg) is int:
            self.__build_model(arg)
        else:
            self.__load_model(arg)

    def __build_model(self, n_inputs):
        self.model = Sequential()
        self.setup_layers(n_inputs)
        self.model.add(Dense(3, activation='softmax'))

        self.model.compile(loss='categorical_crossentropy', optimizer = 'adam', metrics=['accuracy'])

    def setup_layers(self, n_inputs):
        pass

    def __load_model(self, path):
        import keras.models
        self.model = keras.models.load_model(path)

    def fit(self, input):
        for data, labels in input:
            self.model.fit([data], [labels], epochs=conf.epochs)

    def save(self, path):
        self.model.save(path)

    def test(self, input_test):
        for data, labels in input_test:
            r = self.model.evaluate([data], [labels])
            print(r)

    def predict(self, inputs):
        for data, labels in inputs:
            for i in range(0, len(data)):
                predicted = self.model.predict([[data[i]]])
                print(self.__to_readable_floats(labels[i]), self.__to_readable_floats(predicted[0]))

    def __to_readable_floats(self, floats):
        floats_readable = []
        for f in floats:
            floats_readable.append(round(f, 4))
        return floats_readable
