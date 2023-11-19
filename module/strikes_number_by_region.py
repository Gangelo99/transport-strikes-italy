from input import df, pd

grouped_df = df.groupby('nome_regione').size().reset_index(name='NumeroScioperi')

# Remove the first element of this Database because it's the number of Italy protests (national)
italy_protests_number = grouped_df['NumeroScioperi'].iat[0] #Save the number of national protest in this variable
grouped_df = grouped_df.iloc[1:] #Drop teh first element


### Remove the below comment to output the new CSV file
# grouped_df.to_csv("strikes_number_by_region.csv")