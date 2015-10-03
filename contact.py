from flask import Flask, render_template, request, flash
from flask.ext.mail import Message, Mail
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField

import cgi
import cgitb; cgitb.enable()  # for troubleshooting

app = Flask(__name__,template_folder='static/templates',static_folder='static')
 
app.secret_key = 'development key'
app.config.from_object(__name__)
mail = Mail(app)

app.config.update(dict(
    MAIL_DEBUG    = True,
    MAIL_SERVER   = 'smtpout.secureserver.net',
    MAIL_PORT     = 465,
    MAIL_USE_SSL  = True,
    MAIL_USERNAME = 'admin@socalnsp.org',
    MAIL_PASSWORD = 'hal9000e',
    DEFAULT_MAIL_SENDER = 'admin@socalnsp.org',
    SECRET_KEY     = app.secret_key,
))

mail.init_app(app)

app.secret_key = 'development key'

class ContactForm(Form):
  name = TextField("Name")
  email = TextField("Email")
  subject = TextField("Subject")
  message = TextAreaField("Message")
  submit = SubmitField("Send")

debugStatus="false"
import os
if os.name == 'nt':
    debugStatus = "true"

@app.route('/contact', methods=['GET', 'POST'])
def done():
    return("All done!")
    
@app.route('/', methods=['GET','POST'])
def contact():
  form = ContactForm()
 
  if request.method == 'POST':
    if form.validate() == False:
      flash('All fields are required.')
      return render_template('contact.html', form=form)
    else:
      msg = Message(form.subject.data, sender='contact@example.com', recipients=['your_email@example.com'])
      msg.body = """
      From: %s <%s>
      %s
      """ % (form.name.data, form.email.data, form.message.data)
      mail.send(msg)
 
      return 'Form posted.'
 
  elif request.method == 'GET':
    return render_template('test.html', form=form)
    

if __name__ == '__main__':
    app.run(debug=debugStatus)