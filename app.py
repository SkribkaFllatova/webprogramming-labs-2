from flask import Flask, redirect, url_for, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/index")
def start():
    return redirect ("/menu", code=302)
@app.route("/menu")
def menu ():
    return """
        <!doctype html>
        <html>
            <head>
                <title>НГТУ, ФБ, Лабораторные работы</title>
            </head>
            <body>
                <header> НГТУ, ФБ, WEB - программирование, часть 2. Список лабораторных</header>
                <ol>
                <li><a href="/lab1">Первая лабораторная</a>
                <li><a href="/lab2">Вторая лабораторная</a>
                </ol>

                <footer>&copy;  Скрибка Владислав, Филатова Юлия, ФБИ-11, 3 курс, 2023</footer>
            </body>
        </html>
        """
@app.route("/lab1")
def lab1():
    return """
        <!doctype html>
        <html>
            <head>
                <title>Скрибка Владислав, Филатова Юлия, Лабораторная работа 1</title>
            </head>
            <body>
                <header> НГТУ, ФБ, Лабораторная работа 1</header>
                <div>Flask — фреймворк для создания веб-приложений на языке программирования Python, использующий набор инструментов Werkzeug, 
                а также шаблонизатор Jinja2. Относится к категории так называемых микрофреймворков — минималистичных каркасов веб-приложений, 
                сознательно предоставляющих лишь самые базовые возможности.</div>
                <a href="/menu">Меню</a>
                <h2>Реализованные роуты</h2>
                    <ol>
                        <li><a href="/lab1/oak">/lab/oak - дуб </a>
                        <li><a href="/lab1/student">/lab1/student - студент </a>
                        <li><a href="/lab1/python">/lab1/python - python</a>
                        <li><a href="/lab1/unfl">/lab1/unfl - инфляция</a>
                        <li><a href="/lab2/example">/lab1/unfl - инфляция</a>
                    </ol>
                <footer>&copy;  Скрибка Владислав, Филатова Юлия, ФБИ-11, 3 курс, 2023</footer>
            </body>
        </html>
        """
@app.route ('/lab1/oak')
def oak():
    return'''
        <!doctype html>
        <html>
            <head> 
                <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
            </head>
            <body>
                <header>
                    <h1>Дуб</h1>
                </header>
                <main>     
                    <img src="''' + url_for('static' , filename='oak.jpg') +'''" >
                </main>
                <footer>
                </footer> 
            </body>
        </html>
        '''
@app.route ('/lab1/student')
def student():
    return'''
        <!doctype html>
        <html>
            <head> 
                <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
            </head>
            <body>
                <header>
                    <div>Скрибка Владислав</div>
                    <div>Филатова Юлия</div>
                </header>
                <main>
                    <img src="''' + url_for('static' , filename='flag.png') + '''" >
                </main>
                <footer>
                </footer> 
            </body>
        </html>
        '''
@app.route ('/lab1/python')
def python():
    return'''
        <!doctype html>
        <html>
            <head> 
                <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
            </head>
            <body>
                <header>
                    <div> Python в русском языке встречаются названия питон или пайтон) — высокоуровневый язык программирования общего назначения 
                    с динамической строгой типизацией и автоматическим управлением памятью, ориентированный на повышение производительности 
                    разработчика, читаемости кода и его качества, а также на обеспечение переносимости написанных на нём программ. 
                    Язык является полностью объектно-ориентированным в том плане, что всё является объектами. Необычной особенностью языка 
                    является выделение блоков кода пробельными отступами. Синтаксис ядра языка минималистичен, за счёт чего на практике 
                    редко возникает необходимость обращаться к документации. Сам же язык известен как интерпретируемый и используется в 
                    том числе для написания скриптов. 
                    </div>
                    <div></div>
                    <div></div>
                    <div></div>
                    <div></div>
                </header>
                <main>
                   <img src="''' + url_for('static' , filename='python.png') + '''" >
                </main>
                <footer>
                </footer> 
            </body>
        </html>
        '''
@app.route ('/lab1/unfl')
def unfl():
    return'''
        <!doctype html>
        <html>
            <head> 
                <link rel="stylesheet" href="''' + url_for('static', filename='lab1.css') + '''">
            </head>
            <body>
                <header>
                    <div> Инфляция  — устойчивое повышение общего уровня цен на товары и услуги; процесс обесценивания денег, 
                    падение их покупательной способности вследствие чрезмерного выпуска (эмиссии) или сокращения товарной массы 
                    в обращении при неизменном количестве выпущенных денег.</div>
                    <div> При инфляции цена идентичных товаров со временем увеличивается: на одну и ту же сумму денег по прошествии 
                    некоторого времени можно будет купить меньше товаров и услуг, чем прежде. По сути, покупательная способность 
                    денег снижается, деньги обесцениваются. Обесценивание денег приводит к повышению цен в рыночной экономике. 
                    В административно-командной системе хозяйствования обесценивание денег может не приводить к изменению цен, но 
                    возникает нарастающий товарный дефицит.
                    </div>
                    
                </header>
                <main>
                   <img src="''' + url_for('static' , filename='unfl.png') + '''" >
                </main>
                <footer>
                </footer> 
            </body>
        </html>
        '''
@app.route ('/lab2/example')
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

@app.route('/lab2/')
def lab2():
    return render_template('lab2.html')

@app.route('/lab2/car')
def car():
    return render_template('car.html')