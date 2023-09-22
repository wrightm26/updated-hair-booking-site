import os
from app import app, db
from flask import render_template, redirect, url_for, flash
from app.forms import ReviewForm
from app.models import Reviews

@app.route('/')
def index():
    reviews = Reviews.query.order_by(Reviews.review_id.desc()).all()
    return render_template('index.html', reviews=reviews)



@app.route('/review', methods=['GET', 'POST'])
def review():
    form = ReviewForm()
    if form.validate_on_submit():
        review = form.review.data
        db.session.commit()
        review_info = Reviews(review=review)
        flash(f"Thank you for submitting the following review: {review_info.review}", "success")
        return redirect(url_for('index'))
    return render_template('review.html', form=form)
