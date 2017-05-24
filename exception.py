
while True:
    try:
        n = int(input('How old are you ?'))
        if n == 50:
            break
    except ValueError:
            print('Please enter a integer value')
    finally:
        