import time
import vk_api
import random
import requests
from vk_api.longpoll import VkLongPoll,VkEventType
allow = [228102740]
def main():
      session = vk_api.VkApi(token='19a4a4d060e680a839b18d07e0923197bb60ea2ca305b2cf3358d314921047c1c57082a2204ec39290acf')
      longpoll = VkLongPoll(session)
      vk = session.get_api()
      for event in longpoll.listen():
            if event.from_chat:
                      try:
                              ms = event.text.lower()
                      except AttributeError:                                                                                                         
                              continue
                      if "id228102740" in ms or "https://vk.com/ded_moksem" in ms:
                            vk.messages.send(
                              peer_id=event.peer_id,
                              message="✅Сигнал отправлен дежурному",
                              random_id=0)
                      elif "add" in ms and event.user_id in allow:
                              xid = ms[7:16]
                              try:                 
                                          vk.messages.addChatUser(
                                          chat_id=event.chat_id,
                                          user_id=xid)
                                          vk.messages.send(
                                          peer_id=event.peer_id,
                                          message="✅Пользователь был добавлен в беседу",
                                          random_id=0)
                              except Exception as error:
                                          print(error)
                                          vk.messages.send(
                                          peer_id=event.peer_id,
                                          message="⚠Не могу добавить, проверьте его на наличие в друзьях или в беседе.",
                                          random_id=0)
                      elif "del" in ms and event.user_id in allow:
                                          kid = ms[7:16]
                                          try:
                                                  vk.messages.removeChatUser(
                                                  chat_id=event.chat_id,
                                                  user_id=kid)
                                                  vk.messages.send(
                                                  peer_id=event.peer_id,                               
                                                  message="✅Пользователь был удалён из беседы ",                                     
                                                  random_id=0)
                                          except Exception as error:                         
                                                  print(error)
                                                  vk.messages.send(
                                                  peer_id=event.peer_id,
                                                  message="Не могу удалить пользователя",
                                                  random_id=0)
                                                  
                      elif "chat id" in ms:                                                                             vk.messages.send(
        peer_id=event.peer_id,
        message="Айди этого чата среди моих: " + str(event.chat_id),
        random_id=0)                                
                            
                      elif "exit" in ms and event.user_id in allow:
                                                  vk.messages.send(
    peer_id=event.peer_id,
    message="Покидаю беседу",
    random_id=0)
                                                  vk.messages.removeChatUser(
                                              chat_id=event.chat_id,
                                              member_id=228102740)
    
                      if "adm" in ms:
                                          jjd = ms[7:16]
                                          if event.user_id == 228102740:
                                              try:                             allow.append(int(jjd))
                                              except Exception as error:
                                                  print(error)                                                                                     
                      if "-adm" in ms:
                                          jjd = ms[7:16]
                                          if event.user_id == 228102740:
                                              try:                             allow.remove(int(jjd))
                                              except Exception as error:
                                                  print(error)                    
                      elif "+друг" in ms:
                                              try:
                                                  vk.friends.add(
        user_id=event.user_id)
                                                  vk.messages.send(
        peer_id=event.peer_id,
        message="отправил заявку",
        random_id=0)
                                              except Exception as error:
                                                    print(error)
                                              vk.messages.send(
        peer_id=event.peer_id,
        message="Не удалось отправить заявку",
        random_id=0)
                                                                                         
                      elif "report" in ms:
                                          repid = ms[11:20]
                                          vk.users.report(
                                          user_id=int(repid),
                                          type="spam")
                                          vk.messages.send(
    peer_id=event.peer_id,
    message="Жалоба на [id" + repid + "|пользователя] отправлена",
    random_id=0)                                                          
                                                                            
def main2():
              try:                                                                                                       
                        main()                                                                                   
              except vk_api.exceptions.Captcha:   
                        time.sleep(30)                                                   
                        main2()                                                                                 
              except requests.exceptions.ConnectionError:                       
                        time.sleep(2)
                        main2()
              except vk_api.exceptions.ApiError as v:
                        time.sleep(2)                                                                             
                        main2()
              except requests.exceptions.ReadTimeout:
                        time.sleep(2)
                        main2()
if __name__ == '__main__':
    main2() 