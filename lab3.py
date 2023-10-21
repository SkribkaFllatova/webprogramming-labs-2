from flask import Blueprint, render_template, request
lab3 = Blueprint('lab3', __name__)


@lab3.route('/lab3/')
def lab():
    return render_template('lab3.html')


@lab3.route('/lab3/form1')
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

@lab3.route('/lab3/order')
def order():
    return render_template('order.html')

@lab3.route('/lab3/pay')
def pay():
    price = 0
    drink = request.args.get('drink')
    if drink == 'coffe':
        price = 120
    elif drink == 'black-tea':
        price = 80
    else:
        price = 70

    if request.args.get('milk') == 'on':
        price += 30
    if request.args.get('sugar') == 'on':
        price += 10

    return render_template('pay.html', price=price)


@lab3.route('/lab3/success')
def success():
    return render_template('success.html')



@lab3.route('/lab3/bilet')
def bilet():
    errors2 = {}
    fio = request.args.get('fio')
    if fio == '':
        errors2['fio'] = 'Заполните поле'

    tip = request.args.get('tip')

    polka = request.args.get('polka')

    bag = request.args.get('bag')

    errors3 = {}
    age1 = request.args.get('age1')
    if age1 == '':
        errors3['age1'] = 'Заполните поле'

    errors4 = {}
    gorod = request.args.get('gorod')
    if gorod == '':
        errors4['gorod'] = 'Заполните поле'

    errors5 = {}
    gorod1 = request.args.get('gorod1')
    if gorod1 == '':
        errors5['gorod1'] = 'Заполните поле'

    errors6 = {}
    date = request.args.get('date')
    if date == '':
        errors6['date'] = 'Заполните поле'

    return render_template('bilet.html', fio=fio, tip=tip, polka=polka, bag=bag, age1=age1, gorod=gorod, gorod1=gorod1, date=date, errors2=errors2, errors3=errors3, errors4=errors4, errors5=errors5, errors6=errors6)

