#This Python file creates a histogram where the X-axis
# is the sectors in which transport strikes occur

import matplotlib.pyplot as plt
from module.strikes_number_per_categories import grouped_df
from font import font_title, font_labels, font_ticks

print(grouped_df)

sector_list = grouped_df['settore'].tolist()
strikes_number_list = grouped_df['NumeroScioperi'].tolist()

def shorten_strings(string_list, max_length, max_word_length):
    result = []

    for input_string in string_list:
        words = input_string.split()

        if len(words) > 1:
            new_string = ''
            for word in words:
                if len(word) > max_word_length:
                    new_string += word[:max_word_length] + '. '
                else:
                    new_string += word + ' '
            new_string = new_string.strip()[:max_length]
            result.append(new_string)
        else:
            result.append(input_string)

    return result

sector_list = shorten_strings(sector_list, 30, 5)

print(sector_list)
print(strikes_number_list)

plt.figure(figsize=(12,8))
plt.bar(sector_list, strikes_number_list, width=0.2)

def addlabels(x, y):
    for i, value in enumerate(y):
        plt.text(x[i], value + 0.2, str(value), ha='center', va='bottom', fontdict=font_ticks)

addlabels(sector_list, strikes_number_list)

plt.xlabel('Anno', fontdict=font_labels, labelpad=20)

plt.ylabel('Numbers of transport protest', fontdict=font_labels, labelpad=20)
plt.xticks(rotation=15, ha="center", size=9)
plt.yticks(size=15)
plt.tick_params(axis='x', pad=10)
plt.title('Distribution of Transport Strikes Across Sectors (2014-2020)', pad=20,
          fontdict=font_title)


plt.show()
