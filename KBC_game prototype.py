questions = [{
   "question": "What is the capital of India?",
   "options": ["1. Delhi", "2. Mumbai", "3. Kolkata", "4. Chennai"],
   "answer": 1
},{
   "question": "Which planet is known as the Red Planet?",
   "options": ["1. Jupiter", "2. Venus", "3. Mars", "4. Saturn"],
   "answer": 3
},{
   "question": "Who painted the Mona Lisa?",
   "options": ["1. Vincent van Gogh", "2. Pablo Picasso", "3. Leonardo da Vinci", "4. Claude Monet"],
   "answer": 3
}]

prize_won = 0
Running = True
que_no = 0

def show_que(num):
    print('\t\t',questions[num]['question'])
    print('\n')
    
def show_opt(num):
    for i in range(3):
        print('\t\t',questions[num]['options'][i],'\t')
    print('\n')
    
def check_ans(num,opt):
    if opt == questions[num]['answer'] - 1:
        return 1
    else:
        return -1

while Running:
    show_que(que_no)
    show_opt(que_no)
    ans = input("Enter your Answer:-  ")
    if check_ans(que_no,ans):
        prize_won += 10000
    else:
        print('Wrong answer')
        print('Your prize is: ',prize_won)
        Running = False
        
    if que_no==len(questions)-1:
        print('Game over')
        print("You have won amount:-  ", prize_won)
        Running = False
    else:
        que_no+=1
        
        
        
        
        
    
    
    

















