import os 
import pandas as pd


data={
    "name":['manish','suraj','ram','shyam'],
    "age":[15,16,17,18],
    'city':['mumbai','dehli','up','bihar']
}
df=pd.DataFrame(data)

data_dir="data"
os.makedirs(data_dir,exist_ok=True)

file_path=os.path.join(data_dir,'sample.csv')
df.to_csv(file_path,index=False)

print(f'CSV FILE SAVE TO {file_path}')

