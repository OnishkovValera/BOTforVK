import time

import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType

import random

import requests

vk_session = vk_api.VkApi(token='кнешн')
longpoll = VkBotLongPoll(vk_session, 210555883)

tyte = time.time()
raspisanie_dima_like = '1.Английский язык\n' \
                       '2.Английский язык\n' \
                       '3.Химия\n' \
                       '4.Информатика\n' \
                       '5.Информатика\n'

raspisdist = {'понедельник': '1.Каникулы\n'
                             '2.Английский язык\n'
                             '3.Химия\n'
                             '4.Информатика\n'
                             '5.Каникулы\n'
                             '6.Физика\n',

              'вторник': '1.Каникулы\n'
                         '2.Русский язык\n'
                         '3.История\n'
                         '4.Алгебра\n'
                         '5.Астрономия\n',

              'среда': '1.Каникулы\n'
                       '2.Литература\n'
                       '3.Алгебра\n'
                       '4.Литература\n'
                       '5.Каникулы\n'
                       '6.История\n',

              'четверг': '1.Каникулы\n'
                         '2.Алгебра\n'
                         '3.Алгебра\n'
                         '4.Математика ЕГЭ\n'
                         '5.Биология\n',

              'пятница': '1.Каникулы\n'
                         '2.Обществознание\n'
                         '3.Физика\n'
                         '4.Физика\n'
                         '5.Каникулы\n'
                         '6.Английский язык\n',

              'суббота': 'мы не учимся',

              'воскресенье': 'иди нахуй'
              }
raspiscommon = {'понедельник': '1.Английский язык\n'
                               '2.Английский язык\n'
                               '3.Химия\n'
                               '4.Информатика\n'
                               '5.Инфрматика\n'
                               '6.Физика\n',

                'вторник': '1.Физкультура\n'
                           '2.Литература\n'
                           '3.История\n'
                           '4.Алгебра\n'
                           '5.Алгебра\n'
                           '6.Астрономия\n',

                'среда': '1.Физкультура\n'
                         '2.Астрономия\n'
                         '3.Алгебра\n'
                         '4.Русский язык\n'
                         '5.Физика\n'
                         '6.История\n'
                         '7.Алгебра\n',

                'четверг': '1.Английский\n'
                           '2.Геометрия\n'
                           '3.Геометрия\n'
                           '4.Физика\n'
                           '5.Биология\n'
                           '6.Физра\n'
                           '7.Русский язык',

                'пятница': '1.Химия\n'
                           '2.История\n'
                           '3.Физика\n'
                           '4.Физика\n'
                           '5.ОБЖ\n',

                'суббота': '1.Обществознание\n'
                           '2.Литература\n'
                           '3.Алгебра\n'
                           '4.Литература\n'
                           '5.Обществознание\n'
                           '6.Алгебра\n'
                           '7.Руссикй язык ЕГЭ\n',

                'воскресенье': 'жестко играем в бедварс'
                }

spisokofcommands = {'тмр ддшв': ['угроза обществу', 'photo-210555883_457239023'],

                    'трамвай': [' ', 'photo-210555883_457239024'],

                    'баджадж': [' ', 'photo-210555883_457239024'],

                    'звонки': ['Первый урок 8:30 - 9:15\n'
                               'Второй урок 9:25 - 10:10\n'
                               'Третий урок 10:30 - 11:15\n'
                               'Четвертый урок 11:30 - 12:20\n'
                               'Пятый урок 12:30 - 13:35\n'
                               'Шестой урок 13:25 - 14:10\n', ' '],

                    'липси': ['хай', 'audio-2001302414_100302414'],

                    'сигаретный шреддер': ['Когда отпиздил 200 чурок', 'photo-210555883_457239029'],

                    'змс по стрельбе': ['ПАРГОЛОВО АХУЕННО', 'photo263221262_457262349'],

                    'производная': [' ', 'photo-210555883_457239031'],

                    'невидимый враг повержен': ['Когда тебя убили в майнкрафте, а ты не растерялся и блеванул в окно',
                                                'photo-210555883_457239032'],

                    'лавелас нашего времени': ['Он бы её трахнул)))', 'photo263221262_457262349']
                    }


def is_it_dima(messageidentificator, chatid, day):
    info = vk_session.method('messages.getByConversationMessageId',
                             {'peer_id': 2000000000 + chatid, 'conversation_message_ids': messageidentificator,
                              'fields': 'id'})
    if info['items'][0]['from_id'] == 293517193 and day == 'понедельник':
        return True
    else:
        return False


def israspisdistcommand(test):
    test = test.split()
    if len(test) == 3:
        if 'расписание' in test and 'дистант' in test:
            return True
        else:
            return False


def israspiscom(test):
    test = test.split()
    if len(test) == 3:
        if 'расписание' in test and 'обычное' in test:
            return True
        else:
            return False


def sender(sendid, text):
    vk_session.method('messages.send',
                      {'chat_id': sendid, 'message': text, 'random_id': random.randint(100000000, 900000000)})


def mediasender(chatid, url, text):
    vk_session.method('messages.send',
                      {'chat_id': chatid, 'message': text, 'attachment': url,
                       'random_id': random.randint(100000000, 900000000)})


def chatinformation(chatid):
    message = (vk_session.method('messages.getConversationMembers', {'peer_id': 2000000000 + chatid}))
    info = {}
    info['count'] = message['count']
    info['members'] = []
    for i in range(info['count'] - 1):
        info['members'].append({
            'id': message['profiles'][i]['id'],
            'first_name': message['profiles'][i]['first_name'],
            'last_name': message['profiles'][i]['last_name'],
            'screen_name': message['profiles'][i]['screen_name']
        })
    return info


for event in longpoll.listen():
    try:
        if event.type == VkBotEventType.MESSAGE_NEW:
            if event.from_chat:
                chtid = event.chat_id
                message = event.object.message['text'].lower()
                messageid = event.object.message['conversation_message_id']
                print(messageid)
                if message in spisokofcommands:
                    mediasender(chtid, spisokofcommands[message][1], spisokofcommands[message][0])

                elif message == 'test':
                    sender(chtid, 'messagesenderinwork')
                    mediasender(chtid, ' ', 'mediasenderinwork')
                    mediasender(chtid, ' ', 'audiosenderinwork')
                elif message == 'info':
                    info = chatinformation(chtid)
                    for i in info['members']:
                        sender(chtid, '{} {}, id:{}, адрес страницы:{}'.format(i['first_name'], i['last_name'], i['id'],
                                                                               i['screen_name']))

                elif message == 'help':
                    sender(chtid,
                           'основные функции: \'наши баллы на егэ\' - точне вычисление количества баллов с помощью пиздец '
                           'сложных алгоритмов')
                    sender(chtid,
                           '\'до кого доебется историчка\' - вычисление до кого доебется историчка на этот раз, '
                           'вычисляется на кофейной гуще из Латвии(или откуда он там)')
                    sender(chtid, '\'info\' - понятно')
                    sender(chtid,
                           '\'расписание [дистант\обычное] [день недели]\' - что эта команда может блять делать, беспонятия')
                    sender(chtid, 'просто функции: \'\'легчайше\',\'тмр ддшв\', \'трамвай\', \'баджадж\', \'липси\'')

                elif message == 'наши баллы на егэ':
                    info = chatinformation(chtid)
                    for chel in info['members']:
                        sender(chtid, '{} {} сдаст егэ на {} баллов'.format(chel['first_name'], chel['last_name'],
                                                                            random.randint(0, 100)))

                elif len(message) > 70:
                    vk_session.method('messages.send',
                                      {'chat_id': chtid, 'message': ' ', 'attachment': 'photo-210555883_457239025',
                                       'random_id': random.randint(100000000, 900000000)})

                elif message == 'до кого доебется историчка':
                    info = chatinformation(chtid)
                    vk_session.method('messages.send', {'chat_id': chtid, 'message': 'историчка доебется до {}'.format(
                        info['members'][random.randint(0, info['count'] - 2)]['first_name']),
                                                        'random_id': random.randint(100000000, 900000000)})

                elif israspisdistcommand(message):
                    day = message.split()[2]
                    if day in raspiscommon:
                        sender(chtid, raspisdist[day])
                    else:
                        sender(chtid, 'еблан')

                elif israspiscom(message):
                    day = message.split()[2]
                    if day in raspiscommon:
                        if is_it_dima(messageid, chtid, day):
                            sender(chtid, raspisanie_dima_like)
                        else:
                            sender(chtid, raspiscommon[day])
                    else:
                        sender(chtid, 'Какой нахуй {}'.format(day))
                        sender(chtid, 'Пруфы')
                        sender(chtid, 'СЛИТ')
                        sender(chtid, 'БОТ ЕБАНЫЙ')
    except requests.exceptions.ReadTimeout:
        print("\n Переподключение к серверам ВК \n")
        time.sleep(3)
        vk_session = vk_api.VkApi(
            token='да')
        longpoll = VkBotLongPoll(vk_session, 210555883)
        print(time.ctime(time.time()))
