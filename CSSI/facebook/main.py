import webapp2
import jinja2
import os

from google.appengine.ext import ndb

class Message(ndb.Model):
    text = ndb.StringProperty()
    name = ndb.StringProperty()
    created_time = ndb.DateTimeProperty(auto_now_add=True)

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        message_query = Message.query()
        message_query = message_query.order(Message.created_time)
        messages = message_query.fetch()
        TemplateVars = {
            "messages" : messages
        }
    def post(self):
        text = self.request.get("text")
        name = self.request.get("name")
        stuff = Message(text=text, name=name)
        stuff.put()
        template = env.get_template("templates/wall.html")
        self.response.write(template.render(TemplateVars))
class 
app = webapp2.WSGIApplication([
    ("/", MainPage),
], debug=True)
