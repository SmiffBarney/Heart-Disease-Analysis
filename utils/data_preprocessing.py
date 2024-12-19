from sklearn.impute import SimpleImputer
import pandas as pd

# Read in raw data
df = pd.read_csv("data/framingham.csv")

# Handle missing continuous data
cont_to_impute = ['glucose', 'cigsPerDay', 'totChol', 'BMI', 'heartRate']
cont_imputer = SimpleImputer(strategy='median')
df[cols_to_impute] = cont_imputer.fit_transform(df[cols_to_impute])

# Handle missing ordinal/binary data
ord_to_impute = ['education', 'BPMeds']
ord_imputer = SimpleImputer(strategy='most_frequent')
df[ord_to_impute] = ord_imputer.fit_transform(df[ord_to_impute])

# Output processed dataset
df.to_csv('data/cleaned_data.csv', index=False)