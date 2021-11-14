#application programming interface token
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import pandas as pd
path_to_credential = 'test-api-329417-4d8f9f1c9d26.json'
table_name = 'Test table'
scope = ['https://spreadsheets.google.com/feeds',
         'https://www.googleapis.com/auth/drive']

credentials = ServiceAccountCredentials.from_json_keyfile_name(path_to_credential, scope)

gs = gspread.authorize(credentials)
work_sheet = gs.open(table_name)

# Select 1st sheet
sheet1 = work_sheet.sheet1

# Get data in python lists format
data = sheet1.get_all_values()
headers = data.pop(0)
df = pd.DataFrame(data, columns=headers)
print(df.head())
