from datetime import datetime as dt

def calc_logger(data):
    time=dt.now().strftime('%Y-%D %H:%M:%S')

    with open('log.csv', 'a') as file:
        file.write('{};a=;{};b=;{};{}=;{}\n'
        .format(time, *data) )