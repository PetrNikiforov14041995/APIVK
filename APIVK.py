# нужно сделать class и реализовать в нем метод поиска общих друзей
import requests
import json

TOKEN = '949c061174e5048eb7cbba8550186fb2f269c5c27843a90c9f0eb70ab7305fdfc5cc5b18db4f707b1d79c'
user_id_first = input(f'Введите id первого пользователя:')
user_id_second = input(f'Введите id второго пользователя:')

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return f"https://vk.com/id{self.user_id}"
        
    
    def friends(self):
        response = requests.get(
            'https://api.vk.com/method/friends.getMutual',
            params = {
                'access_token': TOKEN,
                'sourse_uid': user_id_first,
                'target_uid': user_id_second,
                'count': 100,
                'v': 5.21
            }
        )
        return response.json()    
    
    def get_friends(self):
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params = {
                'access_token': TOKEN,
                'user_id': self.user_id,
                'v': 5.21
            }
        )
        return response.json()["response"]["items"]

    # def get_compare_second(self):
    #     response = requests.get(
    #         'https://api.vk.com/method/friends.get',
    #         params = {
    #             'access_token': TOKEN,
    #             'user_id': user_id_second,
    #             'v': 5.21
    #         }
    #     )
    #     return response.json()  
          
   
user1 = User(user_id_first)
user2 = User(user_id_second)
result = set(user1.get_friends()) & set(user2.get_friends())
print(user1)
print(user2)
print(result)

