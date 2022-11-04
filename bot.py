import json


print('"Welcome to the HOTEL"')
def formating(text):
    text = text.lower()
    text = text.replace(".", '').replace("!", '').replace("?", '').replace(":", '').replace(";", '')
    text = text.split()
    return text
    

def read_data():
    with open('data1.json') as f:
        return json.load(f)


def identify_question(question):    
    question = formating(question)
    cur_response = ''
    cur_acc = 0
    for i in data:
        for pattern in i["patterns"]:
            pattern = formating(pattern)
            cur_count = 0
            for my_words in question:
                if my_words in pattern:
                    cur_count += 1
            my_acc = cur_count / len(pattern)

            if my_acc > cur_acc:
                cur_acc = my_acc
                cur_response = i["response"]
                tag = i["tag"]

    if cur_acc < accuracy:
        cur_response = "Sorry I do not understand you.\n Try to formulate the question differently, or contact those. support support@gmail.com "
        tag = 'error'

    return cur_response, tag


accuracy = 0.3   # 0..100% of accuracy  // 0.5 = 50% 
data = read_data()

isRunning = True
while isRunning:
    question = input()
    response, tag = identify_question(question)
    print(response)
    if tag == 'stop':
        isRunning = False




