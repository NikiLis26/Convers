# calculate_target расчет целевой конверсии 
# paid_bils оплаченные счета 
# sentences отработанные карточки 
# exhibited_bils выставленные счета 
# fucking_money дожим 

from functools import partial

def calculate_target(sentences, paid_bils):
    return int(paid_bils / sentences * 100)

def spent_exposed(exhibited_bils, sentences):
    return int(exhibited_bils / sentences * 100)

def fucking_money(paid_bils, exhibited_bils):
    return int(paid_bils / exhibited_bils * 100)

# Общие аргументы
paid_bils = 6
exhibited_bils = 14
sentences = 123

# Создание частичных функций с зафиксированными общими аргументами
calculate_target_partial = partial(calculate_target, sentences, paid_bils)
spent_exposed_partial = partial(spent_exposed, exhibited_bils, sentences)
fucking_money_partial = partial(fucking_money, paid_bils, exhibited_bils)

# Вызов частичных функций
result1 = calculate_target_partial()
result2 = spent_exposed_partial()
result3 = fucking_money_partial()

print(result1)
print(result2)
print(result3)
