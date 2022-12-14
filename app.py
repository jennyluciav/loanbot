from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from loanbot import ask, append_interaction_to_chat_log

app = Flask(__name__)
# if for some reason your conversation with the chef gets weird, change the secret key 
app.config['SECRET_KEY'] = 'top-secret!1111'

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
    return str(msg)


if __name__ == '__main__':
    app.run(debug=True)
