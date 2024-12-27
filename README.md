# Heart-Disease-Analysis

On this dataset, we will be performing a logistic regression to predict whether or not an individual may have heart disease given independent variables such as whether they smoke, have diabetes, BMI, glucose, heart rate, etc.
(Ran logistic regression model)

# TO DO LIST
1. Test 3 models on data before and after imputation. Do this in a data preprocessing notebook
   a. Within this notebook, dig further into the missing values by creating charts
2. Final notebook should explore initial, uncleaned data with an emphasis on missing/redunant values
   a. Describe all of the variables
   b. Dive into the actual EDA portion
   c. Explore why people taking BP Medications have a higher risk of CVD
   d. Show that older people are on BP meds so are already at a higher risk
   e. Investigate education variable (it is negligible)

# Fix this later
Note in the above report the existence of a few hundred null counts, occurring most commonly in the 'education' and 'glucose' fields.

We tackle this issue using scikit-learn's SimpleImputer to fill in missing values. This imputation method is chosen over the K-Nearest Neighbors imputer because each row is independent of its adjacent one.

Taking notice of our problem fields, we observe that we are dealing with continuous, ordinal, and binary fields, which should be handled differently. Ordinal data: 'education' Continuous data: 'cigsPerDay,' 'totChol,' 'BMI,' 'heartRate,' 'glucose' Binary data: 'BPMeds'

Our strategy for handling these missing values is to impute missing ordinal data with the mode, continuous data with the median, and binary data with the mode as well.


# EDA Notes
Males appear to smoke more than females in the dataset
Higher systolic blood pressure correlated with age
Correlation between age ald ten year CHD
Prevalent hypertension correlated with age
sysBP and age trends weakly upwards
