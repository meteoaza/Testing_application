import random
# with open(r'C:\Users\Meteoaza\Dropbox\WorkSpace\Docs\Рабочие_Документы\Обучение\Тесты_вопросы\TestForEngrs\SafetyTest'
#           r'.txt', 'r', encoding='utf-8')as f:
with open(r'settings.ini', 'r', encoding='utf-8')as f:
    lines = f.readlines()
    test = {}
    n = 0
    for line in lines:
        if 'SetCol' in line[:7]:
            color = int(line[7:9])
            print(color)
        elif 'Qs_try' in line[:7]:
            q_try = int(line[7:9])

        elif 'SetM_5' in line[:7]:
            mark_5 = int(line[7:9])
        elif 'SetM_4' in line[:7]:
            mark_4 = int(line[7:9])
        elif 'SetM_3' in line[:7]:
            mark_3 = int(line[7:9])
        elif 'SetM_2' in line[:7]:
            mark_2 = int(line[7:9])
    # for line in lines:
    #     try:
    #         if 'Name' in line[:5]:
    #             test_name = line[5:]
    #         elif 'Qs' in line[:2]:
    #             q = line
    #             n += 1
    #         elif 'A1' in line[:2]:
    #             a1 = line
    #         elif 'A2' in line[:2]:
    #             a2 = line
    #         elif 'A3' in line[:2]:
    #             a3 = line
    #         elif 'An' in line[:2]:
    #             k = line
    #         test[n-1] = [q, a1, a2, a3, k]
    #     except NameError:
    #         pass
    # for i in range(5):
    # r = random.sample(test.keys(), k=4)

