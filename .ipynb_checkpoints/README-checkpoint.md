# Heart-Disease-Analysis

On this dataset, we will be performing a logistic regression to predict whether or not an individual may have heart disease given independent variables such as whether they smoke, have diabetes, BMI, glucose, heart rate, etc.
(Ran logistic regression model)


# Fix this later
Note in the above report the existence of a few hundred null counts, occurring most commonly in the 'education' and 'glucose' fields.

We tackle this issue using scikit-learn's SimpleImputer to fill in missing values. This imputation method is chosen over the K-Nearest Neighbors imputer because each row is independent of its adjacent one.

Taking notice of our problem fields, we observe that we are dealing with continuous, ordinal, and binary fields, which should be handled differently. Ordinal data: 'education' Continuous data: 'cigsPerDay,' 'totChol,' 'BMI,' 'heartRate,' 'glucose' Binary data: 'BPMeds'

Our strategy for handling these missing values is to impute missing ordinal data with the mode, continuous data with the median, and binary data with the mode as well.
