from pickle import dump, load

CONFIG_FILENAME = 'conf.ini'

class Config:

    __instance = None

    def __init__(self, filename, **kwargs):
        if not ('vbfyd78bydf' in kwargs and 
                kwargs['vbfyd78bydf'] == 54263754637):
            raise Exception('Do not create Config manually. Use Config.get_instance()')

        self.filename = filename
        self.params = {}

    @classmethod
    def get_instance(cls):
        if not cls.__instance:
            cls.__instance = Config(CONFIG_FILENAME, vbfyd78bydf=54263754637)
        return cls.__instance


    def read(self):
        try:
            with open(self.filename, 'rb') as f:
                self.params = load(f)
        except FileNotFoundError:
            pass

    def write(self):
        with open(self.filename, 'wb') as f:
            dump(self.params, f)

    def __getattr__(self, name):
        return self.params.get(name, None)

    def __setattr__(self, name, value):
        if name in ('params', 'filename'):
            return super().__setattr__(name, value)
        self.params[ name ] = value

    # запускается при попытке удаления: del Config().some_param
    def __delattr__(self, name):
        pass


if __name__=='__main__':
    a = Config.get_instance()
    b = Config.get_instance()
    c = Config.get_instance()
    print(a, b, a == b == c)

    d = Config(filename='vfvd')
    print(a == d)