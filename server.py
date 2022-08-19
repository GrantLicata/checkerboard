from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def eight_by_eight():
    return render_template('index.html', x = 8, y = 8, color1 = 'black', color2 = 'white')

@app.route('/4')
def eight_by_four():
    return render_template('index.html', x = 8, y = 4, color1 = 'black', color2 = 'white')

@app.route('/<int:x_input>/<int:y_input>')
def user_choice(x_input, y_input):
    return render_template('index.html', x = x_input, y = y_input, color1 = 'black', color2 = 'white')

@app.route('/<int:x_input>/<int:y_input>/<string:color1_input>/<string:color2_input>')
def user_choice_color(x_input, y_input, color1_input, color2_input):
    return render_template('index.html', x = x_input, y = y_input, color1 = color1_input, color2 = color2_input)

if __name__=="__main__":   
    app.run(debug=True)