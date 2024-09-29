import pickle
import streamlit as st
#from streamlit_option_menu import option_menu


# Page config
st.set_page_config(
    page_title="Disease Prediction",
    page_icon="🏥",
    layout="wide"

)

# Centering the title
st.markdown(
    """
    <style>
    .centered-title {
        display: flex;
        justify-content: center;
        align-items: center;
        height: 100%;
        font-size: 40px;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.markdown('<div class="centered-title">NCD Prediction System</div>', unsafe_allow_html=True)
st.markdown('<div class="centered-title">(Non Communicable Diseases)</div>', unsafe_allow_html=True)
# Introduction text
st.markdown('<p class="intro-text">Welcome to the Non-Communicable Disease (NCD) Prediction System. This platform helps in predicting various NCDs such as Diabetes, Heart Disease, Cancer, and more, using advanced machine learning models. Please select a disease from the sidebar to get started.</p>', unsafe_allow_html=True)

# loading the saved models

diabetes_model = pickle.load(open('models/diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('models/heart_disease_model.sav', 'rb'))

cancer_model = pickle.load(open('models/cancer_model.sav', 'rb'))

#respiratory_model = pickle.load(open('models/respiratory_model.sav', 'rb'))

#hypertension_model = pickle.load(open('models/hypertension_model.sav', 'rb'))

#kidney_model = pickle.load(open('models/kidney_model.sav', 'rb'))

#mental_health_model = pickle.load(open('models/mental_health_model.predict.sav', 'rb'))

# Sidebar for navigation

selected = st.selectbox(
    'Dashboard',
    ['Home', 'Diabetes', 'Heart Disease', "Cancer", "Respiratory Disease", "Hypertension", "Chronic Kidney Disease", "Mental Health Disorders", "Chronic Liver Disease", "Obesity", "Arthritis"],
    index=0
)

# Navigation Icons for display
nav_icons = {
    'Home': 'house-fill',
    'Diabetes': 'capsule-pill',
    'Heart Disease': 'heart-pulse-fill',
    'Cancer': 'capsule-pill',  # same as Diabetes, can change if desired
    'Respiratory Disease': 'lungs-fill',
    'Hypertension': 'activity',  # use 'activity' for high blood pressure
    'Chronic Kidney Disease': 'droplet-half',  # water drop can symbolize kidneys
    'Mental Health Disorders': 'emoji-frown',  # sad face
    'Chronic Liver Disease': 'wine',  # wine glass can symbolize liver
    'Obesity': 'graph-up',  # growth chart
    'Arthritis': 'joint'  # bone/joint icon
}

# Display the selected icon
#st.sidebar.write(f"Selected: {selected} ({nav_icons[selected]})")


# Diabetes Prediction Page
if selected == 'Home':
   # st.title('Disease Prediction System')
    st.image('assets/Health.gif')
    
if selected == 'Diabetes':

    # page title
    st.title('💊Diabetes')

    # getting the input data from the user
    col1, col2, col3 = st.columns(3)

    with col1:
        Pregnancies = st.number_input('Number of Pregnancies',min_value=0,max_value=15)

    with col2:
        Glucose = st.number_input('Glucose Level',min_value=0,max_value=200)

    with col3:
        BloodPressure = st.number_input('Blood Pressure value',min_value=0,max_value=200)

    with col1:
        SkinThickness = st.number_input('Skin Thickness value',min_value=0,max_value=50)

    with col2:
        Insulin = st.number_input('Insulin Level',min_value=0,max_value=100)

    with col3:
        BMI = st.number_input('BMI value',min_value=0.0,max_value=50.0,step=0.1)

    with col1:
        DiabetesPedigreeFunction = st.number_input(
            'Diabetes Pedigree Function value',min_value=0.0,max_value=50.0, step=0.01)

    with col2:
        Age = st.number_input('Age of the Person',min_value=0,max_value=100)

    # code for Prediction
    diab_diagnosis = ''

    # creating a button for Prediction

    if st.button('Diabetes Test Result'):
        diab_prediction = diabetes_model.predict(
            [[Pregnancies, Glucose, BloodPressure, SkinThickness, Insulin, BMI, DiabetesPedigreeFunction, Age]])

        if diab_prediction[0] == 1:
            diab_diagnosis = 'The person is diabetic'
        else:
            diab_diagnosis = 'The person is not diabetic'

    st.success(diab_diagnosis)


# Heart Disease Prediction Page
if selected == 'Heart Disease':

    # page title
    st.title('❤️Heart Disease')

    col1, col2, col3 = st.columns(3)

    with col1:
        age = st.number_input('Age',min_value=0,max_value=100)

    with col2:
        sex = st.number_input('Sex',min_value=0,max_value=1)

    with col3:
        cp = st.number_input('Chest Pain types',min_value=0,max_value=3)

    with col1:
        trestbps = st.number_input('Resting Blood Pressure',min_value=94,max_value=200)

    with col2:
        chol = st.number_input('Serum Cholesterol in mg/dl',min_value=126,max_value=564)

    with col3:
        fbs = st.number_input('Fasting Blood Sugar > 120 mg/dl',min_value=0,max_value=1)

    with col1:
        restecg = st.number_input('Resting Electrocardiograph results',min_value=0,max_value=2)

    with col2:
        thalach = st.number_input('Maximum Heart Rate achieved',min_value=71,max_value=202)

    with col3:
        exang = st.number_input('Exercise Induced Angina',min_value=0,max_value=1)

    with col1:
        oldpeak = st.number_input('ST depression induced by exercise',min_value=0.0,max_value=7.0, step=0.1)

    with col2:
        slope = st.number_input('Slope of the peak exercise ST segment',min_value=0,max_value=3)

    with col3:
        ca = st.number_input('Major vessels colored by fluoroscopy',min_value=0,max_value=3)

    with col1:
        thal = st.number_input(
            'thal: 0 = normal; 1 = fixed defect; 2 = reversible defect',min_value=0,max_value=2)

    # code for Prediction
    heart_diagnosis = ''

    # creating a button for Prediction

    if st.button('Heart Disease Test Result'):
        heart_prediction = heart_disease_model.predict(
            [[age, sex, cp, trestbps, chol, fbs, restecg, thalach, exang, oldpeak, slope, ca, thal]])

        if heart_prediction[0] == 1:
            heart_diagnosis = 'The person is having heart disease'
        else:
            heart_diagnosis = 'The person does not have any heart disease'

    st.success(heart_diagnosis)


# Cancer Disease Prediction Page
if selected == 'Cancer':

    # page title
    st.title(":cancer: Cancer Disease")

    col1, col2, col3 = st.columns(3)

    with col1:
        Clump_Thickness = st.number_input('Clump Thickness',min_value=0,max_value=100)

    with col2:
        Uniformity_of_Cell_Size = st.number_input('Uniformity of Cell Size',min_value=0,max_value=100)

    with col3:
        Uniformity_of_Cell_Shape = st.number_input('Uniformity of Cell Shape',min_value=0,max_value=100)

    with col1:
        Marginal_Adhesion = st.number_input('Marginal Adhesion',min_value=0,max_value=200)

    with col2:
        Single_Epithelial_Cell_Size = st.number_input('Single_Epithelial_Cell_Size',min_value=0,max_value=564)

    with col3:
        Bare_Nuclei = st.number_input('Bare Nuclei',min_value=0,max_value=100)

    with col1:
        Bland_Chromatin = st.number_input('Bland Chromatin',min_value=0,max_value=100)

    with col2:
        Normal_Nucleoli = st.number_input('Normal Nucleoli',min_value=0,max_value=202)

    with col3:
        Mitoses = st.number_input('Mitoses',min_value=0,max_value=100)

    # code for Prediction
    cancer_diagnosis = ''

    # creating a button for Prediction

    if st.button('Cancer Disease Test Result'):
        cancer_prediction = cancer_model.predict(
            [[Clump_Thickness, Uniformity_of_Cell_Size, Uniformity_of_Cell_Shape, Marginal_Adhesion, Single_Epithelial_Cell_Size, Bare_Nuclei, Bland_Chromatin, Normal_Nucleoli, Mitoses]])

        if cancer_prediction[0] == 1:
            cancer_diagnosis = 'The person is having cancer disease'
        else:
            cancer_diagnosis = 'The person does not have cancer disease'

    st.success(cancer_diagnosis)
    

# Respiratory Disease Prediction Page
if selected == 'Respiratory Disease':

    # page title
    st.title(":lungs: Respiratory Disease")

    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.number_input('Age', min_value=0, max_value=120)

    with col2:
        Smoking_History = st.number_input('Smoking History (years)', min_value=0, max_value=100)

    with col3:
        Shortness_of_Breath = st.number_input('Shortness of Breath (1-10 scale)', min_value=1, max_value=10)

    with col1:
        Chest_Pain = st.number_input('Chest Pain (1-10 scale)', min_value=1, max_value=10)

    with col2:
        Cough_Severity = st.number_input('Cough Severity (1-10 scale)', min_value=1, max_value=10)

    with col3:
        Sputum_Production = st.number_input('Sputum Production (1-10 scale)', min_value=1, max_value=10)

    with col1:
        Wheezing = st.number_input('Wheezing (1-10 scale)', min_value=1, max_value=10)

    with col2:
        Fever = st.number_input('Fever (degrees Celsius)', min_value=35, max_value=42)

    with col3:
        Fatigue = st.number_input('Fatigue (1-10 scale)', min_value=1, max_value=10)

    # code for Prediction
    respiratory_diagnosis = ''

    # creating a button for Prediction
    if st.button('Respiratory Disease Test Result'):
        respiratory_prediction = respiratory_model.predict(
            [[Age, Smoking_History, Shortness_of_Breath, Chest_Pain, Cough_Severity, Sputum_Production, Wheezing, Fever, Fatigue]])

        if respiratory_prediction[0] == 1:
            respiratory_diagnosis = 'The person is having a respiratory disease'
        else:
            respiratory_diagnosis = 'The person does not have a respiratory disease'

    st.success(respiratory_diagnosis)
    
    
    
    # Hypertension Prediction Page
if selected == 'Hypertension':

    # page title
    st.title(":activity: Hypertension")

    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.number_input('Age', min_value=0, max_value=120)

    with col2:
        BMI = st.number_input('Body Mass Index (BMI)', min_value=0.0, max_value=100.0, format="%.1f")

    with col3:
        Smoking_History = st.number_input('Smoking History (years)', min_value=0, max_value=100)

    with col1:
        Physical_Activity_Level = st.number_input('Physical Activity Level (hours per week)', min_value=0, max_value=168)

    with col2:
        Family_History_of_Hypertension = st.selectbox('Family History of Hypertension', ['Yes', 'No'])

    with col3:
        Alcohol_Consumption = st.number_input('Alcohol Consumption (drinks per week)', min_value=0, max_value=100)

    with col1:
        Sodium_Intake = st.number_input('Sodium Intake (mg per day)', min_value=0, max_value=10000)

    with col2:
        Potassium_Intake = st.number_input('Potassium Intake (mg per day)', min_value=0, max_value=10000)

    with col3:
        Stress_Level = st.number_input('Stress Level (1-10 scale)', min_value=1, max_value=10)

    # code for Prediction
    hypertension_diagnosis = ''

    # creating a button for Prediction
    if st.button('Hypertension Test Result'):
        hypertension_prediction = hypertension_model.predict(
            [[Age, BMI, Smoking_History, Physical_Activity_Level, 1 if Family_History_of_Hypertension == 'Yes' else 0, Alcohol_Consumption, Sodium_Intake, Potassium_Intake, Stress_Level]])

        if hypertension_prediction[0] == 1:
            hypertension_diagnosis = 'The person is having hypertension'
        else:
            hypertension_diagnosis = 'The person does not have hypertension'

    st.success(hypertension_diagnosis)


# Chronic Kidney Disease Prediction Page
if selected == 'Chronic Kidney Disease':

    # page title
    st.title(":droplet-half: Chronic Kidney Disease")

    col1, col2, col3 = st.columns(3)

    with col1:
        Age = st.number_input('Age', min_value=0, max_value=120)

    with col2:
        Blood_Pressure = st.number_input('Blood Pressure (mm Hg)', min_value=0, max_value=300)

    with col3:
        Specific_Gravity = st.number_input('Specific Gravity (1.005 - 1.025)', min_value=1.005, max_value=1.025, format="%.3f")

    with col1:
        Albumin = st.number_input('Albumin (g/dL)', min_value=0, max_value=10)

    with col2:
        Sugar = st.number_input('Sugar (mg/dL)', min_value=0, max_value=500)

    with col3:
        Red_Blood_Cells = st.selectbox('Red Blood Cells', ['Normal', 'Abnormal'])

    with col1:
        Pus_Cell = st.selectbox('Pus Cell', ['Normal', 'Abnormal'])

    with col2:
        Serum_Creatinine = st.number_input('Serum Creatinine (mg/dL)', min_value=0.0, max_value=15.0, format="%.1f")

    with col3:
        Hemoglobin = st.number_input('Hemoglobin (g/dL)', min_value=0, max_value=20)

    with col1:
        Packed_Cell_Volume = st.number_input('Packed Cell Volume', min_value=0, max_value=100)

    with col2:
        White_Blood_Cell_Count = st.number_input('White Blood Cell Count (cells/cmm)', min_value=0, max_value=20000)

    with col3:
        Red_Blood_Cell_Count = st.number_input('Red Blood Cell Count (millions/cmm)', min_value=0.0, max_value=10.0, format="%.1f")

    # code for Prediction
    kidney_diagnosis = ''

    # creating a button for Prediction
    if st.button('Chronic Kidney Disease Test Result'):
        kidney_prediction = kidney_model.predict(
            [[Age, Blood_Pressure, Specific_Gravity, Albumin, Sugar, 1 if Red_Blood_Cells == 'Abnormal' else 0,
              1 if Pus_Cell == 'Abnormal' else 0, Serum_Creatinine, Hemoglobin, Packed_Cell_Volume, White_Blood_Cell_Count, Red_Blood_Cell_Count]])

        if kidney_prediction[0] == 1:
            kidney_diagnosis = 'The person is having chronic kidney disease'
        else:
            kidney_diagnosis = 'The person does not have chronic kidney disease'

    st.success(kidney_diagnosis)


# Mental Health Disorders Prediction Page
if selected == 'Mental Health Disorders':

    # Page title
    st.title(":emoji-frown: Mental Health Disorders")

    col1, col2, col3 = st.columns(3)

    with col1:
        Stress_Level = st.slider('Stress Level', min_value=0, max_value=10, step=1)

    with col2:
        Sleep_Quality = st.slider('Sleep Quality', min_value=0, max_value=10, step=1)

    with col3:
        Mood_Swings = st.slider('Mood Swings', min_value=0, max_value=10, step=1)

    with col1:
        Anxiety = st.slider('Anxiety', min_value=0, max_value=10, step=1)

    with col2:
        Depression = st.slider('Depression', min_value=0, max_value=10, step=1)

    with col3:
        Social_Isolation = st.slider('Social Isolation', min_value=0, max_value=10, step=1)

    with col1:
        Substance_Use = st.slider('Substance Use', min_value=0, max_value=10, step=1)

    with col2:
        Physical_Activity = st.slider('Physical Activity', min_value=0, max_value=10, step=1)

    with col3:
        Diet_Quality = st.slider('Diet Quality', min_value=0, max_value=10, step=1)

    # Code for Prediction
    mental_health_diagnosis = ''

    # Creating a button for Prediction
    if st.button('Predict Mental Health Disorder'):
        mental_health_prediction = mental_health_model.predict([[Stress_Level, Sleep_Quality, Mood_Swings, Anxiety, Depression, Social_Isolation, Substance_Use, Physical_Activity, Diet_Quality]])
        if mental_health_prediction[0] == 1:
            mental_health_diagnosis = 'The person is predicted to have a mental health disorder'
        else:
            mental_health_diagnosis = 'The person is predicted to not have a mental health disorder'

    st.success(mental_health_diagnosis)
