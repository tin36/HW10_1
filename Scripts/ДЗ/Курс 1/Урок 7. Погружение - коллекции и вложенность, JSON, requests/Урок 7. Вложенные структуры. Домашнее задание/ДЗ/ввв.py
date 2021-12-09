import json


# file = open("example.json", "w")
# data = ["mydata"]
# json.dump(data, file)

score = 2
correct_answer = 2
round_game = 4

with open('questions.json', "w+") as data_file:
    data = json.load(data_file)
    data['correct'].append(correct_answer)
    data['points'].append(score)
    data['incorrect'].append(round_game - correct_answer)
    json.dump(data, data_file)
    print(data)

# data = json.load(open('questions.json', 'rb'))
# data['- correct'].append(score)
# json.dumps(data, open('questions.json', 'wb'))
# print(data['- correct'])

# data3 = {
#     "points": [score],
#     "- correct": [correct_answer],
#     "incorrect" : [round_game - correct_answer],
#  }
#
# data = {
#     "points": [score],
#     "correct": correct_answer,
#     "incorrect" : round_game - correct_answer,
#  }



#json.dumps(data)
#with open('questions.json', 'a') as f:

# score=2
# correct_answer=3
# round_game = 4
#
# write_json = {
#     "points": score,
#     "correct": correct_answer,
#     "incorrect": round_game - correct_answer
#  }
#
# raw_json = json.dumps(write_json)
#
#
# with open('questions.json', 'a') as f:
#   f.write(f'{raw_json}\n')