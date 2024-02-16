
from flask import Flask,render_template


#class object
#instanc object

app =Flask(__name__)

@app.route("/")
def Index():
    return render_template('index.html')
@app.route('/about.html')
def About():
    name ="Uchiha Madara😎🙄"
    return render_template('about.html',display_name  = name )
app.run(debug=True)