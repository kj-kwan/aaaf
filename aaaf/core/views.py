# core\views.py
import os
from flask import render_template, request, Blueprint, redirect
from aaaf import app, db
from werkzeug.utils import secure_filename
from aaaf.models import User, BlogPost

core = Blueprint('core', __name__, static_folder='static', static_url_path='/static')

@core.route('/',methods=["GET","POST"])
def index():
    return render_template('core_pages/home.html')

@core.route('/about',methods=["GET","POST"])
def about():
    return render_template('core_pages/about.html')

@core.route('/our_team',methods=["GET","POST"])
def team():
    return render_template('core_pages/our_team.html')

@core.route('/contact_us',methods=["GET","POST"])
def contact_us():
    return render_template('core_pages/contact_us.html')

@core.route('/blog_posts',methods=["GET","POST"])
def blog_posts():
    page = request.args.get('page',1,type=int)
    blog_posts = BlogPost.query.order_by(BlogPost.date.desc()).paginate(page=page,per_page=10)
    return render_template('blog_pages/blog_posts.html', blog_posts=blog_posts)

@core.route('/events',methods=["GET","POST"])
def events():
    return render_template('core_pages/events.html')

@core.route('/faqs',methods=["GET","POST"])
def faqs():
    return render_template('core_pages/faq.html')

@core.route('/support_us',methods=["GET","POST"])
def support_us():
    return render_template('core_pages/support_us.html')

@core.route('/festival_info',methods=["GET","POST"])
def festival_info():
    return render_template('core_pages/festival_info.html')

@core.route('/donation',methods=["GET","POST"])
def donation():
    return render_template('core_pages/donation.html')

@core.route('/sponsors',methods=["GET","POST"])
def sponsors():
    return render_template('core_pages/sponsors.html')

@core.route('/community_partners',methods=["GET","POST"])
def community_partners():
    return render_template('core_pages/community_partners.html')
