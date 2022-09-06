import re 


def get_variables(question):
    type_variable = ""
    question = question.lower()

    if "correo" in question or "email" in question or "e-mail" in question or "correo electrónico" in question:
        type_variable = "email"

    if "sexo" in question:
        type_variable = "Gender"

    if "dependientes" in question or "dependiente" in question:
        type_variable = "Dependents"

    if "educacion" in question or "educación" in question or "grado de educación" in question:
        type_variable = "Education"

    if "estado civil" in question or "civil" in question:
        type_variable = "Married"

    if "situación laboral" in question or "laboral" in question:
        type_variable = "Self_Employed"

    if "salario" in question or "sueldo" in question:
        type_variable = "ApplicantIncome"

    if "ingresos del co-aplicante" in question:
        type_variable = "CoapplicantIncome"

    if "desea solicitar" in question or "monto del préstamo" in question or "monto" in question:
        type_variable = "LoanAmount"

    if "plazo" in question or "desea pagar" in question:
        type_variable = "Loan_Amount_Term"

    if "historial crediticio" in question:
        type_variable = "Credit_History"

    if "tipo de área" in question or "rural" in question or "urban" in question:
        type_variable = "Property_Area"

    return type_variable


def get_values(type_question, answer):
    answer = answer.replace("Persona: ", "").lower()
    value = ""
    if type_question == "email":
        value = re.search(r'[\w.+-]+@[\w-]+\.[\w.-]+', answer).group(0)

    if type_question == "Gender":
        if "femenino" in answer or "mujer" in answer:
            value = "Female"
        elif "masculino" in answer or "hombre" in answer:
            value = "Male"

    if type_question == "Dependents":
        numero = {'uno': 1, 'dos': 2, 'tres': 3, 'cuatro': 4}
        if "ninguno" in answer or "cero" in answer or "no" in answer:
            value = 0
        elif "mucho" in answer:
            value = 4
        else:
            try:
                value = int(answer)
            except Exception:
                print("Error en capturar dependents")
                value = 0
        #elif len(answer) == 1 and int(answer) in list(numero.values()):
        #    for value in str(numero.values()):
        #        start_index = answer.find(value)
        #        extracted_string = answer[start_index:start_index+3]
        #    value = numero[extracted_string]
        #    print("value", value)

    if type_question == "Education":
        if "graduad" in answer or "universitari" in answer or "superior":
            value = "Graduate"
        else:
            value = "Not Graduate"

    if type_question == "Married":
        if "solter" in answer:
            value = "No"
        else:
            value = "Yes"

    if type_question == "Self_Employed":
        if "independiente" in answer or "autónomo" in answer or "autonomo" in answer:
            value = "Yes"
        else:
            value = "No"

    if type_question == "ApplicantIncome":
        salary = [int(s) for s in answer.split() if s.isdigit()]
        if len(salary) == 0:
            salary = re.findall(r'\d+', answer)
        value = int(salary[0])

    if type_question == "CoapplicantIncome":
        cosalary = [int(s) for s in answer.split() if s.isdigit()]
        if len(cosalary) == 0:
            cosalary = re.findall(r'\d+', answer)
        value = float(cosalary[0])

    if type_question == "LoanAmount":
        loanamount = [int(s) for s in answer.split() if s.isdigit()]
        if len(loanamount) == 0:
            loanamount = re.findall(r'\d+', answer) 
        value = float(loanamount[0])

    if type_question == "Loan_Amount_Term":
        loanamountterm = [int(s) for s in answer.split() if s.isdigit()]
        if len(loanamountterm) == 0:
            loanamountterm = re.findall(r'\d+', answer)
        value = float(loanamountterm[0])

    if type_question == "Credit_History":
        if "si" in answer:
            value = 1.0
        else:
            value = 0.0

    if type_question == "Property_Area":
        if "urbano" in answer:
            value = "Urban"
        elif "semiurbano" in answer:
            value = "Semiurban"
        else:
            value = "Rural"

    return value


def get_loan_currency(answer):
    answer = answer.replace("Persona: ", "").lower()
    currency = " ".join(re.findall("[a-zA-Z]+", answer))
    return currency.upper()
