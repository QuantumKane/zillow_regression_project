
# **Regression Project Using Zillow**

## Planning the project
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
Why is customer loyalty important? What is the cost of churn over time?
According to Patrick Campbell from [ProfitWell](https://www.profitwell.com/customer-churn/analysis),
>"Even seemingly small, single-figure increases in churn rate 
>can quickly have a major negative effect on your company’s ability 
>to grow. What’s more, high churn rates are more likely to compound 
>over time."

### Data Dictionary

After prepping the dataframe, the variables are the following:

| Feature                       | Definition                            | Data Type                          |
|-------------------------------|---------------------------------------|------------------------------------|
|contract_type_id               |monthly, year, or two-year             |int - (0-2)                         |
|payment_type_id                |type of payment                        |int - (0-2)                         |
|customer_id                    |unique identifier                      |object                              |
|partner                        |has partner or not                     |int - boolean                       |
|dependents                     |has dependents or not                  |int - boolean                       |
|phone_service                  |one or multiple lines, or no service   |int - (0-2)                         |
|multiple lines                 |multiple lines or not                  |object                              |
|internet_service_type          |DSL, fiber optic, or no service        |object                              |
|online_security_1              |security or not                        |int - boolean                       |
|online_backup                  |backup or not                          |int - boolean                       |
|device_protection              |protection or not                      |int - boolean                       |
|tech_support_1                 |support or not                         |int - boolean                       |
|streaming_tv                   |streaming or not                       |int - boolean                       |
|streaming_movies               |streaming or not                       |int - boolean                       |
|contract_type                  |monthy, 1 year, 2 year                 |object                              |
|paperless_billing              |paperless or mailed bills              |int - boolean                       |
|monthly charges                |in USD                                 |float                               |
|churn                          |customer has left the company or not   |int - boolean                       |
|tenure (months or years)       |length the customer has remained       |int for months, float for years     |
|internet_service_type_id_orig  |DSL, fiber optic, or no service        |int - (0-2)                         |
|tech_support_orig              |tech support or not                    |int - boolean                       |
|internet_service_type_2        |DSL or not                             |int - boolean                       |                 
|internet_service_type_3        |Fiber Optic or not                     |int - boolean                       |
|payment type                   |check or bank transfer                 |object                              |
|online_security_orig           |security or not                        |int - boolean                       |



## Inital Questions and Hypotheses
### Questions
- Does square footage affect tax value?
- ?
### Hypotheses
### Does square footage affect tax value?
`Null Hypothesis: The average price of homes with 4000 sq.ft. or more is equal to the average price of homes with 4000 sq.ft. or less`
`Alternate Hypothesis: Homes with 4000 sq.ft. or more have higher than average tax dollar count`

Is there a difference between the means of monthly_charges for fiber customers who have tech support and those who don't? 
`Null Hypothesis: There is no difference between the means of monthly charges for fiber customers who have tech support and those who don't`
`Alternate Hypothesis: There is a difference between the means of monthly_charges for fiber customers who have tech support and those who don't`

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
- Finding which features have the highest correlation to churn
- Testing hypothesis with T-test
- Visualizing churn with plots

## Model
After splitting and exploring the data, we progress to modeling.  
With the train data set, try four different classification models, determining which data features and model parameters create better predictions.
- 2 different Logistic Regression Models
- Decision Tree
- Random Forest

Evaluate the best model on the test data set
### Outcome
- The first Logistic Regression Model had the best reults, if only slightly
- That model performed even better on the test data

# **How to Reproduce**
- Read this README.md
- Download the aquire.py, prepare.py, and project_report.ipynb into your working directory
- Run the project_report.ipynb notebook



