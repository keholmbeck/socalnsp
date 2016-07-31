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
app.config.from_object(__name__)
mail = Mail(app)

import sys
sys.path.append('../PA_repo/')
from app_config import *

config_app(app)
mail.init_app(app)

from forms import *

#-----------------------------------#'''

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', pageTitle="Home")
    
@app.route('/<url_name>')
def gen_route(url_name):
    url_name = url_name.lower()
    file = url_name
    page = 'Error'
    
    if url_name == 'about':
        page = 'About'
    elif url_name == 'join':
        page = 'Join NSP'
    elif url_name == 'member_patrols':
        page = 'Member Patrols'
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


@app.route('/contact', methods=['GET', 'POST'])
def contact():
    return test
    '''
    global emails
    form = ContactForm(csrf_enabled=False)
    nSelected = 1;
    
    if request.method == 'GET':
        return render_template('contact.html', pageTitle="Contact Us", form=form, emails=emails, nth_selected=nSelected)
    
    #   if request.method == 'POST':    
    if form.validate() == False:
        flash('All fields are required.')
        return render_template('contact.html', form=form, emails=emails, nth_selected=nSelected)
        
    else:
        return "Posted"
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

#---------- PROGRAMS ---------#
@app.route('/programs/<progname>')
def prog_route(progname):

    proganame = progname.lower()
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
    elif progname == 'MTR':
        page = 'Mountain Travel & Rescue'
    elif progname == 'OEC':
        page = 'Outdoor Emergency Care'
    elif progname == 'SAR':
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
    app.run(debug=True)