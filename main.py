#%%
# data manipulation
from asyncore import read
import pandas as pd
import numpy as np
import requests

# data viz
import matplotlib.pyplot as plt
from matplotlib import rcParams
import seaborn as sns

# apply some cool styling
plt.style.use("ggplot")
rcParams['figure.figsize'] = (12,  6)


url = 'https://api-get-jobs-from-dwp.herokuapp.com/available_jobs'

def read_data(url):
    """
    Reads data from a url and returns a dataframe
    """
    try:
        response = requests.get(url)
    except requests.exceptions.RequestException as e:
        print(e)
    else:
        print('status code:', response.status_code)
        print('Last posting date:',response.json()['last_posting_date'])
        print('available jobs:', response.json()['jobs_count'])
        df = pd.DataFrame(response.json()['data'])
    return df
#%%
df = read_data(url)
df.shape
# %%
df.info()
# %%
df.describe()
# %%
df['company'].value_counts()
# %%
df['location'].value_counts()
#%%
url_sponsors = 'https://assets.publishing.service.gov.uk/government/uploads/system/uploads/attachment_data/file/1095789/2022-08-02_-_Worker_and_Temporary_Worker.csv'

sponsors = pd.read_csv(url_sponsors)


# %%


