# Задание №7
# Создать страницу, на которой будет форма для ввода числа
# и кнопка "Отправить"
# При нажатии на кнопку будет произведено
# перенаправление на страницу с результатом, где будет
# выведено введенное число и его квадрат.

from flask import Flask, render_template, request, redirect, url_for
import math
app = Flask(__name__)


@app.route('/num/', methods=['GET', 'POST'])
def num():
    if request.method == 'POST':
        return redirect(url_for('result')) 
    return render_template('task7_1.html')

@app.route('/result/')
def result():
    num = int(request.form.get('num'))
    result = num ** 2
    context = {
            'title' : 'Результат',
            'result' : result,
        }
    return render_template('task7_2.html', **context)


if __name__ == '__main__':
    app.run(debug=True)