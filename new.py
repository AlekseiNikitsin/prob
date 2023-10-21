nuumb = 12
running = True
while running:
    gs = int(input("vvod chisla: "))
    if gs == nuumb:
        print('winner')
        running = False
    elif gs < nuumb:
        print('net bolshe')
    else:
        print('menshe')
else:
    print('whill zakonchen')