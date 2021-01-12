import json
import requests

{

},

data = {
    "postId": 1,
    "id": 5,
    "name": "vero eaque aliquid doloribus et culpa",
    "email": "Hayden@althea.biz",
    "body": "harum non quasi et ratione\ntempore iure ex voluptates in ratione\nharum architecto fugit inventore cupiditate\nvoluptates magni quo et"
}

with open("json_files/data_file.json", "w") as write_file:
    json.dump(data, write_file)

json_string = json.dumps(data)
print(json_string)

json_string_indentation = json.dumps(data, indent=4)
print(json_string_indentation)

new_clothes = ("Price", 420)
encoded_clothes = json.dumps(new_clothes)
decoded_clothes = json.loads(encoded_clothes)

print(new_clothes == encoded_clothes)
print(type(new_clothes))
print(type(decoded_clothes))
print(new_clothes == tuple(decoded_clothes))

with open("json_files/data_file.json", "r") as read_file:
    data = json.load(read_file)
print(data)

json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}
"""
data = json.loads(json_string)
print(data)

response = requests.get("https://jsonplaceholder.typicode.com/comments")
comments = json.loads(response.text)

print(response.json() == comments)
print(type(comments))
print(comments[:10])

comments_by_user = {}
for comment in comments:
    try:
        if len(comments["body"]) > comments_by_user[comments["postId"]]:
            comments_by_user[comments["potId"]] = len(comments["body"])
    except KeyError:
        comments_by_user[comments["postId"]] = len(comments["body"])

longest_comment = sorted(comments_by_user.items(),
                         key=lambda x: x[1], reverse=True)
print(comments_by_user)
print(longest_comment)

users_longest_comments = []
for longest in longest_comment:
    if longest_comment[0][1] > longest[1]:
        break
    users_longest_comments.append(str(longest[0]))

user_string = " and ".join(users_longest_comments)
s = "s" if len(users_longest_comments) > 1 else ""
print(f'User{s} {user_string} wrote the longest post with {longest_comment[0][1]} signs')

posts = longest_comment[:5]


def keep(comment):
    counter = False
    for comment in comments:
        if comment[1] == len(comment["body"]) and comment["userId"] == comment[0]:
            counter = True
    return counter


with open("json_files/filtered_data_file.json", "w") as data_file:
    filtered_comments = list(filter(keep, comments))
    json.dump(filtered_comments, data_file, indent=2)


class Elf:
    def __init__(self, level, ability_scores=None):
        self.level = level
        self.ability_scores = {
            "str": 11, "dex": 12, "con": 10,
            "int": 16, "wis": 14, "cha": 13
        } if ability_scores is None else ability_scores
        self.hp = 10 + self.ability_scores["con"]


try:
    elf = Elf(level=4)
    json.dumps(elf)
except TypeError as type_error:
    print("A TypeError has occurred!")
    print("Message: ", type_error.args[0])


def encode_complex(z):
    if isinstance(z, complex):
        return (z.real, z.imag)
    else:
        type_name = z.__class__.__name__
        raise TypeError(f"Object of type '{type_name}' is not JSON serializable")


json.dumps(9 + 5j, default=encode_complex)


class ComplexEncoder(json.JSONEncoder):
    def default(self, z):
        if isinstance(z, complex):
            return (z.real, z.imag)
        else:
            return super().default(z)


print(json.dumps(2 + 5j, cls=ComplexEncoder))
encode = ComplexEncoder()
encode.encode(3 + 6j)

complex_json = json.dumps(4+17J,cls=ComplexEncoder)
json.loads(complex_json)

def decode_complex(dct):
    if "__complex__" in dct:
        return complex(dct["real"], dct["imag"])
    return dct

with open("json_files/complex_data.json") as complex_data:
    data=complex_data.read()
    z=json.loads(data, object_hook=decode_complex)

print(type(z))
z