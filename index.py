from flask import *
#from objects import *


app = Flask(__name__)
#engine = create_engine("sqlite:///data.db")
#session = Session(bind=engine)


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


if __name__ == '__main__':
   app.run(debug=True)