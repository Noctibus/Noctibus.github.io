import pandas as pd

df = pd.read_csv("yop")

df = df.rename(columns={'Unnamed: 0': 'entry_id'})
df_train = df[['embeddings', 'entry_id']]
df_data = df[['number', 'claim_id', 'claim_text_id', 'sequence', 'entry_id']]

df_train.to_csv("train.csv")
df_data.to_csv("data.csv")
