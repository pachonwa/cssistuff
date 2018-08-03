import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class MainPage(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/start.html")
        self.response.write(template.render())

class JumpIn(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/jumpin.html")
        self.response.write(template.render())

class Run(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/run.html")
        self.response.write(template.render())

class Ignore(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/ignore.html")
        self.response.write(template.render())

class Call(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/call.html")
        self.response.write(template.render())

class RanOver(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/ranover.html")
        self.response.write(template.render())

class Hide(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/hide.html")
        self.response.write(template.render())

class Accept(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/accept.html")
        self.response.write(template.render())

class Reject(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/reject.html")
        self.response.write(template.render())

app = webapp2.WSGIApplication([
    ("/", MainPage),
    ("/jumpin", JumpIn),
    ("/run", Run),
    ("/ignore", Ignore),
    ("/call", Call),
    ("/hide", Hide),
    ("/reject", Reject),
    ("/accept", Accept)
], debug=True)
