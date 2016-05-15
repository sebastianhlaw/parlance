from flask import Flask, render_template
from werkzeug.debug import get_current_traceback
app = Flask(__name__)

@app.route('/')
def hello_world():
  return render_template('hello.html', title="Welcome", name="Daniel")

@app.route('/child/')
def hello_kiddies():
  my_name = "Danny boy"
  return render_template('hello.html', title="Welcome", name=my_name)

if __name__ == '__main__':
    app.run(debug=True)
