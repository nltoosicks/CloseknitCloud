from flask import render_template, redirect, url_for, flash
from flask_login import login_required, current_user
from app.main import bp
from app.models import Gallery
from app.main.forms import CreateGalleryForm
from app import db

@bp.route('/')
@bp.route('/home')
def index():
    return render_template('index.html', title='Home')

@bp.route('/create_gallery', methods=['GET', 'POST'])
@login_required
def create_gallery():
    form = CreateGalleryForm()
    if form.validate_on_submit():
        gallery = Gallery(name=form.name.data, description=form.description.data, owner=current_user)
        db.session.add(gallery)
        db.session.commit()
        flash('Gallery created successfully!', 'success')
        return redirect(url_for('main.index'))
    return render_template('create_gallery.html', title='Create Gallery', form=form)
