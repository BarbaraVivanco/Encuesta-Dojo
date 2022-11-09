from central import app
from flask import render_template,request, redirect, session

@app.route('/')
def formulario_registro():
    return render_template('registro.html')

@app.route('/process', methods=['POST'])
def envio_formulario():
    session['name']= request.form['name']
    session['location']= request.form['location']
    session['language']= request.form['language']
    session['comments']= request.form['comments']
    return redirect('/result')


@app.route('/result')         
def result():
    return render_template("result.html",name_on_template=session['name'], location_on_template=session['location'],language_on_template=session['language'], comments_on_template=session['comments'])



