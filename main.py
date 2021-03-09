import pandas as pd
from faker import Faker
# Create object of the Faker class
fake = Faker()
# Create a dataframe
df = pd.DataFrame(columns=[''])
# Create Columns and fill the Rows of the data frame
for i in range(1, 10000):
    # inserting values in  rows
    df.loc[i, 'First Name'] = fake.first_name()
    df.loc[i, 'Last Name'] = fake.last_name()
    df["FullName"] = df["First Name"] + " " + df["Last Name"].map(str)
    df.loc[i, 'Date of Birth'] = fake.date_between(
        start_date='-16y', end_date='-6y')
    df.loc[i, 'Address'] = fake.address()
    df.loc[i, 'Email'] = fake.email()
# Check Duplication
if (duplicated := df.duplicated(keep=False)).any():
    some_duplicates = df[duplicated].sort_values(
        by=df.columns.to_list()).head()
    print(
        f"Dataframe has one or more duplicated rows, for example:\n{some_duplicates}")

else:
    print("There is no duplication in the data.")
# Create a csv file
df.to_csv('profile.csv')
