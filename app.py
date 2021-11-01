from flask import Flask
from routes.charts import charts_router
from dotenv import load_dotenv


load_dotenv()
app = Flask(__name__)
app.register_blueprint(charts_router)

if __name__ == '__main__':
    app.run()
