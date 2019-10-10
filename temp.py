import time

with open(
        r'C:\Users\Meteoaza\Dropbox\WorkSpace\Docs\Рабочие_Документы\Обучение\Тесты_вопросы\TestForEngrs\SafetyTest.txt ',
        'r', encoding='utf-8')as f:
    lines = f.readlines()
n = 0
t = []
d = {}
test_dic = dict.fromkeys(('Qs', 'A1', 'A2', 'A3', 'A4', 'A5', 'An'), 0)
for line in lines:
    for k in test_dic.keys():
        if k in line:
            t.append(line)
            if 'An' in line:
                d.update({n: t})
                n += 1
                t = []
# print(d)
l = [int(a) for a in d[0][-1][3:].split()]
l.sort()

print(l)
