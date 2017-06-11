#!/usr/bin/env python
# coding=utf-8

import tornado.ioloop, logging
import tornado.web
from tornado import gen, escape
import json
from tornado.httpclient import AsyncHTTPClient
from inventory import *
import json
from summarizer import generate


log = logging.getLogger(__name__)
logging.basicConfig(format='%(levelname)s - %(asctime)s - %(message)s', level=logging.DEBUG)

class Frontend(tornado.web.RequestHandler):
    @gen.coroutine
    def get(self, query):
        query = self.get_argument("q")
        query = query.lower()
        inputs = query.split()
        try:
            res = generate(inputs)
        except:
            res = "generation error"
        ans = {'results': res}
        self.finish(json.dumps(ans))

if __name__ == "__main__":
    application = tornado.web.Application([
                (r'/([^/]*)', Frontend),
            
    ])
    application.listen(BASE_PORT)
    log.info('Front end is listening on %d', BASE_PORT)
    tornado.ioloop.IOLoop.current().start()
