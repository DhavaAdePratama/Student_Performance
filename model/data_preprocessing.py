import joblib
import numpy as np
import pandas as pd

Status =joblib.load('model/encoder_Status.joblib')
Application_mode= joblib.load('model/scaler_Application_mode.joblib')
Mothers_qualification=joblib.load('model/scaler_Mothers_qualification.joblib')
Fathers_qualification = joblib.load('model/scaler_Fathers_qualification.joblib')
Age_at_enrollment = joblib.load('model/scaler_Age_at_enrollment.joblib')
Tuition_fees_up_to_date = joblib.load('model/scaler_Tuition_fees_up_to_date.joblib')
Curricular_units_1st_sem_enrolled = joblib.load('model/scaler_Curricular_units_1st_sem_enrolled.joblib')
Curricular_units_1st_sem_approved = joblib.load('model/scaler_Curricular_units_1st_sem_approved.joblib')
Curricular_units_2nd_sem_enrolled = joblib.load('model/scaler_Curricular_units_2nd_sem_enrolled.joblib')
Curricular_units_2nd_sem_approved = joblib.load('model/scaler_Curricular_units_2nd_sem_approved.joblib')
Curricular_units_1st_sem_evaluations = joblib.load('model/scaler_Curricular_units_1st_sem_evaluations.joblib')
Curricular_units_1st_sem_grade = joblib.load('model/scaler_Curricular_units_1st_sem_grade.joblib')
Curricular_units_2nd_sem_grade = joblib.load('model/scaler_Curricular_units_2nd_sem_grade.joblib')
Curricular_units_2nd_sem_evaluations = joblib.load('model/scaler_Curricular_units_2nd_sem_evaluations.joblib')

def data_preprocessing(data):

    data = data.copy()
    df = pd.DataFrame()
    

    df["status"] = Status.transform(data["status"])[0]

    df["Age_at_enrollment"] = Age_at_enrollment.transform(np.asarray(data["Age_at_enrollment"]).reshape(-1,1))[0]
    data["Application_mode"]= Application_mode.transform(np.asarray(data['Application_mode']).reshape(-1,1))[0]
    data["Mothers_qualification"]= Application_mode.transform(np.asarray(data['Mothers_qualification']).reshape(-1,1))[0]
    data["Fathers_qualification"] = Fathers_qualification.transform(np.asarray(data["Fathers_qualification"]).reshape(-1,1))[0]
    data["Age_at_enrollment"] = Age_at_enrollment.transform(np.asarray(data["Age_at_enrollment"]).reshape(-1,1))[0]
    data["Tuition_fees_up_to_date"] = Tuition_fees_up_to_date.transform(np.asarray(data["Tuition_fees_up_to_date"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_enrolled"] = Curricular_units_1st_sem_enrolled.transform(np.asarray(data["Curricular_units_1st_sem_enrolled"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_approved"] = Curricular_units_1st_sem_approved.transform(np.asarray(data["Curricular_units_1st_sem_approved"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_enrolled"] = Curricular_units_2nd_sem_enrolled.transform(np.asarray(data["Curricular_units_2nd_sem_enrolled"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_approved"] = Curricular_units_2nd_sem_approved.transform(np.asarray(data["Curricular_units_2nd_sem_approved"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_evaluations"] = Curricular_units_1st_sem_evaluations.transform(np.asarray(data["Curricular_units_1st_sem_evaluations"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_grade"] = Curricular_units_1st_sem_grade.transform(np.asarray(data["Curricular_units_1st_sem_grade"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_grade"] = Curricular_units_2nd_sem_grade.transform(np.asarray(data["Curricular_units_2nd_sem_grade"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_evaluations"] = Curricular_units_2nd_sem_evaluations.transform(np.asarray(data["Curricular_units_2nd_sem_evaluations"]).reshape(-1,1))[0]

    return df