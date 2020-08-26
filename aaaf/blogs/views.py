# blogs\views.py
from flask import render_template, url_for, flash, redirect, request, Blueprint
from flask_login import current_user, login_required
from aaaf import db
from aaaf.models import BlogPost
from aaaf.blogs.forms import BlogPostForm

blog_posts = Blueprint('/blog_posts', __name__)

@blog_posts.route('/create_post', methods=['GET','POST'])
def create_post():
    form = BlogPostForm()
    if form.validate_on_submit():
        blog_post = BlogPost(title=form.title.data,
                             text=form.text.data,
                             user_id=current_user.id)
        db.session.add(blog_post)
        db.session.commit()
        flash('Blog post created.')
        return redirect(url_for('core.index'))
    return render_template('blog_pages/create_post.html', form=form)

@blog_posts.route('/<int:blog_post_id>')
def blog_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    return render_template('blog_pages/blog_post.html',
                            title=blog_post.title,
                            date=blog_post.date,
                            post=blog_post)

@blog_posts.route('/<int:blog_post_id>/update_post', methods=['GET','POST'])
@login_required
def update_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        abort(403) # Forbidden. No access.

    form = BlogPostForm()
    if form.validate_on_submit():
        blog_post.title = form.title.data
        blog_post.text = form.text.data
        db.session.commit()
        flash('Post has been updated.')
        return redirect(url_for('/blog_posts.blog_post', blog_post_id=blog_post.id))
    elif request.method == 'GET':
        form.title.data = blog_post.title
        form.text.data = blog_post.text
    return render_template('blog_pages/update_post.html',
                            title='Update',
                            form=form)

@blog_posts.route('/<int:blog_post_id>/delete_post', methods=['POST'])
@login_required
def delete_post(blog_post_id):
    blog_post = BlogPost.query.get_or_404(blog_post_id)
    if blog_post.author != current_user:
        abort(403) # Forbidden. No access.
    form = BlogPostForm()
    db.session.delete(blog_post)
    db.session.commit()
    flash('Post has been deleted.')
    return redirect(url_for('core.index'))
