import pandas as pd
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

# Creating a function to appropriately engineer the 'Age' column
def create_age_bins(col):
    '''Engineers age bin variables for pipeline'''

    # Defining / instantiating the necessary variables
    age_bins = [-1, 12, 18, 25, 50, 100]
    age_labels = ['child', 'teen', 'young_adult', 'adult', 'elder']
    age_imputer = SimpleImputer(strategy = 'median')
    age_ohe = OneHotEncoder()

    # Performing basic imputation for nulls
    imputed = age_imputer.fit_transform(col)
    ages_filled = pd.DataFrame(data = imputed, columns = ['Age'])

    # Segregating ages into age bins
    age_cat_cols = pd.cut(ages_filled['Age'], bins = age_bins, labels = age_labels)
    age_cats = pd.DataFrame(data = age_cat_cols, columns = ['Age'])

    # One hot encoding new age bins
    ages_encoded = age_ohe.fit_transform(age_cats[['Age']])
    ages_encoded = pd.DataFrame(data = ages_encoded.toarray())

    return ages_encoded



# Creating function to appropriately engineer the 'Embarked' column
def create_embarked_columns(col):
    '''Engineers the embarked variables for pipeline'''

    # Instantiating the transformer objects
    embarked_imputer = SimpleImputer(strategy = 'most_frequent')
    embarked_ohe = OneHotEncoder()

    # Performing basic imputation for nulls
    imputed = embarked_imputer.fit_transform(col)
    embarked_filled = pd.DataFrame(data = imputed, columns = ['Embarked'])

    # Performing OHE on the col data
    embarked_columns = embarked_ohe.fit_transform(embarked_filled[['Embarked']])
    embarked_columns_df = pd.DataFrame(data = embarked_columns.toarray())

    return embarked_columns_df
