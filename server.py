from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    return "Hello world"


@app.route('/play')
@app.route('/play/<x>')
@app.route('/play/<x>/<color>')
def play_times_and_color(x=3,color="red"):  
    return render_template('index.html',x=int(x),color=color)


if __name__ == '__main__':
  app.run(debug=True)