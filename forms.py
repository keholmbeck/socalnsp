from wtforms import TextField, TextAreaField, SubmitField, validators
from flask.ext.wtf import Form

class ContactForm(Form):
    name    = TextField("Name",         [validators.Required('Enter your name')])
    email   = TextField("Email",        [validators.Required(), validators.Email('Enter a valid email address.')])
    subject = TextField("Subject")
    message = TextAreaField("Message",  [validators.Required('Please enter a message.')])
    submit  = SubmitField("Send")
    
    email_list = (
        ('Awards', 'awards'), 
        ('Recruiting', 'recruiting'), 
        ('Director', 'regiondirector'), 
        ('Instructor Development', 'instructordevelopment'),
        ('Senior Program','senior'),
        ('Avalanche', 'avalanche'), 
        ('Treasurer', 'treasurer'), 
        ('Alumni', 'alumni'), 
        ('Snowboarding', 'snowboarding'), 
        ('Certified', 'certified'), 
        ('Mountaineering', 'mountaineering'),
        ('Outdoor Emergency Care', 'oec'), 
        ('Nordic', 'nordic'),
        ('General Information', 'webmaster')
    );
