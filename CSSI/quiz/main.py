import webapp2
import jinja2
import os

env = jinja2.Environment(
    loader = jinja2.FileSystemLoader(os.path.dirname(__file__))
)

class Quiz(webapp2.RequestHandler):
    def get(self):
        template = env.get_template("templates/quiz.html")
        self.response.write(template.render())

class Results(webapp2.RequestHandler):
    def post(self):
        template = env.get_template("templates/result.html")
        templateVars = {
            "question1" : self.request.get("question1"),
            "name" : self.request.get("name")
        }
        self.response.write(template.render(templateVars))

app = webapp2.WSGIApplication([
    ("/", Quiz),
    ("/result", Results),
], debug=True)
