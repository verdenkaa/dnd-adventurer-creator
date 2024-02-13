from flask import *
from objects import *
from pdf_creator import *


app = Flask(__name__)
engine = create_engine("sqlite:///data.db")
session = Session(bind=engine)


@app.route('/')
@app.route('/index', methods=['GET', 'POST'])
def index():
    races = [i for i in session.query(Race).all()]  # берем значения из базы данных
    clases = [i for i in session.query(Class).all()]
    chose_race = request.form.get('race_select')  # при выборе возмет то что выбрали, иначе None
    chose_class = request.form.get('class_select')
    return render_template('index.html', races=races, clases=clases, chose_race=chose_race,
                           chose_class=chose_class)

@app.route('/download', methods=['GET', 'POST'])  # метод скачивания файла
def download():
    race = request.args.get('race')  # парсим аргументы
    clas = request.args.get('clas')
    pdf_make(race=race, clas=clas)  # меняем в шаблоне
    path = "./static/images/template_none_time.pdf"
    return send_file(path, as_attachment=True)  # скачиваем


# Перед комитом обязательно коментить запуск, иначе не работает хостинг
#if __name__ == '__main__':
   #app.run(debug=True)