

def clean_zillow(df):
    '''
    This function takes in a dataframe, and performs the following:
    - renames columns to make them understandable
    - sets parcelid as the index
    - drops null/NAN rows
    - removes outliers from tax_value and square_feet
    '''
    df = df.rename(columns={"bedroomcnt": "bedrooms", "bathroomcnt": "bathrooms", "calculatedfinishedsquarefeet": "square_feet", 
                        "taxamount": "taxes", "regionidzip": "zip_code", "taxvaluedollarcnt": "tax_value", 
                        "yearbuilt": "year_built", "regionidcounty": "county"})
    
    
    # Dropping redundant or unnecessary columns
    df = df.drop(['airconditioningtypeid', 'architecturalstyletypeid', 'basementsqft', 'buildingclasstypeid', 'buildingqualitytypeid', 'calculatedbathnbr', 'decktypeid', 'finishedfloor1squarefeet', 'finishedsquarefeet13', 'finishedsquarefeet15', 'finishedsquarefeet50', 'finishedsquarefeet6', 'fireplacecnt', 'garagecarcnt', 'garagetotalsqft', 'hashottuborspa', 'heatingorsystemtypeid', 'poolcnt', 'poolsizesum', 'pooltypeid10', 'pooltypeid2', 'pooltypeid7', 'propertyzoningdesc', 'propertycountylandusecode', 'taxdelinquencyyear', 'taxdelinquencyflag', 'regionidneighborhood', 'threequarterbathnbr', 'fireplaceflag', 'numberofstories', 'yardbuildingsqft26', 'yardbuildingsqft17', 'typeconstructiontypeid', 'unitcnt', 'storytypeid', 'logerror', 'transactiondate', 'id', 'censustractandblock'],axis=1)
    
    df = df.dropna()
    
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