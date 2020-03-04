from app import app
from app.forms import PatchCordForm, LoginForm
from flask import render_template, flash, redirect, url_for

@app.route('/')
@app.route('/index')
def index():
    users = {'username':'robby'}
    goods = [
        {'name':'MDA', 'SNs':'NS03232AA', 'status':'OK'},
        {'name':'MDA', 'SNs':'NS12232AA', 'status':'OK'},
        {'name':'IOM', 'SNs':'NS53323AB', 'status':'OK'}
    ]
    return render_template('index.html', title='I-MAN', users=users, goods=goods)

@app.route('/input', methods=['GET', 'POST'])
def input():
    form = PatchCordForm()
    if form.validate_on_submit():
        flash('Input Patch Cord Sukses')
        return redirect(url_for('index'))
    return render_template('patchCordForm.html', title='I-MAN', form=form)

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash('Login Sukses')
        return redirect(url_for('index'))
    return render_template('loginForm.html', title='I-MAN', form=form)