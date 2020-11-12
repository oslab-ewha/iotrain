#!/usr/bin/python3

import os
import logger
from conf_it import ConfIotrain
import conf

def __usage_iotrain():
    print("""\
Usage: iotrain.py [<options>] <path>
  <options>
   -h: help(this message)
   -e <epochs>
   -C: clear an existing model if any
   -m <model file>
""")

class IoTrain:
    def goTrain(self):
        from input_train import InputTrain
        from input_test import InputTest
        from model import TrainModel

        input = InputTrain(3, 0)
        input.load(conf.path)

        if not conf.clearModel and os.path.exists(conf.path_model):
            model = TrainModel(conf.path_model)
        else:
            model = TrainModel(input.n_data)
        model.fit(input)

        if not conf.path_model is None:
            model.save(conf.path_model)

if __name__ == "__main__":
    import iotrain

    logger.init("iotrain")

    it = iotrain.IoTrain()

    ConfIotrain(__usage_iotrain)
    exit(it.goTrain())
