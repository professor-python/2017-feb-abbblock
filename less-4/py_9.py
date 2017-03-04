import tornado.ioloop
import tornado.web

from os import listdir
from os.path import getsize, join

class MainHandler(tornado.web.RequestHandler):

    def get(self):
        path = self.get_argument('path', '.') # так получаем атрибуды запроса

        filenames = listdir(path)
        sizes = { fi : getsize(join(path, fi)) for fi in filenames }

        html = ''
        for fi, size in sizes.items():
            html += f'<p><b>{fi}</b>: {size}</p>'

        self.write(html)

    def post(self): # для запроса типа POST
        pass

def make_app():
    return tornado.web.Application([
        (r"/", MainHandler),
    ])

if __name__ == "__main__":
    app = make_app()
    app.listen(8888)
    tornado.ioloop.IOLoop.current().start()