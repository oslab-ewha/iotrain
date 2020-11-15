import conf

class ConfIotrain(conf.Conf):
    def __init__(self, usage):
        conf.epochs = 10
        conf.clearModel = False
        conf.width = 5
        conf.height = 10

        super().__init__('e:Cd:', usage)

    def handleOpt(self, o, a):
        if o == '-e':
            conf.epochs = int(a)
        elif o == '-C':
            conf.clearModel = True
        elif o == '-d':
            self.__parse_accbmp_dim(a)

    def __parse_accbmp_dim(self, dim):
        width, height = dim.split(sep='x', maxsplit=1)
        conf.width = int(width)
        conf.height = int(height)
