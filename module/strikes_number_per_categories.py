from input import df, pd

grouped_df = df.groupby('settore').size().reset_index(name='NumeroScioperi')

print(grouped_df)


