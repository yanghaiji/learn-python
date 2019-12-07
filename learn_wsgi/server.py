# coding:utf-8
"""
desc: WSGI服务器实现
"""
from wsgiref.simple_server import make_server
from learn_wsgi.client import hello


def main():
    server = make_server('localhost', 8001, hello)
    print('Serving HTTP on port 8001...')
    server.serve_forever()


if __name__ == '__main__':
    main()
