import time

while True:

    hora_atual = time.strftime ("%H:%M:%S")

    print(hora_atual, end="\r")
    time.sleep(1)