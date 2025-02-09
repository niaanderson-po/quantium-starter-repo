import os   
import pandas as pd 
import glob
os.chdir(os.path.dirname(os.path.abspath(__file__)))

file_path = "/Users/niaapple/Desktop/VSCode/quantium-starter-repo/data"
csv_files = glob.glob('*.{}'.format('csv'))

df= pd.concat([pd.read_csv(f) for f in csv_files ], ignore_index=True)

df['price'] = df['price'].str.replace('$', '')
df['price'] = df['price'].astype(float).astype(int)
df['sales'] = df.price.mul(df.quantity)

value_to_keep = 'pink morsel'
column_to_check = 'product'
filtered_df = df[df[column_to_check] == value_to_keep].copy()
filtered_df.set_index('product', inplace=True) 

df = filtered_df[['sales', 'date', 'region']]
print(df)

