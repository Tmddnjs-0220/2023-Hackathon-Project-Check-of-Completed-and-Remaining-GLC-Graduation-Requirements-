import pandas as pd


def load_and_clean(csv_path):
    # Try reading with utf-8 first
    try:
        df = pd.read_csv(csv_path, encoding='utf-8')
    except:
        # If utf-8 fails (Windows Excel case), try cp949
        df = pd.read_csv(csv_path, encoding='cp949')

    # Organizing columns (remove space/lowercase)
    new_columns = []
    for col in df.columns:
        col = col.strip()
        col = col.lower()
        new_columns.append(col)
    df.columns = new_columns

    # credits 숫자 변환
    credits_list = []
    for value in df['credits']:
        try:
            num = float(value)
        except:
            num = 0
        credits_list.append(num)
    df['credits'] = credits_list

    return df


def save_result_csv(df, file_name):
    # utf-8-sig prevents Korean 깨짐 in Excel
    df.to_csv(file_name, index=False, encoding='utf-8-sig')
