from flask import Blueprint, redirect, url_for, render_template
lab2 = Blueprint('lab2', __name__)


@lab2.route ('/lab2/example')
def example():
    name, lab2, group, course = 'Скрибка Владислав, Филатова Юлия', 3, 'ФБИ-11', 3
    fruits = [
        {'name': 'яблоки', 'price': 100},
        {'name': 'груши', 'price': 120},
        {'name': 'апельсины', 'price': 80},
        {'name': 'мандарины', 'price': 95},
        {'name': 'манго', 'price': 321}
        ]
    knigi = [
        {'name': 'Анджей Сапковский, «The Wicher», фэнтези, 1400 страниц'},
        {'name': 'Лев Толстой, «Война и мир», роман-эпопея, 1300 страниц'},
        {'name': 'Джордж Оруэлл, «1984», роман, 320 страниц'},
        {'name': 'Джеймс Джойс, «Улисс», роман, 800 страниц'},
        {'name': 'Владимир Набоков, «Лолита», роман, 450 страниц'},
        {'name': 'Уильям Фолкнер, «Звук и ярость», роман, 420 страниц'},
        {'name': 'Ральф Эллисон, «Человек-невидимка», роман, 400 страниц'},
        {'name': 'Джейн Остен, «Гордость и предубеждение», роман, 390 страниц'},
        {'name': 'Джонатан Свифт, «Путешествия Гулливера», роман, 690 страниц'},
        {'name': 'Дмитрий Глуховский, «Metro 2033», роман, 390 страниц'}
    ]
    return render_template('example.html', name=name, lab2=lab2, group=group, course=course, fruits=fruits, knigi=knigi)


@lab2.route('/lab2/')
def lab():
    return render_template('lab2.html')


@lab2.route('/lab2/car')
def car():
    return render_template('car.html')



