#!/usr/bin/python3

import logger
from conf import Conf

def __usage_iotrain():
    print("""\
Usage: iotrain.py [<options>] <path>
  <options>
   -h: help(this message)
   -m <model file>
""")

class IoTrain:
    def goTrain(self, conf):
        from input_train import InputTrain
        from input_test import InputTest
        from model import TrainModel

        input = InputTrain(3, 100)
        input.load(conf.path)

        model = TrainModel(input.n_data)
        model.fit(input)

        if not conf.path_model is None:
            model.save(conf.path_model)

if __name__ == "__main__":
    import iotrain

    logger.init("iotrain")

    it = iotrain.IoTrain()

    exit(it.goTrain(Conf("", __usage_iotrain)))


