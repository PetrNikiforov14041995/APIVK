# нужно сделать class и реализовать в нем метод поиска общих друзей
import requests

TOKEN = '949c061174e5048eb7cbba8550186fb2f269c5c27843a90c9f0eb70ab7305fdfc5cc5b18db4f707b1d79c'
user_id_first = input(f'Введите id первого пользователя:')
user_id_second = input(f'Введите id второго пользователя:')

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    
    # def friends(self):
    #     response = requests.get(
    #         'https://api.vk.com/method/friends.getMutual',
    #         params = {
    #             'access_token': TOKEN,
    #             'sourse_uid': user_id_first,
    #             'target_uid': user_id_second,
    #             'count': 100,
    #             'v': 5.21
    #         }
    #     )
    #     return response.json()    
    
    def get_compare_first(self):
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params = {
                'access_token': TOKEN,
                'user_id': user_id_first,
                'v': 5.21
            }
        )
        return response.json()

    def get_compare_second(self):
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params = {
                'access_token': TOKEN,
                'user_id': user_id_second,
                'v': 5.21
            }
        )
        return response.json()  
          
    # def __add__(self, other):

    # def __str__(self):
    #     return super().__str__()

vakson = User(TOKEN)
result = set(vakson.get_compare_first()) & set(vakson.get_compare_second())
print(result)
# print(vakson.friends())
# print(vakson.get_compare_second())