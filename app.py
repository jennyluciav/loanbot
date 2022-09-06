from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from loanbot import ask, append_interaction_to_chat_log
import random

app = Flask(__name__)
# if for some reason your conversation with the chef gets weird, change the secret key 
app.config['SECRET_KEY'] = 'top-secret!66666'


@app.route('/loanbot', methods=['POST'])
def loan():
    incoming_msg = request.values['Body']
    print("incoming_msg = ", incoming_msg)
    chat_log = session.get('chat_log')
    answer = ask(incoming_msg, chat_log)
    print("answer = ", answer)
    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,
                                                         chat_log)
    #print("the session chat_log = ", chat_log)
    msg = MessagingResponse()
    msg.message(answer)
    print("msg = ", msg)
    if "estado de su solicitud" in answer or "estado de tu solicitud" in answer:
        print("FINALIZAR CONVERSACION")
        chat_filename = "chat_log_" + str(random.randint(0,10)) + ".txt"
        file = open(chat_filename, "w")
        file.write(session['chat_log'])
        file.close()
    return str(msg)


if __name__ == '__main__':
    app.run(debug=True)
