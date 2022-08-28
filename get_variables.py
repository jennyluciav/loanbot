

def get_variables(question):
    type_variable = ""
    if question in ["correo", "email", "e-mail", "correo electrónico"]:
        type_variable = "email"

    if question in ["sexo"]:
        type_variable = "Gender"

    if question in ["dependientes", "dependiente"]:
        type_variable = "Dependents"

    if question in ["educacion", "educación", "grado de educación"]:
        type_variable = "Education"

    if question in ["estado civil", "civil"]:
        type_variable = "Married"

    if question in ["situación laboral", "laboral"]:
        type_variable = "Self_Employed"

    if question in ["salario", "sueldo"]:
        type_variable = "ApplicantIncome"

    if question in ["ingresos del co-aplicante"]:
        type_variable = "CoapplicantIncome"

    if question in ["monto del préstamo", "monto"]:
        type_variable = "LoanAmount"

    if question in ["plazo"]:
        type_variable = "Loan_Amount_Term"

    if question in ["historial crediticio"]:
        type_variable = "Credit_History"

    if question in ["tipo de área"]:
        type_variable = "Property_Area"

    return type_variable
