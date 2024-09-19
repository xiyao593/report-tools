import pandas as pd

if __name__ == '__main__':
    f = 'data/销售明细.xlsx'

    df = pd.read_excel(f)
    print(df)

