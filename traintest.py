#!/usr/bin/python3

import logger
import conf

def __usage_traintest():
    print("""\
Usage: traintest.py [<options>] <path>
  <options>
   -h: help(this message)
   -m <model file>
""")

class TrainTest:
    def testTrain(self):
        from input_test import InputTest
        from model import TrainModel

        model = TrainModel(conf.path_model)

        input_test = InputTest(3, 100)
        input_test.load(conf.path)
        model.test(input_test)

if __name__ == "__main__":
    import traintest

    logger.init("testtrain")

    tt = traintest.TrainTest()
    conf.Conf("", __usage_traintest)
    exit(tt.testTrain())
