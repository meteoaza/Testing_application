try:
    with open('settings.ini', 'r', encoding='utf-8')as f:
        line = f.readline()
except FileNotFoundError:
    pass
settings = [12345]

print(line.split())
