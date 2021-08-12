import pywhatkit

def send_whatsapp_message():

    number = input('> Enter recipients number: ')

    print()

    message = input('> Enter message: ')

    print()

    time = input('> Enter time of delivery(in format 08, 43): ')

    splitted_time = time.split(',')

    hour = int(splitted_time[0])

    minute = int(splitted_time[1])

    pywhatkit.sendwhatmsg(number,message,hour,minute)

def search_on_youtube():

    search = input('> What do you want to search for on youtube: ')

    pywhatkit.playonyt(search)

def search_on_google():

    search_google = input('> What do you want to search for on Google: ')

    pywhatkit.search(search_google)

def search_info():

    info = input('> What do you want to search for: ')

    pywhatkit.info(info)

while True:

    operation = input('> What operation do you want to perform: ')

    if operation == 'send whatsapp message' or operation == 'swm':

        send_whatsapp_message()

    elif operation == 'youtube search' or operation == 'ys':

        search_on_youtube()

    elif operation == 'search on google' or operation == 'sog':

        search_on_google()

    elif operation == 'quick search' or operation == 'qs':

        search_info()

    elif operation == 'quit' or operation == 'end':

        break

