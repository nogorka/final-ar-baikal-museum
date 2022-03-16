from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('start_page.html')

@app.route('/predefined/')
def predefined():
    return render_template('predefined.html')

@app.route('/generated')
def generated():
    return render_template('generated.html')

@app.route('/custom')
def custom():
    return render_template('custom.html')

@app.route('/building')
def building():
    return 'Your route is building...'

@app.errorhandler(404)
def page_not_found(error):
    return render_template('error.html', error=error), 404


if __name__ == '__main__':
    app.run(debug=True)