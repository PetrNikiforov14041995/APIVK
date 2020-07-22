# нужно сделать class и реализовать в нем метод поиска общих друзей
import requests

token = '958eb5d439726565e9333aa30e50e0f937ee432e927f0dbd541c541887d919a7c56f95c04217915c32008'
# user_id = input()
class User:
    def __init__(self, token):
        self.token = token

    def get_status(self):
        response = requests.get(
            'https://api.vk.com/method/account.getProfileInfo',
            params = {
                'access_token': token,
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
    
vakson = User(token)
print(vakson.get_status())
# print(vakson.friends())