from datetime import datetime

current_time = datetime.now()
current_time = current_time.strftime('%d/%m/%Y - %H:%M:%S')

def log(title:str) -> None:
    file = open('backend/log.txt', 'a')
    file.write(f'{current_time} - {title}\n')
    file.close()
