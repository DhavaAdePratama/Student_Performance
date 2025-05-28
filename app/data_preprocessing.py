import joblib
import numpy as np
import pandas as pd

Status = joblib.load('model/encoder_Status.joblib')
Application_mode = joblib.load('model/scaler_Application_mode.joblib')
Mothers_qualification = joblib.load('model/scaler_Mothers_qualification.joblib')
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
Marital_status = joblib.load('model/scaler_Marital_status.joblib')
Application_order = joblib.load('model/scaler_Application_order.joblib')
Course = joblib.load('model/scaler_Course.joblib')
Daytime_evening_attendance = joblib.load('model/scaler_Daytime_evening_attendance.joblib')
Previous_qualification = joblib.load('model/scaler_Previous_qualification.joblib')
Previous_qualification_grade = joblib.load('model/scaler_Previous_qualification_grade.joblib')
Nacionality = joblib.load('model/scaler_Nacionality.joblib')
Mothers_occupation = joblib.load('model/scaler_Mothers_occupation.joblib')
Fathers_occupation = joblib.load('model/scaler_Fathers_occupation.joblib')
Admission_grade = joblib.load('model/scaler_Admission_grade.joblib')
Displaced = joblib.load('model/scaler_Displaced.joblib')
Educational_special_needs = joblib.load('model/scaler_Educational_special_needs.joblib')
Debtor = joblib.load('model/scaler_Debtor.joblib')
Gender = joblib.load('model/scaler_Gender.joblib')
Scholarship_holder = joblib.load('model/scaler_Scholarship_holder.joblib')
International = joblib.load('model/scaler_International.joblib')
Curricular_units_1st_sem_credited = joblib.load('model/scaler_Curricular_units_1st_sem_credited.joblib')
Curricular_units_1st_sem_without_evaluations = joblib.load('model/scaler_Curricular_units_1st_sem_without_evaluations.joblib')
Curricular_units_2nd_sem_credited = joblib.load('model/scaler_Curricular_units_2nd_sem_credited.joblib')
Curricular_units_2nd_sem_without_evaluations = joblib.load('model/scaler_Curricular_units_2nd_sem_without_evaluations.joblib')
Unemployment_rate = joblib.load('model/scaler_Unemployment_rate.joblib')
Inflation_rate = joblib.load('model/scaler_Inflation_rate.joblib')
GDP = joblib.load('model/scaler_GDP.joblib')

def data_preprocessing(data):

    data = data.copy()
    df = pd.DataFrame()
    

    df["status"] = Status.transform(data["status"])[0]

    data["Marital_status"] = Marital_status.transform(np.asarray(data["Marital_status"]).reshape(-1,1))[0]
    data["Application_mode"] = Application_mode.transform(np.asarray(data['Application_mode']).reshape(-1,1))[0]
    data["Application_order"] = Application_order.transform(np.asarray(data["Application_order"]).reshape(-1,1))[0]
    data["Course"] = Course.transform(np.asarray(data["Course"]).reshape(-1,1))[0]
    data["Daytime_evening_attendance"] = Daytime_evening_attendance.transform(np.asarray(data["Daytime_evening_attendance"]).reshape(-1,1))[0]
    data["Previous_qualification"] = Previous_qualification.transform(np.asarray(data["Previous_qualification"]).reshape(-1,1))[0]
    data["Previous_qualification_grade"] = Previous_qualification_grade.transform(np.asarray(data["Previous_qualification_grade"]).reshape(-1,1))[0]
    data["Nacionality"] = Nacionality.transform(np.asarray(data["Nacionality"]).reshape(-1,1))[0]
    data["Mothers_qualification"] = Mothers_qualification.transform(np.asarray(data['Mothers_qualification']).reshape(-1,1))[0]
    data["Fathers_qualification"] = Fathers_qualification.transform(np.asarray(data["Fathers_qualification"]).reshape(-1,1))[0]
    data["Mothers_occupation"] = Mothers_occupation.transform(np.asarray(data["Mothers_occupation"]).reshape(-1,1))[0]
    data["Fathers_occupation"] = Fathers_occupation.transform(np.asarray(data["Fathers_occupation"]).reshape(-1,1))[0]
    data["Admission_grade"] = Admission_grade.transform(np.asarray(data["Admission_grade"]).reshape(-1,1))[0]
    data["Displaced"] = Displaced.transform(np.asarray(data["Displaced"]).reshape(-1,1))[0]
    data["Educational_special_needs"] = Educational_special_needs.transform(np.asarray(data["Educational_special_needs"]).reshape(-1,1))[0]
    data["Debtor"] = Debtor.transform(np.asarray(data["Debtor"]).reshape(-1,1))[0]
    data["Tuition_fees_up_to_date"] = Tuition_fees_up_to_date.transform(np.asarray(data["Tuition_fees_up_to_date"]).reshape(-1,1))[0]
    data["Gender"] = Gender.transform(np.asarray(data["Gender"]).reshape(-1,1))[0]
    data["Scholarship_holder"] = Scholarship_holder.transform(np.asarray(data["Scholarship_holder"]).reshape(-1,1))[0]
    data["Age_at_enrollment"] = Age_at_enrollment.transform(np.asarray(data["Age_at_enrollment"]).reshape(-1,1))[0]
    data["International"] = International.transform(np.asarray(data["International"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_credited"] = Curricular_units_1st_sem_credited.transform(np.asarray(data["Curricular_units_1st_sem_credited"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_enrolled"] = Curricular_units_1st_sem_enrolled.transform(np.asarray(data["Curricular_units_1st_sem_enrolled"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_evaluations"] = Curricular_units_1st_sem_evaluations.transform(np.asarray(data["Curricular_units_1st_sem_evaluations"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_approved"] = Curricular_units_1st_sem_approved.transform(np.asarray(data["Curricular_units_1st_sem_approved"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_grade"] = Curricular_units_1st_sem_grade.transform(np.asarray(data["Curricular_units_1st_sem_grade"]).reshape(-1,1))[0]
    data["Curricular_units_1st_sem_without_evaluations"] = Curricular_units_1st_sem_without_evaluations.transform(np.asarray(data["Curricular_units_1st_sem_without_evaluations"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_credited"] = Curricular_units_2nd_sem_credited.transform(np.asarray(data["Curricular_units_2nd_sem_credited"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_enrolled"] = Curricular_units_2nd_sem_enrolled.transform(np.asarray(data["Curricular_units_2nd_sem_enrolled"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_evaluations"] = Curricular_units_2nd_sem_evaluations.transform(np.asarray(data["Curricular_units_2nd_sem_evaluations"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_approved"] = Curricular_units_2nd_sem_approved.transform(np.asarray(data["Curricular_units_2nd_sem_approved"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_grade"] = Curricular_units_2nd_sem_grade.transform(np.asarray(data["Curricular_units_2nd_sem_grade"]).reshape(-1,1))[0]
    data["Curricular_units_2nd_sem_without_evaluations"] = Curricular_units_2nd_sem_without_evaluations.transform(np.asarray(data["Curricular_units_2nd_sem_without_evaluations"]).reshape(-1,1))[0]
    data["Unemployment_rate"] = Unemployment_rate.transform(np.asarray(data["Unemployment_rate"]).reshape(-1,1))[0]
    data["Inflation_rate"] = Inflation_rate.transform(np.asarray(data["Inflation_rate"]).reshape(-1,1))[0]
    data["GDP"] = GDP.transform(np.asarray(data["GDP"]).reshape(-1,1))[0]


    return df.pd.DataFrame([data]) 