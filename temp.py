with open('/home/meteoaza/Downloads/TestForEngrs/MeteoSystemsTest.txt', 'r', encoding='cp1251')as f:
    for _ in range(2):
        name = f.readline()
    test = {}
    for _ in range(5):
        question = f.readline()
        answer1 = f.readline()
        answer2 = f.readline()
        answer3 = f.readline()
        right = f.readline()
        test[question] = [answer1, answer2, answer3, right]
score = 0
b = 0
br = input("How much question?")
for q, a in test.items():
    if str(b) == br:
        print('break')
        break
    b += 1
    print(q)
    print(a[0])
    print(a[1])
    print(a[2])
    an = a[3]
    r = input('Input write answer ')
    if r == an:
        print('r = an')
        score += 1
print(f'Your score is {score}')
