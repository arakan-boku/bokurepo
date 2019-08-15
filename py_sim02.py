import matplotlib.pyplot as plt
import random

# 最初に全員が保持する金額
INITIAL_INCOME = 0
# 一回のトレードで受け渡しをする金額
TRANSACTION_AMOUNT = 200
# トレードを繰り返す回数
REPEAT_COUNT = 1000000
# 処理対象とする人数
NUMBER_OF_PEOPLE = 1000

# 10000円ずつもった1000人を生成
current_income_list = [INITIAL_INCOME for dummy in range(NUMBER_OF_PEOPLE)]
# 乱数であたった一人目から二人目に金額をうつす
for i in range(REPEAT_COUNT):
    provider = random.randrange(0, NUMBER_OF_PEOPLE)
    recipient = random.randrange(0, NUMBER_OF_PEOPLE)
    current_income_list[provider] -= TRANSACTION_AMOUNT
    current_income_list[recipient] += TRANSACTION_AMOUNT

# 1000円レンジでカウントに使う辞書
income_distribution_dic = {
    'MIN': 0,
    '-11': 0,
    '-10': 0,
    '-9': 0,
    '-8': 0,
    '-7': 0,
    '-6': 0,
    '-5': 0,
    '-4': 0,
    '-3': 0,
    '-2': 0,
    '-1': 0,
    'CTR': 0,
    '1': 0,
    '2': 0,
    '3': 0,
    '4': 0,
    '5': 0,
    '6': 0,
    '7': 0,
    '8': 0,
    '9': 0,
    '10': 0,
    '11': 0,
    '12': 0,
    '13': 0,
    '14': 0,
    '15': 0,
    'MAX': 0
}

# カウント時に比較する金額レンジをもつ辞書
income_forwork_dic = {
    'MIN': -2000,
    '-11': -1000,
    '-10': 0,
    '-9': 1000,
    '-8': 2000,
    '-7': 3000,
    '-6': 4000,
    '-5': 5000,
    '-4': 6000,
    '-3': 7000,
    '-2': 8000,
    '-1': 9000,
    'CTR': 10000,
    '1': 11000,
    '2': 12000,
    '3': 13000,
    '4': 14000,
    '5': 15000,
    '6': 16000,
    '7': 17000,
    '8': 18000,
    '9': 19000,
    '10': 20000,
    '11': 21000,
    '12': 22000,
    '13': 23000,
    '14': 24000,
    '15': 25000,
    'MAX': 99999
}
# 辞書にカウントしていく
for r in current_income_list:
    for key_a, val_a in income_forwork_dic.items():
        if r <= val_a:
            if key_a != 'MIN':
                income_distribution_dic[key_a] += 1
            break
# 棒グラフの表示
plt.bar(x=income_distribution_dic.keys(),
        height=income_distribution_dic.values())
plt.show()
