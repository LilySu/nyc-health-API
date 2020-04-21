from flask import Flask
import markdown
import os

app = Flask(__name__)

@app.route("/")
def hello():
    with open(os.path.dirname(app.root_path) + '/README.md','r') as markdown_file:
        content = markdown_file.read()
        return markdown.markdown(content)
