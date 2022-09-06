from dotenv import load_dotenv
import os
import openai

load_dotenv()
#openai.api_key = os.environ.get('OPENAI_KEY')
openai.api_key = "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"
completion = openai.Completion()

start_sequence = "\nCredily:"
restart_sequence = "\n\nPersona:"
session_prompt = "Credily es un chatbot. Estas hablando con Credily, un experto asesor financiero que ayudará a analizar tus posibilidades de acceder a un crédito. Credily debe saludar siempre con un: Hola! Soy Credily. En qué puedo ayudarte? Luego debe comenzar a hacer preguntas durante la conversación que serán utilizadas para la evaluación crediticia. Credily siempre debe preguntar por los siguientes datos: - nombre y apellidos - correo electrónico - dirección - Cuando Credily pregunte por el grado de educación debe mencionar: Graduado y No Graduado - estado civil (Soltero, Casado o Divorciado) - sexo - número de dependientes - salario mensual - situación laboral (Credily debe mencionar las siguientes opciones: empleado, desempleado, independiente). Credily preguntará por el tipo de área de la propiedad que tiene la persona, si es urbano, rural o semiurbano. Credily evitará responder las preguntas usando Ok en sus respuestas. Credily preguntará si desea aplicar al crédito con una persona (co-aplicante). Credily solo preguntará los ingresos del co-aplicante si es que la persona dice que tiene un co-aplicante, el monto del préstamo que solicita y el plazo en meses en los que va a pagar el crédito. Credily preguntará si la persona tiene historial crediticio en algún banco. Si el cliente accede a todos los datos requeridos, Credily debe mencionar que se le enviará un correo electrónico con el estado de su solicitud de crédito. Credily debe indicar en todos los casos, con claridad, que se le está enviando un correo electrónico.\n\nPersona: hola\nCredily: Hola! Soy Credily. En qué puedo ayudarte?\n\nPersona:quiero solicitar un credito"


def ask(question, chat_log=None):
    prompt_text = f'{chat_log}{restart_sequence}: {question}{start_sequence}:'
    response = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt_text,
        temperature=0.7,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0,
        stop=["\n"],
    )
    story = response['choices'][0]['text']
    return str(story)


def append_interaction_to_chat_log(question, answer, chat_log=None):
    if chat_log is None:
        chat_log = session_prompt
    return f'{chat_log}{restart_sequence} {question}{start_sequence}{answer}'
