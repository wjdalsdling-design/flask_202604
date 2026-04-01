from flask import Flask
from flask_migrate import Migrate
from flask_sqlalchemy import SQLAlchemy

import config

db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(config)

    # ORM
    db.init_app(app)
    migrate.init_app(app, db)
    from .import models

    # 블루프린트 등록
    from .views import main_veiws, question_veiws, answer_views
    app.register_blueprint(main_veiws.bp)
    app.register_blueprint(question_veiws.bp)
    app.register_blueprint(answer_views.bp)

    return app
