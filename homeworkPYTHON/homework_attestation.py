# Усложнение задач выделены (*). Они необязательны для решения и нужны для тех, кому мало выполнить обычное задание.
# Если вы хотите решить усложненное задание - сначала сделайте задание обычной сложности.

# 10.1[44]: Дан код, генерирующий DataFrame, которая состоит всего из 1 столбца. Ваша задача перевести его в one hot вид.
# Статья про one hot вид https://colab.research.google.com/drive/1qKamnDiRmpRZkpiqWPkunBdAhmzhMcGz?usp=sharing

# Сделайте one hot вид с использованием get_dummies
# Сделайте one hot вид с использованием изученных методов группировки данных. Обратите внимание, что Nan это не ноль.


# import pandas as pd

import random

lst = ['robot'] * 10

lst += ['human'] * 10

random.shuffle(lst)

data = pd.DataFrame({'whoAmI': lst})

unique_values = data['whoAmI'].unique()

for value in unique_values:

   data[value] = (data['whoAmI'] == value).astype(int)

data.drop('whoAmI', axis=1, inplace=True)

print(data.head())







