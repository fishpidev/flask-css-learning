from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'This is the Pi! TEST'

@app.route('/lemons')
def hello_lemons():
    return 'WHEN LIFE GIVES YOU LEMONS...MAKE SOMETHING'

@app.route('/hello-you/')
@app.route('/hello-you/<name>')
def hello_you(name=None):
    return render_template('hello.html', name=name)


#for some reason the config below is often not read by the comand line arguments
#that are in the turotial... but commenting them out and doing:
#    flask run --host=0.0.0.0
#makes it visible from the wider network using the PI IP address (run hostname -I to get this)

#image credit: Photo by Angel Sinigersky on Unsplash
#the CSS tutorial is here: https://jgthms.com/web-design-in-4-minutes/

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5050, debug=False)
