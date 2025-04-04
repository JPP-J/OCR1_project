from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired, URL

class ImageForm(FlaskForm):
    image_url = StringField("Image Image", 
                            validators=[DataRequired(), URL()],
                            render_kw={"class": "input-field", "placeholder": "Enter image URL"}  # Adds a CSS class & placeholder  
    )
    submit = SubmitField("Submit", 
                         render_kw={"class": "submit-btn"})  # ✅ Set CSS class here