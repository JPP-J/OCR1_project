from flask import Blueprint, render_template, request, flash
from app.forms import ImageForm
from app.models import is_valid_image_url, extract_text


main = Blueprint("main", __name__)


@main.route("/", methods=["GET", "POST"])
@main.route("/index", methods=["GET", "POST"])
def index():
    form = ImageForm()
    image_url = None  # Default value (no image at first)
    result_text = None  # Default value (no result text at first)


    if form.validate_on_submit():
        image_url = form.image_url.data

        if is_valid_image_url(image_url):
            flash("Image URL is valid!", "success")

            # Extract text from the image URL
            result_text = extract_text(image_url)

            if result_text:
                flash("Text extracted successfully!", "success")
                # return render_template("result.html", title="Result", result_text=result_text, image_url=image_url)
            else:
                flash("No text found in the image.", "warning")
        else:
            flash("Invalid image URL. Please try again.", "danger")

    return render_template("index.html", title="Home", form=form, image_url=image_url, result_text=result_text)