from flask import Flask, render_template
from werkzeug.debug import get_current_traceback
app = Flask(__name__)

@app.route('/')
def hello_world():
    return render_template('hello.html', title="Welcome", name="Chaps")

# @app.route('/child/')
# def hello_kiddies():
#     return 'Hello Kiddies!'

if __name__ == '__main__':
    app.run(debug=True)
