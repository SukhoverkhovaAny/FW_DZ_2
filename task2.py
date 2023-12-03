# Задание №2
# Создать страницу, на которой будет изображение и ссылка
# на другую страницу, на которой будет отображаться форма
# для загрузки изображений.
from flask import Flask, render_template, redirect, url_for

app = Flask(__name__)


@app.route('/image/')
def show_image():
    context = {
        'title' : 'Красивая картинка',
    }
    return render_template('task2_1.html', **context)

@app.route('/loading/')
def loading():
    return render_template('task2_2.html')


if __name__ == '__main__':
    app.run(debug=True)