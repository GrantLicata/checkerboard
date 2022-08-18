from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def eight_by_eight():
    return render_template('index.html', x = 8, y = 8)



if __name__=="__main__":   
    app.run(debug=True)