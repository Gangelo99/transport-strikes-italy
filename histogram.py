# This python file creates a histogram where the X axis is the year
# while the Y axis is the number of transport strikes that occurred in that year

import matplotlib.pyplot as plt
from module.strikes_number_per_year import grouped_df
from module.font import font_title, font_labels, font_ticks

years_list = grouped_df['dataInizio'].tolist()
strikes_number_list = grouped_df['NumeroScioperi'].tolist()

# print(years_list)
# print(strikes_number_list)

plt.figure(figsize=(10,6))
plt.bar(years_list, strikes_number_list, width=1.0, edgecolor='black')


def addlabels(x, y):
    for i, value in enumerate(y):
        plt.text(x[i], value + 0.2, str(value), ha='center', va='bottom', fontdict=font_ticks)


addlabels(years_list, strikes_number_list)

plt.ylim(200, 850)
plt.xlabel('Year', fontdict=font_labels, labelpad=20)
plt.ylabel('Numbers of transport protest', fontdict=font_labels, labelpad=20)
plt.xticks(size=20)
plt.yticks(size=15)
plt.tick_params(axis='x', pad=10)
plt.title('Number of transport strikes each year', pad=20,
          fontdict=font_title)


plt.show()
