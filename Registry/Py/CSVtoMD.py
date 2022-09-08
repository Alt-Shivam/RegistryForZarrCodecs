import pandas as pd

df = pd.read_csv("Registry/Registry.csv", engine='python')
with open("Registry/Registry.md", 'w') as md:
    df.fillna('', inplace=True)
    df.to_markdown(buf=md, index=False)
