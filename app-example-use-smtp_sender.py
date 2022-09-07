from flask import Flask
import smtp_sender

app = Flask(__name__)

@app.route("/")
def index():
   smtp_sender.mailing('Prueba', 'Esta es una prueba CODE', 'cmontoya88@gmail.com')
   return "Envío"


if __name__ == '__main__':
   app.run()