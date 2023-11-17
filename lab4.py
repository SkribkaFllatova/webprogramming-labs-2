from flask import Blueprint, render_template, request
lab4 = Blueprint('lab4', __name__)

@lab4.route('/lab4/')
def lab():
    return render_template('lab4.html')


@lab4.route('/lab4/login', methods = ['GET' , 'POST'])
def login():
    if request.method == 'GET':
        return render_template("login.html")
    username = request.form.get('username')
    password = request.form.get('password')
    if username == 'VladJulia' and password == '123':
            return render_template('success1.html', username=username)
    else:
        error = 'Неверные логин и/или пароль'
    if username == '':
        error = 'Введите логин'
    if password == '':
        error = 'Введите пароль'
        return render_template('login.html', error=error, username=username, password=password)


@lab4.route('/lab4/success1')
def success1():
    username=request.args.get('username')
    return render_template('success1.html', username = username)


@lab4.route('/lab4/holog', methods = ['GET' , 'POST'])
def holog():
    if request.method == 'GET':
        return render_template('holog.html')

    grad = request.form.get('grad')

    if grad == '':
        error1 = 'Не задана температура'
    else:
        grad = int(grad)
        if grad < -12:
            error1 = 'Не удалось установить температуру - слишком низкое значение'
        elif grad > -1:
            error1 = 'Не удалось установить  температуру - слишком высокое значение'
        elif (grad >= -12) and (grad <= -9):
            error1 = f'Установлена температура: { grad } °C ❄️❄️❄️'
        elif (grad >= -8) and (grad <= -5):
            error1 = f'Установлена температура: { grad } °C ❄️❄️' 
        elif (grad >= -4) and (grad <= -1):
            error1 = f'Установлена температура: { grad } °C ❄️'
    return render_template('holog.html', grad = grad, error1=error1)


@lab4.route('/lab4/zerno', methods = ['GET' , 'POST'])
def zerno():
    if request.method == 'GET':
        return render_template('zerno.html')
    price = 0
    error2 = ''
    zerno = request.form.get('zerno')
    weight = request.form.get('weight')

    if weight == '':
        error2 = 'Не введен вес'
        return render_template('zerno.html', error2=error2)

    weight = int(weight)

    if zerno == 'zxvtym':
        price = 12000 * weight
    elif zerno == 'jdtc':
        price = 8500 * weight
    elif zerno == 'gitybwf':
        price = 8700 * weight
    else:
        zerno == 'hj;m'
        price = 14000 * weight

    if weight <= 0:
        error2 = 'Неверное значение веса'
        return render_template('zerno.html', error2=error2)
    elif weight > 50:
        error2 = 'Такого объема сейчас нет в наличии'
        return render_template('zerno.html', error2=error2)
    else:
        weight > 50
        price = price - (price * 10 / 100)
        error2 = 'Применится скидка 10% за большой объем'
        return render_template('success2.html', price=price, zerno=zerno, weight=weight, error2=error2)


@lab4.route('/lab4/success2')
def success2():
    return render_template('success2.html')


@lab4.route('/lab4/cookies', methods = ['GET' , 'POST'])
def cookies():
    if request.method == 'GET':
        return render_template('cookies.html')
    
    color = request.form.get('color')
    backcolor = request.form.get('backcolor')
    fontsize = request.form.get('fontsize')
    error3 = ''

    if color == backcolor:
        error3 = 'Цвета не должны совпадать!'
        return render_template('cookies.html', error3=error3)
    elif color != backcolor:
        color = color

    if fontsize == '':
        error3 = 'Не задан размер текста:'
        return render_template('cookies.html', error3=error3)

    if fontsize is not None and fontsize.isdigit():
        fontsize = int(fontsize)
        if 5 <= fontsize <= 30:
            fontsize = str(fontsize) + 'px'
    else:
        error3 = 'Размер шрифта должен быть от 5 до 30'
        return render_template('cookies.html', error3=error3)

    headers = {
        'Set-Cookie': 'color=' + color + '; path=/',
        'Set-Cookie': 'backcolor=' + backcolor + '; path=/',
        'Set-Cookie': 'fontsize=' + fontsize + '; path=/',
        'Location': '/lab4/cookies'
    }

    return '', 303, headers