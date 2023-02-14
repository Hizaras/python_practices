users = [
    {'name': 'Ibrahim',
     'age': 32,
     'gender': 'male',
     'user_name': 'Ibro',
     'is_verified': False,
     'tweets': [
         {'content': 'PO for President', 'likes': 450, 'retweets': 233},
         {'content': 'Atiku is our man', 'likes': 4, 'retweets': 12}
     ]
     },

    {'name': 'Racheal',
     'age': 21,
     'gender': 'Female',
     'user_name': 'betty',
     'is_verified': False,
     'tweets': [
         {'content': '', 'likes': 450, 'retweets': 233},
         {'content': 'Thinking about amez', 'likes': 4, 'retweets': 2},
         {'content': 'Amazing grace', 'likes': 2000, 'retweets': 1542}
     ]
     },

    {'name': 'James',
     'age': 25,
     'gender': 'male',
     'user_name': 'amez',
     'is_verified': True,
     'tweets': [
         {'content': 'Love is life', 'likes': 66, 'retweets': 89},
         {'content': 'only Racheal i know', 'likes': 97, 'retweets': 2}
     ]
     },

    {'name': 'Dorris',
     'age': 16,
     'gender': 'Female',
     'user_name': 'anything',
     'is_verified': False,
     'tweets': [
         {'content': 'i love chimamanda Adichie', 'likes': 450, 'retweets': 233},
         {'content': ' Feminism is the goal', 'likes': 4, 'retweets': 2}
     ]
     },

    {'name': 'Jacob',
     'age': 37,
     'gender': 'male',
     'user_name': 'elder_j',
     'is_verified': True,
     'tweets': [
         {'content': 'Reflection is my goal', 'likes': 5, 'retweets': 3},
         {'content': 'How to get more likes on twitter', 'likes': 1, 'retweets': 1}
     ]
     },

    {'name': 'Derrick',
     'age': 29,
     'gender': 'Male',
     'user_name': 'standby_gen',
     'is_verified': False,
     'tweets': [
     ]
     },

    {'name': 'Mubarak',
     'age': 47,
     'gender': 'Male',
     'user_name': 'Whistle',
     'is_verified': True,
     'tweets': [

     ]
     },

    {'name': 'Elijah',
     'age': 16,
     'gender': 'male',
     'user_name': 'el_di_si',
     'is_verified': True,
     'tweets': [
         {'content': 'PO for President', 'likes': 450, 'retweets': 233},
         {'content': 'Atiku is our man', 'likes': 4, 'retweets': 2}
     ]
     },

    {'name': 'Hadizaa',
     'age': 21,
     'gender': 'Female',
     'user_name': 'deeza',
     'is_verified': True,
     'tweets': [
         {'content': 'PO for President', 'likes': 450, 'retweets': 233},
         {'content': 'Atiku is our man', 'likes': 4, 'retweets': 2}
     ]
     }
]

no_of_users = len(users)
user_names = {user['user_name'] for user in users}
female_users = [user['name'] for user in users if user['gender'] == 'Female']
inactive_users = [user for user in users if len(user['tweets']) == 0]
name_and_age = [{'name': user['name'], 'age': user['age']} for user in users]
avrg_age_of_users = round(sum(user['age'] for user in users)/ len(users))
print(name_and_age)
print(female_users)
