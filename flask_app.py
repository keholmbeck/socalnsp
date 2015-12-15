#
# git add --all
# git commit -m"Commit message"
# git push origin master
#

from flask import Flask, render_template, Blueprint
from flask import request, redirect, flash
from flask.ext.wtf import Form, RecaptchaField
from wtforms import TextField, TextAreaField, SubmitField, validators
import feedparser

from flask.ext.mail import Message, Mail
 
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

from app import *

#---------- MAIL STUFF ------------ #
app.config.from_object(__name__)
mail = Mail(app)

import sys
sys.path.append('../PA_repo/')
from app_config import *

mail.init_app(app)

class ContactForm(Form):
    name    = TextField("Name",         [validators.Required("Please enter your name.")])
    email   = TextField("Email",        [validators.Required("Please enter your email address."), validators.Email("Please enter your email address.")])
    subject = TextField("Subject",      [validators.Required("Please enter a subject.")])
    message = TextAreaField("Message",  [validators.Required("Please enter a message.")])
    submit  = SubmitField("Send")
    captcha = TextField("Type the website URL to verify you are not a robot", [validators.Required(), validators.EqualTo("socalnsp.org", message="Wrong")])
    recaptcha = RecaptchaField()

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
# -------------------------------- #



@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', pageTitle="Home")
    
@app.route('/about')
def about():
    return render_template('about.html', pageTitle="About")

@app.route('/news')
def news():
    d = feedparser.parse('http://socalnsp.blogspot.com/feeds/posts/default?alt=rss')
    title_entry = d.entries[0]
    d.entries = d.entries[1:4]

    # Most recent blog entry
    title_news = title_entry.date[0:10]
    title_news += "<br> <a href=\"" + title_entry.link + "\">" + title_entry.title + "</a> <BR><BR>"
    title_news += title_entry.summary + "<br><BR><BR>"

    # Titles of recent blogs
    str = ""
    for post in d.entries:
        str += "<a href=\"" + post.link + "\">" + post.title + "</a> <BR><BR>"

    # Additional, non-blog news or to showcase sponsors
    other_news = dict()
    other_news['title'] = 'Whaley Park Instructor Refresher - 13 September'

    other_news['summary'] = 'Gourmet breakfast burritos for the instructor refresher at Whaley Park will be '
    other_news['summary'] += 'provided by <a href=\"http://www.simmzys.com\">Simmzy\'s Pub</a>. Check them out!'

    return render_template('news.html', pageTitle="Upcoming Events", other_news=other_news, title_news=title_news, rss_feed=str)


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return "hi"

@app.route('/join')
def join():
    return render_template('join.html', pageTitle="Join NSP")

@app.route('/MemberPatrols')
def member_patrols():
    return render_template('MemberPatrols.html', pageTitle="Member Patrols")

@app.route('/programs')
def programs():
    return render_template('programs.html', pageTitle="Programs")

 #---------- PROGRAMS ---------#
@app.route('/programs/alumni')
def alumni():
    return render_template('programs/alumni.html', pageTitle="Alumni Program")

@app.route('/programs/avalanche')
def avalanche():
    return render_template('programs/avalanche.html', pageTitle="Avalanche Program")

@app.route('/programs/awards')
def awards():
    return render_template('programs/awards.html', pageTitle="Awards")

@app.route('/programs/certified')
def certified():
    return render_template('programs/certified.html', pageTitle="Certified Program")

@app.route('/programs/instructor_development')
def instructor_development():
    return render_template('programs/instructor_development.html', pageTitle="Instructor Development")

@app.route('/programs/MTR')
def MTR():
    return render_template('programs/MTR.html', pageTitle="Mountain Travel & Rescue")

@app.route('/programs/OEC')
def OEC():
    return render_template('programs/OEC.html', pageTitle="Outdoor Emergency Care")

@app.route('/programs/SAR')
def SAR():
    return render_template('programs/SAR.html', pageTitle="Search & Rescue")

@app.route('/programs/senior')
def senior():
    return render_template('programs/senior.html', pageTitle="Senior Program")

@app.route('/programs/ski_and_toboggan')
def ski_and_tobbogan():
    return render_template('programs/ski_and_toboggan.html', pageTitle="Ski & Toboggan Program")

@app.route('/programs/snowboard')
def snowboard():
    return render_template('programs/snowboard.html', pageTitle="Snowboard Program")


if __name__ == '__main__':
    app.run(debug=False)