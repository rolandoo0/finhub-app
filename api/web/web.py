from flask import Blueprint, render_template, send_from_directory

web_blueprint = Blueprint(
    "web",
    __name__,
    static_url_path="/",
    static_folder="../../frontend/build/",
    template_folder="../../frontend/build/",
)


@web_blueprint.route("/Home")
@web_blueprint.route("/")
def home(path=None):
    "Renders the index html page"
    return web_blueprint.send_static_file("index.html")

