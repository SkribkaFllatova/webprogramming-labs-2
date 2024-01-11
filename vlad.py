from werkzeug.security import check_password_hash, generate_password_hash
from flask import redirect, render_template, request, Blueprint, session
import psycopg2

vlad = Blueprint("vlad", __name__)


def dbConnect():
    conn = psycopg2.connect(
        host="127.0.0.1",
        port="65223",
        database="rgzvlad",
        user="vlad",
        password="123")

    return conn;

def dbClose(cursor, connection):
    cursor.close()
    connection.close()


@vlad.route("/vlad/")
def main():
    return render_template("rgz/vlad.html")


@vlad.route("/vlad/poisk")
def poisk():
    errors = {}
    lek = request.args.get('lek')
    if lek == '':
        errors['lek'] = 'Заполните поле!'
    
    conn = dbConnect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM medic LIMIT 10;")

    data = cursor.fetchall()

    dbClose(cursor, conn)

    return render_template("rgz/poisk.html", errors=errors, lek=lek, data=data)


@vlad.route("/vlad/poisk1")
def poisk1():
    errors = {}
    lek = request.args.get('lek')
    if lek == '':
        errors['lek'] = 'Заполните поле!'
    
    conn = dbConnect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM medic LIMIT 10 OFFSET 10;")

    data = cursor.fetchall()

    dbClose(cursor, conn)

    return render_template("rgz/poisk1.html", errors=errors, lek=lek, data=data)


@vlad.route("/vlad/poisk2")
def poisk2():
    errors = {}
    lek = request.args.get('lek')
    if lek == '':
        errors['lek'] = 'Заполните поле!'
    
    conn = dbConnect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM medic LIMIT 10 OFFSET 20;")

    data = cursor.fetchall()

    dbClose(cursor, conn)

    return render_template("rgz/poisk2.html", errors=errors, lek=lek, data=data)


@vlad.route("/vlad/poisk3")
def poisk3():
    errors = {}
    lek = request.args.get('lek')
    if lek == '':
        errors['lek'] = 'Заполните поле!'
    
    conn = dbConnect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM medic LIMIT 10 OFFSET 30;")

    data = cursor.fetchall()

    dbClose(cursor, conn)

    return render_template("rgz/poisk3.html", errors=errors, lek=lek, data=data)


@vlad.route("/vlad/poisk4")
def poisk4():
    errors = {}
    lek = request.args.get('lek')
    if lek == '':
        errors['lek'] = 'Заполните поле!'
    
    conn = dbConnect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM medic LIMIT 10 OFFSET 40;")

    data = cursor.fetchall()

    dbClose(cursor, conn)

    return render_template("rgz/poisk4.html", errors=errors, lek=lek, data=data)


@vlad.route("/vlad/poisk5")
def poisk5():
    errors = {}
    lek = request.args.get('lek')
    if lek == '':
        errors['lek'] = 'Заполните поле!'
    
    conn = dbConnect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM medic LIMIT 10 OFFSET 50;")

    data = cursor.fetchall()

    dbClose(cursor, conn)

    return render_template("rgz/poisk5.html", errors=errors, lek=lek, data=data)


@vlad.route("/vlad/poisk6")
def poisk6():
    errors = {}
    lek = request.args.get('lek')
    if lek == '':
        errors['lek'] = 'Заполните поле!'
    
    conn = dbConnect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM medic LIMIT 10 OFFSET 60;")

    data = cursor.fetchall()

    dbClose(cursor, conn)

    return render_template("rgz/poisk6.html", errors=errors, lek=lek, data=data)


@vlad.route("/vlad/poisk7")
def poisk7():
    errors = {}
    lek = request.args.get('lek')
    if lek == '':
        errors['lek'] = 'Заполните поле!'
    
    conn = dbConnect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM medic LIMIT 10 OFFSET 70;")

    data = cursor.fetchall()

    dbClose(cursor, conn)

    return render_template("rgz/poisk7.html", errors=errors, lek=lek, data=data)


@vlad.route("/vlad/poisk8")
def poisk8():
    errors = {}
    lek = request.args.get('lek')
    if lek == '':
        errors['lek'] = 'Заполните поле!'
    
    conn = dbConnect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM medic LIMIT 10 OFFSET 80;")

    data = cursor.fetchall()

    dbClose(cursor, conn)

    return render_template("rgz/poisk8.html", errors=errors, lek=lek, data=data)


@vlad.route("/vlad/poisk9")
def poisk9():
    errors = {}
    lek = request.args.get('lek')
    if lek == '':
        errors['lek'] = 'Заполните поле!'
    
    conn = dbConnect()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM medic LIMIT 10 OFFSET 90;")

    data = cursor.fetchall()

    dbClose(cursor, conn)

    return render_template("rgz/poisk9.html", errors=errors, lek=lek, data=data)


@vlad.route('/vlad/login', methods=['GET', 'POST'])
def loginPage():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        conn = dbConnect()
        cursor = conn.cursor()

        cursor.execute("SELECT * FROM users WHERE username = %s;", (username,))
        user = cursor.fetchone()

        if user and check_password_hash(user[2], password):
            session['user_id'] = user[0]
            session['username'] = user[1]
            return redirect('/vlad/admin')
        else:
            error = "Неверное имя пользователя или пароль"
            return render_template("rgz/login.html", error=error)
    else:
        return render_template("rgz/login.html")



@vlad.route('/vlad/admin', methods=['GET', 'POST'])
def admin():
    if 'user_id' in session:
        if request.method == 'POST':
            action = request.form['action']
            if action == 'add':
                lek = request.form['lek']
                cena = request.form['cena']
                conn = dbConnect()
                cursor = conn.cursor()

                cursor.execute("INSERT INTO medic (lek, cena) VALUES (%s, %s);", (lek, cena))

                dbClose(cursor, conn)

                return redirect('/vlad/admin')
            elif action == 'edit':
                lek = request.form['lek']
                cena = request.form['cena']
                id = request.form['id']
                conn = dbConnect()
                cursor = conn.cursor()

                cursor.execute("UPDATE medic SET lek = %s, cena = %s WHERE id = %s;", (lek, cena, id))

                dbClose(cursor, conn)

                return redirect('/vlad/admin')
            elif action == 'delete':
                id = request.form['id']
                conn = dbConnect()
                cursor = conn.cursor()

                cursor.execute("DELETE FROM medic WHERE id = %s;", (id,))

                dbClose(cursor, conn)

                return redirect('/vlad/admin')

        else:
            conn = dbConnect()
            cursor = conn.cursor()

            cursor.execute("SELECT * FROM medic;")

            data = cursor.fetchall()

            dbClose(cursor, conn)

            return render_template("rgz/admin.html", data=data)
    else:
        return redirect('/vlad/login')

