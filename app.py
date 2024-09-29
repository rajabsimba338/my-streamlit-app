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

diabetes_model = pickle.load(open('diabetes_model.sav', 'rb'))

heart_disease_model = pickle.load(open('heart_disease_model.sav', 'rb'))

cancer_model = pickle.load(open('cancer_model.sav', 'rb'))



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
    

