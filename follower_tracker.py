import json

with open('/Users/nicolekwan/Workspace/insta/followers_1.json') as file:
    followers_json = json.load(file)

with open('/Users/nicolekwan/Workspace/insta/following.json') as file:
    following_json = json.load(file)

follower_list = []
following_list = []

for item in followers_json:
    follower_list.append(item["string_list_data"][0]["value"])

print()

for item in following_json["relationships_following"]:
    following_list.append(item["string_list_data"][0]["value"])

not_followers = [person for person in following_list if person not in follower_list]

print("People you are following but who are not your followers:")
for ind, user in enumerate(not_followers, start=1):
    print(f"{ind}: {user}")