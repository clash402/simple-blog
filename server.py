from flask import Flask, render_template
from post import Post
from datetime import date

# PROPS
app = Flask(__name__)
posts = Post().get_posts()
current_year = date.today().year


# METHODS
@app.route("/")
def get_home():
    return render_template("index.html", all_posts=posts, year=current_year)


@app.route("/post/<int:index>")
def get_post(index):
    return render_template("post.html", post=posts[index - 1], year=current_year)


# MAIN
if __name__ == "__main__":
    app.run(debug=True)
