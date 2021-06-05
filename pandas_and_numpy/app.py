import pandas as pd
people = {
    'First Name' : ['Aditya', 'Palak', 'Divisha'],
    'Last Name' : ['Singh', 'Singh', 'Singh'],
    'Email ID' : ['aditysingh@gmail.com', 'palaksingh@gmail.com', 'divishasingh@gmail.com']
}
df = pd.DataFrame(people)

print(df)

df['First Name'] = df['First Name'].map({'Aditya' : 'Adityaa'})

print(df['First Name'])