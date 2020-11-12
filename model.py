from keras.models import Sequential
from keras.layers import Dense
import conf

class TrainModel:
    def __init__(self, arg):
        if type(arg) is int:
            self.__build_model(arg)
        else:
            self.__load_model(arg)

    def __build_model(self, n_inputs):
        self.model = Sequential()
        self.model.add(Dense(int(n_inputs / 4), input_dim = n_inputs, activation=None))
        self.model.add(Dense(3))

        self.model.compile(loss='categorical_crossentropy', optimizer = 'adam', metrics=['accuracy'])

    def __load_model(self, path):
        import keras.models
        self.model = keras.models.load_model(path)
        
    def fit(self, input):
        for data, labels in input:
            self.model.fit(data, labels, epochs=conf.epochs)

    def save(self, path):
        try:
            self.model.save(path)
        except:
            print("exception")

    def test(self, input_test):
        for data, labels in input_test:
            r = self.model.evaluate([data], [labels])
            print(self.model.metrics_names)
            print(r)
