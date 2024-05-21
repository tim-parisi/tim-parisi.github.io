#!/usr/bin/python3

import tornado.ioloop
import tornado.options
import tornado.web

# Constants

PORT = 9999

# Handlers

class TestServer(tornado.web.RequestHandler):
    def get(self):
        
        self.render('homepage.html')
# Main Execution

def main():
    application = tornado.web.Application([
        (r'/', TestServer)
    ])

    application.listen(PORT)
    
    tornado.options.parse_command_line()

    tornado.ioloop.IOLoop.current().start()

if __name__ == '__main__':
    main()
