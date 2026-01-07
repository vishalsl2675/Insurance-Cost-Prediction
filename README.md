# Insurance-Cost-Prediction



This project is a **Machine Learning web application** that predicts **medical insurance costs** based on user details such as age, BMI, number of children, smoking habits, sex, and region.

The model is built using **Linear Regression** and deployed using **Streamlit**, with hosting via **GitHub and Streamlit Cloud**.



##  Live Demo
 *(Add your Streamlit Cloud link here after deployment)*  
Example:  
https://insurance-cost-prediction.streamlit.app



##  Project Overview

Medical insurance costs depend on multiple personal and lifestyle factors.  
This application helps estimate insurance charges using a trained ML model.

##  Dataset Description

The dataset used in this project contains **demographic, lifestyle, and health-related information** of individuals.  
It is designed to predict **medical insurance costs**, making this a **regression problem**.

- **Total Columns:** 11  
- **Target Variable:** `medical_cost`

---

##  Column Details

### `age`
- **Type:** Numerical  
- **Description:** Age of the individual in years  
- **Importance:** Medical costs generally increase with age due to higher healthcare needs.

---

### `sex`
- **Type:** Categorical  
- **Values:** `male`, `female`  
- **Description:** Gender of the individual  
- **Importance:** Used to analyze medical cost differences across genders.

---

### `smoker`
- **Type:** Categorical  
- **Values:** `yes`, `no`  
- **Description:** Smoking status of the individual  
- **Importance:** One of the strongest predictors; smokers usually incur significantly higher medical costs.

---

### `region`
- **Type:** Categorical  
- **Values:** `northeast`, `northwest`, `southeast`, `southwest`  
- **Description:** Residential region of the individual  
- **Importance:** Healthcare costs vary across regions due to lifestyle and medical infrastructure differences.

---

### `blood_pressure`
- **Type:** Numerical  
- **Description:** Blood pressure level of the individual  
- **Importance:** High blood pressure indicates cardiovascular risk, leading to increased medical expenses.  
- **Note:** Contains missing values.

---

### `cholesterol`
- **Type:** Numerical  
- **Description:** Cholesterol level in blood  
- **Importance:** High cholesterol increases the risk of heart-related diseases and long-term medical costs.  
- **Note:** Contains missing values.

---

### `glucose`
- **Type:** Numerical  
- **Description:** Blood glucose level  
- **Importance:** Elevated glucose levels may indicate diabetes, which significantly increases medical costs.  
- **Note:** Contains missing values.

---

### `exercise_hours_per_week`
- **Type:** Numerical  
- **Description:** Number of hours spent exercising per week  
- **Importance:** Higher physical activity generally improves health and reduces medical expenses.

---

### `alcohol_consumption`
- **Type:** Numerical  
- **Description:** Level of alcohol intake  
- **Importance:** Excessive alcohol consumption increases health risks and related medical costs.

---

### `diet_score`
- **Type:** Numerical  
- **Description:** Diet quality score (higher score indicates a healthier diet)  
- **Importance:** A healthy diet reduces the risk of chronic diseases and lowers medical expenses.

---

### `medical_cost` *(Target Variable)*
- **Type:** Numerical  
- **Description:** Total medical insurance cost incurred by the individual  
- **Importance:** This is the target variable that the model predicts.

---

##  Problem Type

- **Machine Learning Task:** Regression  
- **Objective:** Predict medical insurance cost based on health, lifestyle, and demographic features.



###  Output
- Predicted Medical Insurance Cost



##  Machine Learning Model

- **Algorithm**: Linear Regression  
- **Library**: Scikit-learn  
- **Preprocessing**:
  - One-hot encoding using `pd.get_dummies()`
  - Feature alignment using stored training columns
- **Target Variable**: Medical Insurance Cost



##  Tech Stack

- **Python**
- **Pandas**
- **NumPy**
- **Scikit-learn**
- **Streamlit**
- **GitHub**
- **Streamlit Cloud**


