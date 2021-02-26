'''
作者：PegasusWang
链接：https://zhuanlan.zhihu.com/p/46147994
来源：知乎
著作权归作者所有。商业转载请联系作者获得授权，非商业转载请注明出处。
'''

# server.py
import random

import tornado.ioloop
import tornado.web
from tornado import gen
from tornado.web import RequestHandler


class AsyncSleepHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        yield gen.sleep(random.random()/10.0)
        self.write('sleep')


class Async2SleepHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        yield gen.sleep(random.random()/10.0*2)
        self.write('sleep')

class AsyncHomeHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        yield gen.sleep(random.random()/10.0*3)
        self.write('home.html')

class AsyncStatHandler(RequestHandler):
    @gen.coroutine
    def get(self):
        yield gen.sleep(random.random()/10.0*3)
        self.write('stats page')


if __name__ == "__main__":
    application = tornado.web.Application([
        (r"/sleep", AsyncSleepHandler),
        (r"/sleep2", Async2SleepHandler),
        (r"/", AsyncHomeHandler),
        (r"/stats/requests", AsyncStatHandler),
    ], debug=1)

#        (r"/double_wave", Async3SleepHandler)

    application.listen(8888)
    try:
        tornado.ioloop.IOLoop.current().start()
    except KeyboardInterrupt:
        tornado.ioloop.IOLoop.current().stop()
