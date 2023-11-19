from input import df, pd

df['dataInizio'] = pd.to_datetime(df['dataInizio']).dt.year
df['dataFine'] = pd.to_datetime(df['dataFine']).dt.year

#Group the dataframe by year
grouped_df = df.groupby('dataInizio').size().reset_index(name='NumeroScioperi')

print(grouped_df)

