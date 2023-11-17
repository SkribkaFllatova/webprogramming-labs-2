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
        


