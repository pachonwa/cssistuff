import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class Email(object):
    def __init__(self, subject, sender, content, image):
        self.subject = subject
        self.sender = sender
        self.content = content
        self.image = image


emails = [
    Email("Test1", "ciera@google.com", "This is the first test email.", "phoebebird.jpg"),
    Email("Test2", "ciera@google.com", "Second Test", "night.jpg"),
    Email("Another", "ciera@google.com", "Final Test", "water.jpg"),
]

class ListEmails(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/list_emails.html")
        templateVars = {
            "emails" : emails
        }
        self.response.write(template.render(templateVars))


class ViewEmail(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/view_emails.html")
        subject = self.request.get("subject")
        sender = self.request.get("sender")
        content = self.request.get("content")
        image = self.request.get("image")
        templateVars = {
            "subject" : subject,
            "sender" : sender,
            "content" : content,
            "image" : image,
        }
        self.response.write(template.render(templateVars))


app = webapp2.WSGIApplication([
    ("/", ListEmails),
    ("/email", ViewEmail),
], debug=True)
