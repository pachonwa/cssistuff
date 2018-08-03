import webapp2
import jinja2
import os

import logging

from google.appengine.api import users
from google.appengine.ext import ndb

class Message(ndb.Model):
    email = ndb.StringProperty()
    content = ndb.StringProperty()
    created_time = ndb.DateTimeProperty(auto_now_add = True)

env = jinja2.Environment(
    loader=jinja2.FileSystemLoader(os.path.dirname(__file__)),
    extensions=['jinja2.ext.autoescape'],
    autoescape=True)

class MainPage(webapp2.RequestHandler):
    def get(self):
        logging.info("This is the main handler")
        login_url =""
        logout_url = ""
        #The current user will be a user object or None.
        current_user = users.get_current_user()

        #If no one is logged in, show a login prompt.
        if not current_user:
            login_url = users.create_login_url("/")
        else:
            logout_url = users.create_logout_url("/")

        message_query = Message.query()
        message_query = message_query.order(-Message.created_time)
        messages = message_query.fetch()


        TemplateVars = {
            "current_user" : current_user,
            "login_url" : login_url,
            "logout_url" : logout_url,
            "messages" : messages,

        }
        template = env.get_template('templates/guestbook.html')
        self.response.write(template.render(TemplateVars))
    def post(self):
        #1. Get information from the request
        content = self.request.get("content")
        current_user = users.get_current_user()
        email = current_user.email()

        #2. Read or write to the database
        message = Message(content=content, email=email)
        message.put()


        #3. Render a response
        self.redirect("/")

app = webapp2.WSGIApplication([
    ('/', MainPage),
], debug=True)
