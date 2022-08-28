from flask import Flask, request, session
from twilio.twiml.messaging_response import MessagingResponse
from loanbot import ask, append_interaction_to_chat_log
from get_variables import get_variables

app = Flask(__name__)
# if for some reason your conversation with the chef gets weird, change the secret key 
app.config['SECRET_KEY'] = 'top-secret!v2'
dict_variables = [] # {}
variable = None


@app.route('/loanbot', methods=['POST'])
def loan():
    incoming_msg = request.values['Body']
    #print("incoming_msg = ", incoming_msg)
    #dict_variables[name_variable] = incoming_msg
    chat_log = session.get('chat_log')
    answer = ask(incoming_msg, chat_log)
    #print("answer = ", answer)
    session['chat_log'] = append_interaction_to_chat_log(incoming_msg, answer,
                                                         chat_log)
    # print("the session chat_log = ", chat_log)
    #previous_answer, question = append_interaction_to_chat_log(incoming_msg, answer,
    #                                                     chat_log)
    #name_variable = get_variables(question)
    #dict_variables.append(previous_answer)
    #dict_variables.append(name_variable)
    msg = MessagingResponse()
    msg.message(answer)

    return str(msg)


if __name__ == '__main__':
    app.run(debug=True)
    print("dict_variables")
    print(dict_variables)
