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
        import input
        import model

        input = input.load()
        model_test = model.create(input)
        model_test.test(input)

if __name__ == "__main__":
    import traintest

    logger.init("testtrain")

    tt = traintest.TrainTest()
    conf.Conf("", __usage_traintest)
    exit(tt.testTrain())
