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

'''#---------- MAIL STUFF ------------ #
mail = Mail(app)

#import sys
#sys.path.append('../PA_repo/')
#from app_config import *
app.config.from_pyfile('../PA_repo/app_config.cfg')
#app = config_app(app)

mail = Mail(app)

from forms import *
#-----------------------------------#'''

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', pageTitle="Home")

@app.route('/patrol_map')
def patrol_map():
    return render_template('patrol_map.html');

@app.route('/<url_name>')
def gen_route(url_name):
    url_name = url_name.lower()
    file = url_name
    page = 'Error'

    if url_name == 'about':
        page = 'About'
    elif url_name == 'join':
        page = 'Join NSP'
    elif url_name == 'join.html':
        page = 'Join NSP'
    elif url_name == 'patrols':
        page = 'Patrols'
    elif url_name == 'programs':
        page = 'Programs'
    elif url_name == 'bill_eslick_fund':
        page = "Bill Eslick Fund"
    elif url_name == 'sponsors':
        page = "Sponsors"
    else:
        file = 'error'

    return render_template(file+'.html', pageTitle=page)

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

'''
@app.route('/contact', methods=['GET', 'POST'])
def contact():
    global emails
    form = ContactForm(csrf_enabled=False)
    nSelected = 1;

    if request.method == 'GET':
        return render_template('contact.html', pageTitle="Contact Us", form=form, emails=emails, nth_selected=nSelected)

    #msg = Message('Hello', sender='keholmbeck@yahoo.com', recipients=['admin@socalnsp.org'])
    #msg.body = "This is the email body"
    #mail.send(msg)
    #return "Sent"

    #   if request.method == 'POST':
    if form.validate() == False:
        flash('All fields are required.')
        return render_template('contact.html', form=form, emails=emails, nth_selected=nSelected)

    else:
        selected  = request.form[ "emailSelect" ]
        selected  = int( selected )
        recipient = emails[selected][1]

        msg = Message(form.subject.data, sender=form.email.data, recipients=[recipient])
        msg.body = """
        (Email sent through socalnsp.org) \n
        From: %s (%s) \n\n
        %s
        """ % (form.name.data, form.email.data, form.message.data)

        mail.send(msg)

        return render_template('contact.html', success=True)
#'''

#---------- PATROLS ---------#
@app.route('/patrols/<page>')
def patrol_route(page):

    pagename = page.lower()
    file = page
    page = 'Error'

    if pagename == 'member_patrols':
        page = 'Member Patrols'
    elif pagename == 'snowboard':
        page = 'Snowboard Program'
    else:
        return render_template('error.html', pageTitle=page);

    return render_template('patrols/' + file + '.html', pageTitle=page);


#---------- PROGRAMS ---------#
@app.route('/programs/<progname>')
def prog_route(progname):

    progname = progname.lower()
    file = progname
    page = 'Error'

    if progname == 'alumni':
        page = 'Alumni Program'
    elif progname == 'avalanche':
        page = 'Avalanche Program'
    elif progname == 'awards':
        page = 'Awards'
    elif progname == 'certified':
        page = 'Certified Program'
    elif progname == 'instructor_development':
        page = 'Instructor Development'
    elif progname == 'mtr':
        page = 'Mountain Travel & Rescue'
    elif progname == 'oec':
        page = 'Outdoor Emergency Care'
    elif progname == 'sar':
        page = 'Search & Rescue'
    elif progname == 'senior':
        page = 'Senior Program'
    elif progname == 'ski_and_toboggan':
        page = 'Ski & Toboggan Program'
    elif progname == 'snowboard':
        page = 'Snowboard Program'
    else:
        return render_template('error.html', pageTitle=page);

    return render_template('programs/' + file + '.html', pageTitle=page);


if __name__ == '__main__':
    app.run(port=5000, debug=True)