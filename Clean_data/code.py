# --------------
# Importing header files
import numpy as np
import pandas as pd
from scipy.stats import mode 
 
import warnings
warnings.filterwarnings('ignore')


#Reading file
bank_data = pd.read_csv(path)


#Code starts here
categorical_var = bank_data.select_dtypes(include = 'object')
#print(categorical_var)
print(categorical_var.shape)
numerical_var = bank_data.select_dtypes(include = 'number')
#print(numerical_var)
print(numerical_var.shape)

# Step 2
banks = bank_data.copy()
banks.drop(['Loan_ID'], axis=1, inplace=True)
print(banks.isnull().sum())
bank_mode = banks.mode()
print(bank_mode)

banks.fillna(bank_mode.iloc[0], inplace=True)
print(banks.isnull().sum().values.sum())

# Step 3
avg_loan_amount = pd.pivot_table(banks, values = 'LoanAmount', index = ['Gender', 'Married', 'Self_Employed'], aggfunc = np.mean)
print(avg_loan_amount)

# Step 4
loan_approved_se = banks[banks['Self_Employed'] == 'Yes'][banks['Loan_Status'] == 'Y'].count()
#print(loan_approved_se)
percentage_se = loan_approved_se*100/614
print(percentage_se)

loan_approved_nse = banks[banks['Self_Employed'] == 'No'][banks['Loan_Status'] == 'Y'].count()
#print(loan_approved_nse)
percentage_nse = loan_approved_nse*100/614
print(percentage_nse)

# Step 5
loan_term = banks['Loan_Amount_Term']/12
big_loan_term = loan_term[loan_term >= 25].count()
print(big_loan_term)

# Step 6
loan_groupby = banks.groupby('Loan_Status')
loan_groupby = loan_groupby[['ApplicantIncome', 'Credit_History']]
mean_values = loan_groupby.mean()
print(mean_values)
print(mean_values.iloc[1,0])




