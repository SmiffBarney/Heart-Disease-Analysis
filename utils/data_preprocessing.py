from sklearn.impute import SimpleImputer
import pandas as pd

# Load in CSV file
def load_data(path):
    return pd.read_csv(path)

# Handle null values
def impute_missing_values(df, strategy="mean"):
    imputer = SimpleImputer(strategy=strategy)
    df_imputed = pd.DataFrame(imputer.fit_transform(df), columns=df.columns)
    return df_imputed

