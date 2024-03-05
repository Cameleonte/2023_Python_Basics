animal_type = input()
data_output = ''

if animal_type == 'dog':
    data_output = 'mammal'
elif animal_type == 'crocodile':
    data_output = 'reptile'
elif animal_type == 'tortoise':
    data_output = 'reptile'
elif animal_type == 'snake':
    data_output = 'reptile'
else:
    data_output = 'unknown'

print(data_output)
