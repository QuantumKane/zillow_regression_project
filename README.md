
# **Regression Project - Zillow**

# **Planning the project**
### Goals
The goal of this project is to be able to predict the values of single unit properties that the tax district assesses using the property data from those with a transaction during the months of May-August, 2017.

>Deliverables will include:
> - This repo containing: 
>   - A Jupyter Notebook detailing the process to create this model
>   - Files that hold functions to acquire and prep the data
>   - This Readme.md detailing project planning and exection, as well as instructions for project recreation
>   - Final model created to predict property value
> - Trello Board outlining project steps
> - Slideshow

### Some Context
What are the key factors that impact the value of your home?
According to Marian White from [moving.com](https://www.moving.com/tips/7-key-factors-that-impact-the-value-of-your-home/), the top two factors are location and square footage.
>"Ask any Realtor what the most important factor is when it comes to a 
>home’s value, and they’ll tell you: “location, location, location.” 
>The size of the home is the next important factor in determining 
>the value of your home."

## Inital Questions and Hypotheses
### Questions
- Does square footage affect tax value?
- Are the number of bathrooms related to the house value?
- Are the number of bedrooms related to the house value?
### Hypotheses
### Does square footage affect tax value?
`Null Hypothesis: The average price of homes with 3000 sq.ft. or more is equal to the average price of homes with 3000 sq.ft. or less`
`Alternate Hypothesis: Homes with 3000 sq.ft. or more have higher than average tax dollar count`

### Are the number of bathrooms related to the house value?
`Null Hypothesis: The number of bathrooms is independent to the value of the home`
`Alternate Hypothesis: The number of bathrooms is related to the value of the home`

### Are the number of bedrooms related to the house value?
`Null Hypothesis: The number of bedrooms is independent to the value of the home`
`Alternate Hypothesis: The number of bedrooms is related to the value of the home`

### Data Dictionary

After prepping the dataframe, the variables are the following:

| Feature         | Description                                                |  Data Type 
|-----------------|------------------------------------------------------------|------------
| bathrooms       | Number of bathrooms in home including fractional bathrooms | float64    
| bedrooms        | Number of bedrooms in home                                 | float64     
| square_feet     | Calculated total finished living area of the home          | float64   
| fips            | Federal Information Processing Standard code               | float64    
| longitude       | Longitude of the middle of the parcel                      | float64     
| city            | City in which the property is located (if any)             | float64    
| zip_code        | Zip code in which the property is located                  | float64    
| year_built      | The Year the principal residence was built                 | float64    
| appraisal_value | The total tax assessed value of the parcel                 | float64    
| taxes           | The total property tax assessed for that assessment year   | float64    

****
# **Project Steps**
## Acquire & Prepare
### acquire.py
- Data is acquired from the company SQL database, with credentials required. Functions are stored in the acquire file, which allows quick access to the data. Once the acquire file is imported, it can be used each time to access the data

### prepare.py
- Renamed columns to make them understandable
- Dropped a total of 52 null/NAN, irrelevant, and redundant rows
- Removed outliers from appraisal_value and square_feet

## Explore
- Finding which features have the highest correlation to home value
- Testing initial hypothesis with T-test and correlation tests
- Visualizing variable correlation with plots

## Model
After splitting and exploring the data, we progress to modeling.  
With the train data set, try 3 different regression models, determining which data features and model parameters create better predictions.
- OLS Regression Model
- Lasso/Lars Model
- Polynomial Model

Evaluate the best model on the test data set
### Outcome
- The OLS Regressor and the Lasso/Lars performed equally as well. I decided to use the OLS model.
- The OLS model performed just slightly worse on the test data

# **How to Reproduce**
- Read this README.md
- Download the aquire.py, prepare.py, and zillow_project_report.ipynb into your working directory
- Run the zillow_project_report notebook



