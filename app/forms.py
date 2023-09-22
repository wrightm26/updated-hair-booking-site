from flask_wtf import FlaskForm
from wtforms import TextAreaField, TextAreaField, SubmitField
from wtforms.validators import InputRequired



class ReviewForm(FlaskForm):
    review = TextAreaField('Review:', validators=[InputRequired()])
    submit = SubmitField('Submit')
