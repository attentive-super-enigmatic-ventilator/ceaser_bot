import random
import vk_api
import requests 
abc = ['а','б','в','г','д','е','ё','ж','з','и','й','к','л','м','н','о','п','р','с','т','у','ф','х','ц','ч','ш','щ','ъ','ы','ь','э','ю','я']
def encryption(text,key):
    new_text = ''
    for i in range(len(text)):
        n_i = (abc.index(text[i])+key)%33
        new_text += abc[n_i]
    return new_text
def decryption(text,key):
    new_text = ''
    for i in range(len(text)):
        n_i = (abc.index(text[i])-key)%33
        new_text += abc[n_i]
    return new_text
print(encryption('вова',1))
from vk_api.longpoll import VkLongPoll, VkEventType 
vk_session = vk_api.VkApi(token='ffee8fff00f944d706dd455eeb8eedf8269d7403122bcee3fabe31bea8d6d147a3e7be2f253ef6d2b8a96')
vk = vk_session.get_api() 
for event in VkLongPoll(vk_session).listen(): 
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text: 
        if event.from_user: #Если написали в ЛС 
            s = event.text 
            if s[:8] == 'Зашифруй': 
                n = s[9]
                try:
                    x=int(n)
                except:
                    vk.messages.send( 
                user_id=event.user_id,
                random_id=random.randint(1,2**32),
                message='Неправильный формат ввода' 
                    )
                    continue
                i=10
                while True:
                    try:
                        e=int(s[i])
                        n+=s[i]
                    except:
                        break
                    i+=1
                n=int(n)
                c = s[i+1:] 
                nc=encryption(c,n)
                vk.messages.send( 
                user_id=event.user_id,
                random_id=random.randint(1,2**32),
                message=nc 
                    )

            elif s[:9] == 'Расшифруй':
                n = s[10]
                i=11
                try:
                    x=int(n)
                except:
                    vk.messages.send( 
                user_id=event.user_id,
                random_id=random.randint(1,2**32),
                message='Неправильный формат ввода' 
                    )
                    continue
                while True:
                    try:
                        e=int(s[i])
                        n+=s[i]
                    except:
                        break
                    i+=1
                n=int(n)
                c = s[i+1:] 
                nc=decryption(c,n)
                vk.messages.send( 
                user_id=event.user_id,
                random_id=random.randint(1,2**32),
                message=nc 
                )
            else:
                vk.messages.send(user_id=event.user_id,
                random_id=random.randint(1,2**32),
                message='Напиши мне:'+'\n'+'-Зашифруй [число] [слово] (бот выдаст тебе это же слово, но зашифрованное шифром Цезаря)'+'\n'+'-Расшифруй [число] [слово, зашифрованное шифром Цезаря] (бот выдаст тебе тоже слово, но расшифрованное)'+'\n'+'Шифр Цезаря - это обычное шифрование сдвигом'+'\n'+'Например, если ты напишешь: Зашифруй 1 мама'+'\n'+'Бот ответит: амам')
