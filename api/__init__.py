import os
from flask import Flask
from .tips.tips import tips_blueprint
from .news.news import news_blueprint
from .web.web import web_blueprint
from .graph.graph import graph_blueprint


app = Flask(__name__, instance_relative_config=True)

app.register_blueprint(web_blueprint, url_prefix="/")
app.register_blueprint(tips_blueprint, url_prefix="/api/tips")
app.register_blueprint(news_blueprint, url_prefix="/api/news")
app.register_blueprint(graph_blueprint, url_prefix="/api/graph")
