import random
import time

questions = [
    {
        "question": "What is the capital of India?",
        "options": ["1. Delhi", "2. Mumbai", "3. Kolkata", "4. Chennai"],
        "answer": 1,
    },
    {
        "question": "Which planet is known as the Red Planet?",
        "options": ["1. Jupiter", "2. Venus", "3. Mars", "4. Saturn"],
        "answer": 3,
    },
    {
        "question": "Who painted the Mona Lisa?",
        "options": [
            "1. Vincent van Gogh",
            "2. Pablo Picasso",
            "3. Leonardo da Vinci",
            "4. Claude Monet",
        ],
        "answer": 3,
    },
    {
        "question": "In ODI Cricket, who created the record of scoring the fastest century in just 31 balls ?",
        "options": [
            "1. Virat Kohli",
            "2. David Warner",
            "3. AB De Villiers",
            "4. Chris Gayle",
        ],
        "answer": 3,
    },
    {
        "question": "Which is the Land of the Rising Sun? ",
        "options": ["1. India", "2. Vietnam", "3. New Zealand", "4. Japan"],
        "answer": 4,
    },
    {
        "question": "The desert that lies on the boundary between India and Pakistan \
  is ",
        "options": ["1. Sahara", "2. Thar", "3. Gobi", "4. Death valley"],
        "answer": 2,
    },
    {
        "question": "Oval stadium in England is associated with ?'",
        "options": ["1. Football", "2. Baseball", "3. Cricket", "4. Ice Hockey"],
        "answer": 3,
    },
    {
        "question": "Ronaldo is associated with ? ",
        "options": ["1. Football", "2. Cricket", "3. Kho-Kho", "4. Golf"],
        "answer": 1,
    },
]
num = 0
que_count = 1
prize_won = 0
Running = True
que_list = [0, 1, 2, 3, 4, 5, 6, 7]


def show_que(count):
    print("\n\t",count ,'. ',questions[num]["question"],"\n")
    for i in range(4):
        print("\t",questions[num]["options"][i], "\t")
    print("\n")
    count+=1


def check_ans(num, opt):
    print('1',questions[num]["answer"] - 1)
    if opt == questions[num]["answer"] :
        return 1
    else:
        return 0

def fifty_fifty(num):
    print('\n\n')
    time.sleep(1)
    ans = questions[num]["answer"]-1    
    lst = [0,1,2,3]
    lst.remove(ans)
    choice = random.choice(lst)
    if ans < choice:
        print('\t\t',questions[num]["options"][ans])
        print('\t\t',questions[num]["options"][choice])
    else:
       print('\t\t',questions[num]["options"][choice]) 
       print('\t\t',questions[num]["options"][ans])
    ans = int(input("Enter your Answer:-  "))
    return ans
    
    

time.sleep(1)
print("\n\t\t\tCHALIYE SHURU KARTE HAI, YE ADHBHUT KHEL\n\n\t\t\t\tKON BANEGA CROREPATI")
print("Rules:\n1.Enter int value between 1&4 for answers\n2.For fifty-fifty life line Enter 5 while answering")
time.sleep(2)

while Running:
    num = random.choice(que_list)
    show_que(que_count)
    try:
        ans = int(input("Enter your Answer:-  "))
        que_list.remove(num)
    except:
        print("enter valid input")
        time.sleep(1)
        continue
    print(ans) 
    time.sleep(2)
    if ans == 5 :
        ans = fifty_fifty(num)
     
    result = check_ans(num,ans)
    print(result)
    if result:
        print('checking')
        print("Your ans is correct")
        prize_won += 10000
        
    else:
        print("Wrong answer")
        print("Your prize is: ",prize_won)
        Running = False

    if len(que_list) == 0:
        print("Game over")
        print("You have won amount:-  ", prize_won)
        Running = False
