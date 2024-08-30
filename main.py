import streamlit as st

# Function to detect male body shape
def detect_body_shape_male(shoulder, chest, waist, hip):
    shoulder_chest_ratio = shoulder / chest
    chest_waist_ratio = chest / waist
    waist_hip_ratio = waist / hip

    lower_threshold = 0.95
    upper_threshold = 1.05

    if (lower_threshold <= shoulder_chest_ratio <= upper_threshold) and \
       (lower_threshold <= chest_waist_ratio <= upper_threshold) and \
       (lower_threshold <= waist_hip_ratio <= upper_threshold):
        return 'Rectangular'
    elif shoulder_chest_ratio < 1 and chest_waist_ratio < 1 and waist_hip_ratio < 1:
        return 'Triangle'
    elif shoulder_chest_ratio > 1 and chest_waist_ratio > 1 and waist_hip_ratio > 1:
        return 'Inverted Triangle'
    elif shoulder_chest_ratio < 1 and chest_waist_ratio > 1 and waist_hip_ratio > 1:
        return 'Trapezoid'
    elif shoulder_chest_ratio < 1 and chest_waist_ratio < 1 and waist_hip_ratio > 1:
        return 'Oval'
    else:
        return 'Undefined'

# Function to detect female body shape
def detect_body_shape_female(shoulder, chest, waist, hip):
    shoulder_hip_ratio = shoulder / hip
    chest_hip_ratio = chest / hip
    chest_waist_ratio = chest / waist
    hip_waist_ratio = hip / waist

    lower_threshold = 0.95
    upper_threshold = 1.05

    if 0.9 <= shoulder_hip_ratio <= 1 and \
       1.001 <= chest_hip_ratio < 1.1 and \
       0.98 <= chest_waist_ratio < 1.1 and \
       hip_waist_ratio < 1:
        return 'Apple'
    elif chest_waist_ratio >= 1.02 and \
         hip_waist_ratio >= 1.02:
        return 'Hourglass'
    elif shoulder_hip_ratio > 1 and \
         chest_hip_ratio > 1 and \
         chest_waist_ratio > 1 and \
         hip_waist_ratio < 1:
        return 'Inverted Triangle'
    elif hip_waist_ratio > 1:
        return 'Pear'
    elif (lower_threshold <= shoulder_hip_ratio <= upper_threshold) and \
         (lower_threshold <= chest_hip_ratio <= upper_threshold) and \
         (lower_threshold <= chest_waist_ratio <= upper_threshold) and \
         (lower_threshold <= hip_waist_ratio <= upper_threshold):
        return 'Rectangle'
    else:
        return 'Undefined'

# Streamlit app layout
st.title("Body Shape Classification")

# User selects gender
gender = st.radio("Select Gender:", ("Male", "Female"))

# Input fields for measurements
shoulder = st.number_input("Enter Shoulder Width (in inches):", min_value=0.0, format="%.2f")
chest = st.number_input("Enter Chest Size (in inches):", min_value=0.0, format="%.2f")
waist = st.number_input("Enter Waist Size (in inches):", min_value=0.0, format="%.2f")
hip = st.number_input("Enter Hip Size (in inches):", min_value=0.0, format="%.2f")

# Prediction button
if st.button("Predict Body Shape"):
    if gender == "Male":
        body_shape = detect_body_shape_male(shoulder, chest, waist, hip)
    else:
        body_shape = detect_body_shape_female(shoulder, chest, waist, hip)
    
    st.success(f"The detected body shape is: {body_shape}")
