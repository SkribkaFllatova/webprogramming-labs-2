from flask import Blueprint, render_template, url_for, request

lab9 = Blueprint('lab9', __name__)

@lab9.route("/lab9/")
def main():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    sex = request.args.get('sex')

    return render_template('/lab9/index.html', user=user, sex=sex, errors=errors)



@lab9.app_errorhandler(404)
def not_found(e):
     return "Нет такой страницы. <a href='" + url_for('lab9.main') + "'>Перейти на главную страницу</a>", 404


@lab9.route("/lab9/500")
def main1():
    return render_template ("/lab9/index1.html")

@lab9.app_errorhandler(500)
def not_found1(e):
     return  "Нет такой страницы" , 500


@lab9.route('/lab9')
def form1():
    errors = {}
    user = request.args.get('user')
    if user == '':
        errors['user'] = 'Заполните поле!'

    errors1 = {}
    age = request.args.get('age')
    if age == '':
        errors2['age'] = 'Заполните поле!'


    sex = request.args.get('sex')

    return render_template('form1.html', user=user, age=age, sex=sex, errors=errors, errors1=errors1)