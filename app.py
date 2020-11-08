from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/index', methods=['POST'])
def index():
    bmi = ''
    if request.method == 'POST' and 'weight' in request.form:
        weight = float(request.form.get('weight'))
        height = float(request.form.get('height'))
        bmi = calc_bmi(weight, height)
    return render_template("index.html",
	                        bmi=bmi)
                            
@app.route('/calc_bmi', methods=['POST'])
def calc_bmi(weight, height):
    return round((weight / ((height / 100) ** 2)*703), 2)

if __name__ == '__main__':
    app.run()