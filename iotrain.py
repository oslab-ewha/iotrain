#!/usr/bin/python3

import logger
from conf import Conf

def __usage_iotrain():
    print("""\
Usage: iotrain.py [<options>] <path>
  <options>
   -h: help(this message)
""")

class IoTrain:
    def goTrain(self, conf):
        from input import Input
        from model import TrainModel

        input = Input(3, 100)
        input.load(conf.path)

        model = TrainModel(input)
        model.fit()
        exit(1)

if __name__ == "__main__":
    import iotrain

    logger.init("iotrain")

    it = iotrain.IoTrain()

    exit(it.goTrain(Conf("", __usage_iotrain)))


