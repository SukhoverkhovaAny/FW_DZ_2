# Задание №4
# Создать страницу, на которой будет форма для ввода текста и
# кнопка "Отправить"
# При нажатии кнопки будет произведен подсчет количества слов
# в тексте и переход на страницу с результатом.
from flask import Flask, render_template, url_for, request
from markupsafe import escape

app = Flask(__name__)


@app.route('/text/')
def text():
    context = {
        'title' : 'Введите текст',
    }
    return render_template('task4_1.html', **context)


@app.route('/count/')
def count():
    if request.method == 'POST':
        text = request.form.get('text')
        count = len(text.split(' '))
        context = {
            'title': 'Результат',
            'count': count,
        }
        return render_template('task4_2.html', **context)



if __name__ == '__main__':
    app.run(debug=True)