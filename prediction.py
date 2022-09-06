import numpy as np
import pandas as pd
import pickle

MODEL_FILE = "loanmodel.pkl"

def data_processing(loan_dataset):
    loan_dataset = pd.DataFrame(loan_dataset, index=[0])
    loan_dataset = loan_dataset.drop(["email","loan_currency"], axis=1)
    loan_dataset.replace({"Loan_Status": {'N': 0,'Y': 1}}, inplace = True)
    loan_dataset = loan_dataset.replace(to_replace='3+', value=4)
    loan_dataset.replace({'Married':{'No':0,'Yes':1},'Gender':{'Male':1,'Female':0},'Self_Employed':{'No':0,'Yes':1},
                        'Property_Area':{'Rural':0,'Semiurban':1,'Urban':2},'Education':{'Graduate':1,'Not Graduate':0}},inplace=True)
    return loan_dataset

def predict(loan_dataset):
    with open(MODEL_FILE, 'rb') as file:
        pickle_model = pickle.load(file)
        prediction = pickle_model.predict(loan_dataset)
        return prediction[0]
