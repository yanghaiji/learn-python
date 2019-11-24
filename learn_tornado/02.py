# coding:utf-8
"""
异步实例
"""
import datetime
import tornado.web
import tornado.gen
import tornado.ioloop
import tornado.httpserver


class MainHandler(tornado.web.RequestHandler):

    @tornado.gen.coroutine
    def get(self):
        yield tornado.gen.sleep(10)
        self.write(str(datetime.datetime.now()))

if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r"/", MainHandler)
        ],
        debug=True
    )
    app.listen(8006)
    tornado.ioloop.IOLoop.current().start()

