#
# git add --all
# git commit -m"Commit message"
# git push origin master
#

from flask import Flask, render_template, Blueprint
from flask import request, redirect, flash
from flask.ext.wtf import Form
from wtforms import TextField, TextAreaField, SubmitField, validators
import feedparser
 
import cgi
import cgitb; cgitb.enable()  # for troubleshooting

from app import *

@app.route('/banquet')
def banquet():
    return redirect('https://www.paypal.com/cgi-bin/webscr?cmd=_s-xclick&hosted_button_id=DFHCMBHGCVRSN');
    
@app.route('/bill_eslick_fund')
def bill():
    return render_template('bill_eslick_fund.html', pageTitle='Fund');
    
@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', pageTitle="Home")
    
@app.route('/sponsors')
def sponsors():
    return render_template('sponsors.html', pageTitle="Our Sponsors")
    
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
    app.run(debug=True)