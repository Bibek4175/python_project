import json

quiz_data = {
    "quiz": {
        "sport": {
            "q1": {
                "question": "Which one is correct team name in NBA?",
                "options": [
                    "New York Bulls",
                    "Los Angeles Kings",
                    "Golden State Warriros",
                    "Huston Rocket"
                ],
                "answer": "Huston Rocket"
            }
        },
        "maths": {
            "q1": {
                "question": "5 + 7 = ?",
                "options": [
                    "10",
                    "11",
                    "12",
                    "13"
                ],
                "answer": "12"
            },
            "q2": {
                "question": "12 - 8 = ?",
                "options": [
                    "1",
                    "2",
                    "3",
                    "4"
                ],
                "answer": "4"
            }
        }
    }
}

with open("quiz.json",mode  = 'w',encoding='utf-8') as write_file:
	json.dump(quiz_data,write_file)


with open("quiz.json",mode='r',encoding='utf-8') as read_file:
	data = json.load(read_file)

print(type(data))


name = {1:{"name":"RAM","Age":23,"Gender":"Male"}}

name_str = json.dumps(name)
print(type(name_str))			
name_json = json.loads(name_str)
print(type(name_json))
