# нужно сделать class и реализовать в нем метод поиска общих друзей
import requests

TOKEN = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
user_id = input()
class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def get_status(self):
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params = {
                'access_token': TOKEN,
                'user_id': user_id,
                'v': 5.21
            }
        )
        return response.json()
    
    # def friends(self):
    #     response = requests.get(
    #         'https://api.vk.com/method/friends.getMutual',
    #         params = {
    #             'access_token': token,
    #             'sourse_uid': user_id,
    #             'target_uid': 171691064, 
    #             'v': 5.21
    #         }
    #     )
    #     return response.json()    
    
vakson = User(user_id)
print(vakson.get_status())
# print(vakson.friends())