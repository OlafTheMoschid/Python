from datetime import datetime
from hashlib import md5
from os.path import splitext
from os import remove
from flask import Flask, redirect, render_template, request, abort
from flask_login import (LoginManager, current_user, login_required,
                         login_user, logout_user)
from flask_restful import Api

from sqlalchemy import func
from data import db_session
from data.users import User
from data.video import Video
from forms.upload import UploadForm, VideoChangeForm
from forms.user import LoginForm, RegisterForm, UserChangeForm
import api_user
import users_resources

app = Flask(__name__)
app.config['SECRET_KEY'] = 'my_secret_key'
api = Api(app)
login_manager = LoginManager()
login_manager.init_app(app)

VIDEO_FOLDER = "D:/Projects/Python/Semester2/static/videos/"
# D:/Projects/Python/Semester2/static/videos/


@login_manager.user_loader
def load_user(user_id):
    db_sess = db_session.create_session()
    return db_sess.query(User).get(user_id)


@app.route('/')
def index():
    db_sess = db_session.create_session()
    videos = db_sess.query(Video)
    return render_template("index.html", title="Rutube", videos=videos)


@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect("/")


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        user = db_sess.query(User).filter(
            User.nickname == form.nickname.data).first()
        if user and user.check_password(form.password.data):
            login_user(user, remember=form.remember_me.data)
            return redirect("/")
        return render_template('login.html', form=form,
                               message="Неправильный логин или пароль")
    return render_template('login.html', title='Авторизация', form=form)


@app.route('/register', methods=['GET', 'POST'])
def register():
    db_sess = db_session.create_session()
    form = RegisterForm()
    if form.validate_on_submit():
        if form.password.data != form.password_again.data:
            return render_template('register.html', title='Регистрация',
                                   form=form, message="Пароли не совпадают")
        if db_sess.query(User).filter(
            User.nickname == form.nickname.data).first() and \
                db_sess.query(User).filter(
                    User.email == form.email.data).first():
            return render_template('register.html', title='Регистрация',
                                   form=form,
                                   message="Такой пользователь уже есть",)

        user = User()
        user.nickname = form.nickname.data
        user.email = form.email.data
        user.set_password(form.password.data)

        db_sess.add(user)
        db_sess.commit()
        return redirect("/")
    return render_template('register.html', title='Регистрация', form=form)


@app.route('/user_change', methods=['GET', 'POST'])
@login_required
def user_change():
    db_sess = db_session.create_session()
    form = UserChangeForm()

    if request.method == 'GET':
        user = db_sess.query(User).filter(User.id == current_user.id).first()
        form.nickname.data = user.nickname
        form.email.data = user.email

    if form.validate_on_submit():
        user = db_sess.query(User).filter(User.id == current_user.id).first()
        if form.password.data != form.password_again.data:
            return render_template('register.html',
                                   title='Редактирование пользователя',
                                   form=form,
                                   message="Пароли не совпадают")

        user_exists = db_sess.query(User).filter(
            User.nickname == form.nickname.data or
            User.email == form.email.data).first()

        if user_exists.id != current_user.id:
            return render_template('register.html',
                                   title='Редактирование пользователя',
                                   form=form,
                                   message="Такой пользователь уже существует")

        user.nickname = form.nickname.data
        user.email = form.email.data

        if form.password.data:
            user.set_password(form.password.data)

        db_sess.commit()
        return redirect("/")
    return render_template('register.html',
                           title='Редактирование пользователя',
                           form=form)


@app.route('/<link>')
def watch(link=None):
    db_sess = db_session.create_session()
    video = db_sess.query(Video).filter(Video.link == link).first()
    if video:
        name = video.name
        return render_template("watch.html", title=name, link=link,
                               name=name)
    else:
        name = 'Видео не найдено'
        return render_template("watch.html", title=name, link='',
                               name=name)


@app.route('/search/<word>')
def search(word=None):
    db_sess = db_session.create_session()
    word = '%' + func.lower(word) + '%'
    videos = db_sess.query(Video).filter(func.lower(Video.name.like(word)))
    message = 'По вашему запросу найдено ' + str(videos.count()) + ' видео:'
    return render_template("search.html", title='videoplayer',
                           videos=videos, message=message)


@app.route('/upload', methods=['GET', 'POST'])
@login_required
def upload():
    form = UploadForm()
    if form.validate_on_submit():
        db_sess = db_session.create_session()
        video = Video()
        video.name = form.name.data
        video.author = current_user.nickname
        link = md5(bytes(current_user.nickname + '_' +
                   str(datetime.now()), encoding='utf8')).hexdigest()
        videofile = form.file_data.data
        video.link = link + splitext(videofile.filename)[1]
        with open(VIDEO_FOLDER + video.link, 'wb') as f:
            f.write(videofile.read())
        video.upload_date = datetime.now()
        db_sess.add(video)
        db_sess.commit()
        return redirect('/')
    return render_template('upload.html',
                           title='Загрузка видео',
                           form=form)


@app.route('/video_change/<link>', methods=['GET', 'POST'])
@login_required
def video_change(link=None):
    db_sess = db_session.create_session()
    form = VideoChangeForm()
    video = db_sess.query(Video).filter(Video.link == link).first()

    videos = db_sess.query(Video).filter(
        Video.author == current_user.nickname).all()

    if video not in videos:
        return render_template('video_change.html',
                               title='Редактирование видео',
                               form=form,
                               message='Этого видео нет на вашем канале')

    if request.method == 'GET':
        form.name.data = video.name

    if form.validate_on_submit():
        video.name = form.name.data
        db_sess.commit()

        return redirect("/")
    return render_template('video_change.html',
                           title='Редактирование видео',
                           form=form)


@app.route('/video_delete/<link>', methods=['GET', 'POST'])
@login_required
def video_delete(link=None):
    db_sess = db_session.create_session()
    video = db_sess.query(Video).filter(Video.link == link).first()
    if video:
        db_sess.delete(video)
        db_sess.commit()
        remove(VIDEO_FOLDER + video.link)
    else:
        abort(404)
    return redirect("/")


def main():
    db_session.global_init("db/rutube.db")
    app.register_blueprint(api_user.blueprint)
    api.add_resource(users_resources.UsersListResource, '/api/v2/users')
    api.add_resource(users_resources.UsersResource, '/api/v2/users/<user_id>')
    app.run(port=8080, host='127.0.0.1')


if __name__ == '__main__':
    main()
