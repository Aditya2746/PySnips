import pandas as pd 
people = {
    'First Name' : ['Aditya', 'Palak', 'Divisha'],
    'Last Name' : ['Singh', 'Singh', 'Singh'],
    'Email ID' : ['aditysingh@gmail.com', 'palaksingh@gmail.com', 'divishasingh@gmail.com']
}

def update_email(email):
    return email.lower()

df = pd.DataFrame(people)

# df.columns = ['first_name', 'last_name', 'Email ID']
 
# df.columns = [x.capitalize() for x in df.columns]

# df.columns = df.columns.str.replace(' ', '_')

df.rename(columns={'First Name' : 'First', 'Last Name' :'Last', 'Email ID' : 'Email'}, inplace=True)

df.loc[3] = ['John', 'Smith', 'JohnSmith@Email ID.com']

df.loc[3, ['Last', 'Email']] = ['Doe', 'JohnDoe@Email ID.com']

df.loc[2, 'Last'] = 'Smith'

filt = (df['Email'] == 'JohnDoe@Email ID.com')

df.loc[filt, 'Last'] = 'Smith'

df['Email'] = df['Email'].apply(update_email)

df['First'] = df['First'].replace({'Aditya': 'Chris', 'Palak': 'Mary'})

df['First'] = df['First'].map({'Chris' : 'Aditya', 'Mary':'Palak', 'Divisha':'Divisha', 'John':'John'})



'''Printing Section'''
print(df)
print(df.columns)
print(df['Email'].apply(len))
print(df.apply(len, axis='columns'))
print(df.apply(len))
print(df.apply(pd.Series.min))
print(df.applymap(len))
print(df.applymap(str.lower))
print(df.applymap(update_email))