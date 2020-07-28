# нужно сделать class и реализовать в нем метод поиска общих друзей
import requests
import json


TOKEN = '949c061174e5048eb7cbba8550186fb2f269c5c27843a90c9f0eb70ab7305fdfc5cc5b18db4f707b1d79c'

class User:
    def __init__(self, user_id):
        self.user_id = user_id

    def __str__(self):
        return f"https://vk.com/id{self.user_id}"
    
    @staticmethod    
    def get_friends(user_id):
        response = requests.get(
            'https://api.vk.com/method/friends.get',
            params = {
                'access_token': TOKEN,
                'user_id': user_id,
                'v': 5.21
            }
        )
        return response.json()["response"]["items"]
    
    def __and__(self, other):
        friends1 = self.get_friends(self.user_id)
        friends2 = self.get_friends(other.user_id)

        result = set(friends1) & set(friends2)

        return [User(user_id) for user_id in result]


user1 = User(47526429)
user2 = User(72773511)

print(f'Первый пользователь: {user1}')
print(f'Второй пользователь: {user2}')

withdraw_friends = user1 & user2
print(f'Общих друзей {len(withdraw_friends)}')
for friend in withdraw_friends:
    print(friend)

