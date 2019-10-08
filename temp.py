with open(r'/home/meteoaza/Downloads/TestForEngrs/SafetyTest.txt', 'r',
          encoding='cp1251')as f:
    lines = f.readlines()
    test = {}
    n = 0
    for line in lines:
        if 'Name' in line[:5]:
            test_name = line[5:]
        elif 'SetCol' in line[:6]:
            clr = line[7:]
        elif 'SetM_5' in line[:7]:
            mark_5 = line[7:9]

    print(mark_5)

    for line in lines:
        try:
            if 'Name' in line[:5]:
                test_name = line[5:]
            elif 'Qs' in line[:2]:
                q = line
                n += 1
            elif 'A1' in line[:2]:
                a1 = line
            elif 'A2' in line[:2]:
                a2 = line
            elif 'A3' in line[:2]:
                a3 = line
            elif 'An' in line[:2]:
                k = line
            test[n-1] = [q, a1, a2, a3, k]

        except NameError:
            pass



