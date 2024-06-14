from flask import Flask #type: ignore
from API.api import route_manager
from Persistence.DataManager import DataManager


app = Flask(__name__)
dm = DataManager()
dm.load_all()
dm.load_countries()
route_manager(app, dm)

if __name__ == "__main__":
    app.run(port=8000, debug=True)