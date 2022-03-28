from flask import Flask, render_template, request, redirect, session
app = Flask(__name__)  
app.secret_key = "survey"

@app.route('/')
def index():
    return render_template("index.html")
    
@app.route('/results')
def result():
    return render_template("results.html")

@app.route('/submit', methods=['POST'])
def submit():
    session['name'] = request.form['name']
    session['dojo_location'] = request.form['dojo_location']
    session['favorite_language'] = request.form['favorite_language']
    session['comment'] = request.form['comment']
    return redirect('/submitting')

@app.route('/submitting')
def submitting(): 
    return render_template('results.html')



@app.route('/go-back')
def clear():
    session.clear()
    return redirect('/')

if __name__=="__main__":   
    app.run(debug=True)    