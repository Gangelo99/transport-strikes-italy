#### AGGIUNGERE

import matplotlib.pyplot as plt
from module.strikes_number_per_categories import grouped_df
from module.font import font_title

print(grouped_df)

sector_list = grouped_df['settore'].tolist()
protests_list = grouped_df['NumeroScioperi'].tolist()

# The percentage value is shown only if it is greater than 0.2%.
def my_autopct(pct):
    return f'{pct:.1f}%' if pct > 0.2 else None


# Create a pie chart without labels
patches, texts, autotexts = plt.pie(protests_list,
                                    labels= None,
                                    # explode=[0, 0, 0.05, 0, 0, 0, 0],
                                    autopct=my_autopct,
                                    pctdistance = 1.15,
                                    labeldistance = 1.4,
                                    colors= ["#003f5c", "#2f4b7c", "#665191", "#a05195", "#d45087", "#f95d6a", "#ff7c43", "#ffa600", "#5c0000", "#900009", "#c60008", "#ff0000"],
                                    startangle=140)

# Imposta l'etichettatura esterna con l'indice e la percentuale
legend_labels = [f"{sector}" for sector, autotext in zip(sector_list, autotexts)]
plt.legend(patches, legend_labels, loc="upper right", bbox_to_anchor=(1.1, 1), fontsize=10)

# # Set external labeling with index and percentage
# manual_labels = [("Categoria1", (1.2, 0.8)),
#                  ("Categoria2", (1.2, 0.6)),
#                 ]
#
# # for i, (text, autotext) in enumerate(zip(sector_list, autotexts)):
#     if (text, autotext) in manual_labels:
#         x, y = manual_labels[(text, autotext)]
#         autotext.set_position((x, y))
#         autotext.set_horizontalalignment('center')
#         autotext.set_verticalalignment('center')

plt.axis('equal')  # Assicura che il grafico a torta sia circolare
plt.title('Distribution of Transport Protests Across Sectors (2014-2020)', pad=20, fontdict=font_title)

plt.show()