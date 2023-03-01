import os
import pandas as pd
import chardet
from tqdm import tqdm

data_dir = "C:/Users/muhrs/Desktop/mega data - Copy"

csv_files = [os.path.join(data_dir, f) for f in os.listdir(data_dir) if f.endswith('.csv')]

results = pd.DataFrame(columns=['filename', 'player_name'])

for csv_file in tqdm(csv_files, desc="Processing files", unit="file"):
    # Use chardet to detect the encoding of the file
    with open(csv_file, 'rb') as f:
        result = chardet.detect(f.read())
        encoding = result['encoding']

    player_names = pd.read_csv(csv_file, usecols=['Player Name'], encoding=encoding)['Player Name']

    player_names = player_names.str.strip()

    file_results = pd.DataFrame({'filename': [os.path.basename(csv_file)]*len(player_names), 'player_name': player_names})

    results = pd.concat([results, file_results], ignore_index=True)

results.to_csv('player_names.csv', index=False)
