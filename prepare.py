# imports needed
from sklearn.model_selection import train_test_split 

def clean_zillow(df):
    '''
    This function takes in a dataframe, and performs the following:
    - renames columns to make them understandable
    - sets parcelid as the index
    - drops null/NAN rows
    - removes outliers from tax_value and square_feet
    '''
    # Rename some columns for ease-of-use
    df = df.rename(columns={"bedroomcnt": "bedrooms", "bathroomcnt": "bathrooms", "calculatedfinishedsquarefeet": "square_feet", 
                        "taxamount": "taxes", "regionidzip": "zip_code", "taxvaluedollarcnt": "tax_value", 
                        "yearbuilt": "year_built", "regionidcounty": "county"})
    
    
    # Drop redundant or unnecessary columns
    df = df.drop(['airconditioningtypeid', 'architecturalstyletypeid', 'basementsqft', 'buildingclasstypeid', 'buildingqualitytypeid', 'calculatedbathnbr', 'decktypeid', 'finishedfloor1squarefeet', 'finishedsquarefeet13', 'finishedsquarefeet15', 'finishedsquarefeet50', 'finishedsquarefeet6', 'fireplacecnt', 'garagecarcnt', 'garagetotalsqft', 'hashottuborspa', 'heatingorsystemtypeid', 'poolcnt', 'poolsizesum', 'pooltypeid10', 'pooltypeid2', 'pooltypeid7', 'propertyzoningdesc', 'propertycountylandusecode', 'taxdelinquencyyear', 'taxdelinquencyflag', 'regionidneighborhood', 'threequarterbathnbr', 'fireplaceflag', 'numberofstories', 'yardbuildingsqft26', 'yardbuildingsqft17', 'typeconstructiontypeid', 'unitcnt', 'storytypeid', 'logerror', 'transactiondate', 'id', 'censustractandblock'],axis=1)
    
    # Remove decimals from latitude and longitude
    df['latitude'] = df['latitude'].astype(int)
    df['longitude'] = df['longitude'].astype(int)
    
    # Convert lat and long to positional/standard-format datapoints
    df['latitude'] = df['latitude'].apply(lambda x: x / 10 ** (len((str(x))) - 2))
    df['longitude'] = df['longitude'].apply(lambda x: x / 10 ** (len((str(x))) - 4))
    
    # Drop the nulls
    df = df.dropna()
    
    # Calling remove_outliers to address two columns
    upper_bound, lower_bound = remove_outlier(df, "tax_value")
    df = df[df.tax_value < upper_bound]
    
    upper_bound, lower_bound = remove_outlier(df, "square_feet")
    df = df[df.square_feet < upper_bound]
    
    return df


def remove_outlier(df, feature):
    '''
    This function takes in a dataframe's features and performs the following:
    - calculates its 1st and 3rd quartiles
    - uses their diference to calculate the IQR
    - uses the IQR to determine upper and lower bounds
    '''
    q1 = df[feature].quantile(.25)
    q3 = df[feature].quantile(.75)
    
    iqr = q3 - q1
    
    upper_bound = q3 + (1.5 * iqr)
    lower_bound = q1 - (1.5 * iqr)
    
    return upper_bound, lower_bound


def train_test_validate(df): 
    '''
    This functon taakes in a dataframe, splits the
    data into train, validate, and test, and then scales the data 
    '''
    # First split:
    # Split into train, validate, and test sets
    train_and_validate, test = train_test_split(df, test_size = .10, random_state=123)
    train, validate = train_test_split(train_and_validate, test_size = .20, random_state=123)

    # These two print functions allow us to ensure the data is properly split
    # Print the shape of each set when running the function
    print("train shape: ", train.shape, ", validate shape: ", validate.shape, ", test shape: ", test.shape)

    # Print the shape of each variable as a percentage of the total data set
    total = df.count()[0]
    print("\ntrain percent: ", round(((train.shape[0])/total),2) * 100, 
            ", validate percent: ", round(((validate.shape[0])/total),2) * 100, 
            ", test percent: ", round(((test.shape[0])/total),2) * 100) 

    # Then Scale:
    # Create the Scaling Object
    scaler = sklearn.preprocessing.StandardScaler()

    # Fit to the train data only
    scaler.fit(train.drop('tax_value', axis=1))

    # Use the object on the whole df
    # this returns an array, so we convert to df in the same line
    train_scaled = pd.DataFrame(scaler.transform(train.drop('tax_value', axis=1)))
    validate_scaled = pd.DataFrame(scaler.transform(validate.drop('tax_value', axis=1)))
    test_scaled = pd.DataFrame(scaler.transform(test.drop('tax_value', axis=1)))

    # the result of changing an array to a df resets the index and columns
    # for each train, validate, and test, change the index and columns back to original values

    # Train
    train_scaled.index = train.index
    train_scaled.columns = ['bathrooms_scaled','bedrooms_scaled','square_feet_scaled']
    train = pd.concat((train, train_scaled), axis=1)

    # Validate
    validate_scaled.index = validate.index
    validate_scaled.columns = ['bathrooms_scaled','bedrooms_scaled','square_feet_scaled']
    validate = pd.concat((validate, validate_scaled), axis=1)

    # Test
    test_scaled.index = test.index
    test_scaled.columns = ['bathrooms_scaled','bedrooms_scaled','square_feet_scaled']
    test = pd.concat((test, test_scaled), axis=1)

    return train, validate, test