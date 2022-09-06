import pandas as pd
from get_variables import get_variables, get_values, get_loan_currency
from prediction import data_processing, predict

MODEL_VARIABLES = ["Gender", "Married", "Dependents", "Education", "Self_Employed", 
                "ApplicantIncome", "CoapplicantIncome", "LoanAmount", "Loan_Amount_Term", 
                "Credit_History", "Property_Area"]

class LoanProcessing:
    def __init__(self, filename):
        self.filename = filename

    def process_chat_history(self):
        with open(self.filename, 'r') as chat:
            data = chat.read()
            data_cleaned = [line for line in data.split('\n') if line.strip() != '']
            data_cleaned.pop(0)
            data_cleaned.pop(0)
            data_cleaned.pop(0)
            data_cleaned.pop(0)
        return data_cleaned


    def get_values_dict(self, data_cleaned):
        variables_dict = {}
        for index, item in enumerate(data_cleaned):
            if "Credily" in item:
                type_question = get_variables(item)
                if type_question and type_question not in variables_dict.keys():
                    value = get_values(type_question, data_cleaned[index+1])
                    variables_dict[type_question] = value
                if type_question == "LoanAmount":
                    variables_dict["loan_currency"] = get_loan_currency(data_cleaned[index+1])
                if "CoapplicantIncome" not in list(variables_dict.keys()):
                    variables_dict["CoapplicantIncome"] = 0.0
        return variables_dict

if __name__ == '__main__':
    filename = "chat_log_6.txt"
    lp = LoanProcessing(filename)
    data_cleaned = lp.process_chat_history()
    variables_dict = lp.get_values_dict(data_cleaned)
    data_processed = data_processing(variables_dict)
    print("Prediction", predict(data_processed))
    print("Moneda:", variables_dict["loan_currency"])
    print("Email:", variables_dict["email"])
