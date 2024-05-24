#!/usr/bin/python3

import tornado.ioloop
import tornado.options
import tornado.web

# Constants

PORT = 9999

# Handlers

class IndexHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('index.html')
class TestProjectHandler(tornado.web.RequestHandler):
    def get(self):
        self.render('testproject.html')

# Main Execution

def main():
    application = tornado.web.Application([
        (r'/', IndexHandler),
        (r'/index.html', IndexHandler),
        (r'/testproject.html', TestProjectHandler),
        (r"/static/(.*)", tornado.web.StaticFileHandler, {
        "photo_path": "./photos" ,
        "template_path": "./templates"
        }),

    ])

    application.listen(PORT)
    print(f'Listening on port {PORT}')
    tornado.options.parse_command_line()

    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
