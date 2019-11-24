# coding:utf-8
"""
最简单的tornado实例
"""
import tornado.web
import tornado.ioloop
import tornado.httpserver


class MainHandler(tornado.web.RequestHandler):

    def get(self):
        self.write("Hello Tornado")


if __name__ == '__main__':
    app = tornado.web.Application(
        [
            (r"/", MainHandler)
        ]
    )
    app.listen(8003)
    tornado.ioloop.IOLoop.current().start()
