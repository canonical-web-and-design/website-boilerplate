from canonicalwebteam.flask_base.app import FlaskBase

# Rename your project below
app = FlaskBase(
    __name__,
    "project-name.com",
    template_folder="../templates",
    static_folder="../static",
    template_404="404.html",
    template_500="500.html",
)
