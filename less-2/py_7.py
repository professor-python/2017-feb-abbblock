from pickle import dump, load

class Config:

    def __init__(self, filename):
        self.filename = filename
        self.params = {}

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

    config = Config(filename='my_config.pickle')
    config.read()
    print( 'main_color:', config.main_color )

    config.main_color = '#ff0000'
    config.write()

    # ДЗ: 
    # 1. в setattr проверять на равенство
    # 2. в класс Config добавляем техническое свойство "changed"
    # 3. Запись в файл происходит только при "changed" == True


