# Задание №6
# Создать страницу, на которой будет форма для ввода имени
# и возраста пользователя и кнопка "Отправить"
# При нажатии на кнопку будет произведена проверка
# возраста и переход на страницу с результатом или на
# страницу с ошибкой в случае некорректного возраста.

from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        name = request.form.get('name')
        age = int(request.form.get('age'))
        if name == 'Харитон' and age == 18:
            return redirect(url_for('hello'))
        else:
            return redirect(url_for('error'))
    return render_template('task6_1.html')  

@app.route('/hello/')
def hello():
    context = {
        'title' : 'Приветствие',
        'name': 'Харитон',
    }
    return render_template('task6_2.html', **context)

@app.route('/error/')
def error():
    context = {
        'title' : 'Ошибка',
        'error' : 'Неверно указаны данные',
    }
    return render_template('task6_3.html', **context)


if __name__ == '__main__':
    app.run(debug=True)