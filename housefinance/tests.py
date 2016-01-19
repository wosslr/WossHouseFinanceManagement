from django.test import TestCase

# Create your tests here.

test_dict = {}
test_dict['201601'] = (2016, 1)
test_dict['201602'] = (2016, 2)
test_dict['201603'] = (2016, 3)
print(test_dict)
for tmp in test_dict:
    print(test_dict[tmp])

for key, value in test_dict.items():
    print(key)
    print(value)

if '201601' in test_dict:
    print('Yes')

if 'jshg' in test_dict:
    print('No')

print(test_dict.get('201601'))
print(test_dict.get('sggd'))

if test_dict.get('201601'):
    print('Get')

if test_dict.get('sgd'):
    print('No Get')