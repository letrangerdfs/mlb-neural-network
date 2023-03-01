import os
import pandas as pd
import glob
from tqdm import tqdm

data_dir = "C:/Users/muhrs/PycharmProjects/ANNmodel/batting-data"

csv_files = glob.glob(os.path.join(data_dir, '*.csv'))

for file in tqdm(csv_files):
    data = pd.read_csv(file, encoding='ISO-8859-1')
    if 'Team Totals' in data['Player Name'].values:
        data = data[data['Player Name'] != 'Team Totals']
        data.to_csv(file, index=False)
