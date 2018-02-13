from __future__ import unicode_literals
# -*- coding: utf-8 -*-
import traceback
from datetime import timedelta
from time import strftime
from flask import Flask, render_template, Response, redirect, url_for, session, request, flash, json, jsonify, \
     g
import os
import pymssql

from pip import logger

from werkzeug.utils import escape

from form import Login, FormFromIndex

from query import main_select

app = Flask(__name__)

secret = os.urandom(24)

app.secret_key = secret


class DataFormatted:

    def __init__(self, data):
        self.data = data

    def get(self):
        return self.data

    def set(self, data):
        self.data = data


data_formatted = None
dataFormatted = DataFormatted(data_formatted)

app.logger.info("Before req:", dataFormatted)


def connect_db(user, password):
    server = '172.20.0.44'
    database = 'GLSis'
    db = pymssql.connect(server=server, user=user, password=password, database=database)
    app.logger.info("open connect db: ")
    app.logger.info(db)
    return db


def get_db(username, password):
    u = username
    p = password

    app.logger.info("u: ")
    app.logger.info(u)

    app.logger.info("p: ")
    app.logger.info(p)

    if not hasattr(g, 'db'):
        g.db = connect_db(u, p)
        app.logger.info("g.db: ")
        app.logger.info(g.db)
    return g.db


@app.before_request
def make_session_permanent():
    session.permanent = True
    app.permanent_session_lifetime = timedelta(minutes=60)
    if '127.0.0.1:5000' in request.host_url or '0.0.0.0' in request.host_url:
        app.jinja_env.cache = {}



@app.route('/', methods=['GET', 'POST'])
def login():
    form_login = Login(request.form)
    name_separate = "OMA\\"
    if request.method == 'POST':

        user = request.form['username']
        passwd = request.form['password']

        if form_login.validate():

            if user == 'sa' or user == "kst":
                session['username'] = user
                session['password'] = passwd
                try:
                    get_db(session['username'],  session['password'])

                    app.logger.info("session login sa: ")
                    app.logger.info(get_db(session['username'],  session['password']))

                    return redirect(url_for('index'))
                except pymssql.DatabaseError:
                    app.logger.info('Logged in as %s' % escape(session['username']))
                    app.logger.info('Logged in as %s' % escape(session['password']))
                    app.logger.info('Error login or password')
                    flash('Ошибка: Нет прав.')
            else:
                user_separate = (name_separate + user)
                session['username'] = user_separate
                session['password'] = passwd

                try:
                    get_db(session['username'], session['password'])
                    app.logger.info("session login another : ")
                    app.logger.info(get_db(session['username'], session['password']))
                    return redirect(url_for('index'))
                except pymssql.DatabaseError:
                    app.logger.info('Logged in as %s' % escape(session['username']))
                    app.logger.info('Logged in as %s' % escape(session['password']))
                    app.logger.info('Error login or password')
                    flash('Ошибка: Нет прав.')

            app.logger.info("User input: ", user, passwd)

            app.logger.info("session user", session['username'], session['password'])
        else:
            flash('Ошибка: Введите логин и пароль.')
    return Response(render_template('login.html', form_login=form_login))


@app.route('/index', methods=['GET', 'POST'])
def index():
    form = FormFromIndex(request.form)

    if 'username' in session:
        app.logger.info('Logged in as %s' % escape(session['username']))

        user = escape(session['username'])

        if request.method == 'POST':

       
            search = request.form['search']
            select = request.form['select']

            valueBox = request.form.getlist('check')

            if form.validate():


                try:

                    conn = get_db(session['username'], session['password'])
                    app.logger.info(conn)
                    app.logger.info(get_db(session['username'], session['password']))
                    valueStr = ', '.join(str(e) for e in valueBox)

                    data = main_select(valueStr, search, select, conn)  # Получаем результат

                    conn.close()
                    data_json = json.dumps(data)

                    for i in range(len(valueBox)):
                        valueBox[i] = valueBox[i].replace("[", "[\u0022")
                        valueBox[i] = valueBox[i].replace("]", "\u0022]")

                    valueBox_json = json.dumps(valueBox)

                    pattern_start = "\"[\\"
                    pattern_finish = "\\\"]\""

                    valueBox_json_pattern_start = valueBox_json.replace(pattern_start, "[")
                    valueBox_json_finish = valueBox_json_pattern_start.replace(pattern_finish, "\"]")

                    dataFormatted.set("{ \"columns\":" + valueBox_json_finish + ", \"data\":" + data_json + "}")
                    app.logger.info(dataFormatted)
                    # data_formatted = "{ \"columns\":" + valueBox_json_finish + ", \"data\":" + data_json + "}"

                    # global data_formatted

                    if not data:
                        flash('Ничего не найдено')
                    else:
                        flash("Найден товар: " + search)
                        return Response(
                            render_template('index.html', user=user, form=form, search=search
                                            ))

                except Exception as err:
                    try:
                        flash("Где-то нет прав.")
                        app.logger.info('Нет прав.')
                        raise pymssql.DatabaseError
                    except:
                        pass
                        traceback.print_tb(err.__traceback__)
                finally:
                    conn.close()
            else:
                flash('Ошибка: Введите номер товара.')
                flash('Длина номера товара, должна быть от 3 до 6.')
                flash('Только цифры.')
        return Response(render_template('index.html', user=user, form=form))
    else:
        return redirect(url_for('login'))



@app.route('/background', methods=['GET'])
def background_process():

    data_back = dataFormatted.get()
    app.logger.info("dataFormatted.get(): ")
    app.logger.info(dataFormatted.get())

    app.logger.info("data_back: ")
    app.logger.info(data_back)
    # data_back = data_formatted
    if data_back is None:
        data_back = {
        "columns": [
                    ["\u0424\u0438\u043b\u0438\u0430\u043b"],
                    ["\u0421\u0435\u043a\u0446\u0438\u044f"],
                    ["\u041a\u043e\u0434 \u0422\u043e\u0432\u0430\u0440\u0430"],
                    ["\u041d\u0430\u0437\u0432\u0430\u043d\u0438\u0435"],
                    ["\u041a\u0430\u0442\u0435\u0433\u043e\u0440\u0438\u044f"],
                    ["\u0426\u0435\u043d\u0430 \u0440\u043e\u0437\u043d\u0438\u0446\u0430"],
                    ["\u041a\u043e\u043b\u0438\u0447\u0435\u0441\u0442\u0432\u043e"]
                ],
                "data": []
        }

        return jsonify(data_back)
    else:
        return data_back




@app.route('/', methods=['GET'])
def logout():
    session.clear()
    # remove the username from the session if it's there
    # удалить из сессии имя пользователя, если оно там есть
    session.pop('username', None)
    return redirect(url_for('/'))



@app.errorhandler(404)
def not_found(error):
    return Response(render_template('404.html')), 404


@app.after_request
def after_request(response):
    response.headers.add('Access-Control-Allow-Origin', '*')
    response.headers.add('Cache-Control', 'no-cache')
    timestamp = strftime('[%Y-%b-%d %H:%M]')
    logger.error('%s %s %s %s %s %s',
                 timestamp, request.remote_addr, request.method,
                 request.scheme, request.full_path, response.status)
    return response


@app.teardown_request
def teardown_request(exception):
    if hasattr(g, 'db'):
        g.db.close()
        app.logger.info("g.db.close()")
        app.logger.info(g.db.close())



