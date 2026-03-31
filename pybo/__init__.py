from flask import Flask

def create_app():
    app = Flask(__name__)

    # 블루프린트 등록
    from .views import main_veiws
    app.register_blueprint(main_veiws.bp)

    return app
