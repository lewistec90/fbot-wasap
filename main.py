# ESCRIBIR POR WASAP BOT

import pywhatkit as pwk
import csv
from datetime import datetime


def get_numbers(filename):
    result = []
    with open(filename, 'r') as csv_file:
        numbers = csv.reader(csv_file)
        for row in numbers:
            # print(row[0])
            result.append(row[0])
    return result


now = datetime.now()

current_time = now.strftime("%H:%M:%S")
print("current time: " + current_time)
h, m, s = current_time.split(':')
print("Hora: {} - Minuto: {} - Segundo: {}".format(h, m, s))

# pwk.sendwhats_image(phone_no="+1123654987", img_path="/home/luiscs/Downloads/giphy.gif", caption="Mensaje de prueba
# de gif")

phone_number = get_numbers("mynumber.csv")
phone_number_links = get_numbers("numberlinks.csv")

print(phone_number)
print(len(phone_number_links))

try:
    pwk.sendwhatmsg(phone_number[0], 'Hola este es un mensaje de prueba', int(h), int(m) + 1, tab_close=True)
    # pwk.sendwhatmsg(phone_number_links[0], 'Hola este es un mensaje de prueba', int(h), int(m) + 1, tab_close=True)

    print("Envio exitoso")

except:
    print("Ha ocurrido un error")
