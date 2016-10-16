from wtforms import TextField, TextAreaField, SubmitField, validators
from flask.ext.wtf import Form
from flask.ext.mail import Message, Mail

class ContactForm(Form):
    name    = TextField("Name",         [validators.Required("Please enter your name.")])
    email   = TextField("Email",        [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
    subject = TextField("Subject",      [validators.Required("Please enter a subject.")])
    message = TextAreaField("Message",  [validators.Required("Please enter a message.")])
    submit  = SubmitField("Send")
    #captcha = TextField("Type the website URL to verify you are not a robot", [validators.Required(), validators.EqualTo("socalnsp.org", message="Wrong")])
    #recaptcha = RecaptchaField()

emails = list([ ("General Information",     "admin@socalnsp.org"), 
                ("JOIN Ski Patrol",         "join@socalnsp.org"),
                ("Alumni",                  "alumni@socalnsp.org"),
                ("Avalanche",               "avalanche@socalnsp.org"),
                ("Awards",                  "awards@socalnsp.org"),
                ("Certified",               "certified@socalnsp.org"),
                ("Instructor Development",  "instructordevelopment@socalnsp.org"),
                ("Mountaineering",          "mountaineering@socalnsp.org"),
                ("OEC",                     "oec@socalnsp.org"),
                ("Senior",                  "senior@socalnsp.org"),
                ("Ski & Toboggan",          "senior@socalnsp.org"),
                ("Snowboarding",            "snowboarding@socalnsp.org")
                ])

