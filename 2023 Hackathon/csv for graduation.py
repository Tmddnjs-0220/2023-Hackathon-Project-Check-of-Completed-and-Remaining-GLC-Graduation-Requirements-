import pandas as pd

def load_and_clean(csv_path):
    df = pd.read_csv(csv_path)  

    # Organizing columns (remove space/lowercase)
    new_columns = []
    for col in df.columns:
        col = col.strip()
        col = col.lower()
        new_columns.append(col)
    df.columns = new_columns

    # credits 
    credits_list = []
    for value in df['credits']:
        try:
            num = float(value)
        except:
            num = 0
        credits_list.append(num)
    df['credits'] = credits_list

    return df
