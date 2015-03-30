import tornado
from tornado.web import url
# from context.handlers.root import Root
from context.handlers.feedback import Feedback
from context.handlers.root import Root
from context.handlers.status import Status
from context.contextualizer import Contextualizer
__author__ = 'robdefeo'


class Application(tornado.web.Application):
    def __init__(self):
        handlers = [
            url(r"/", Root, dict(contextualizer=Contextualizer()), name="root"),
            url(r"/feedback", Feedback, name="feedback"),
            url(r"/status", Status, name="status")
        ]

        settings = dict(
            # static_path = os.path.join(os.path.dirname(__file__), "static"),
            # template_path = os.path.join(os.path.dirname(__file__), "templates"),
            debug=tornado.options.options.debug,
        )
        tornado.web.Application.__init__(self, handlers, **settings)