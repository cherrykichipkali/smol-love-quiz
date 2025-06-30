print("----------------  PUT YOUR LOVE TO TEST🧐 --------------")
print("      WARNING: BETTER SCORE WELL ELSE U ARE SO DEAD      \n")

ques = (
    'when did we meet for the first time?(u dare not open ur calender ticket or gallery😒🔪)',
    'how many times do u piss me off in a day? and if im mad at u how long do you think it lasts???',
    'what colour do i think looks the best on me?😎',
    'what do i get the most attracted to?',
    'which is my fav movie????',
    'what would i love the most as my gift?😘',
    'my fav weather????????????????'
)

option = (
    ('1. 17 aug', '2. 16 aug ', '3. 15 aug', '4. 14 aug'),
    ('1. min 3 times and as i see ur text', '2. more than 5 n untill u apologise', '3. a million times and never',
     '4. veri little and as u say that u love me'),
    ('1. black/dark blue', '2. pink', '3. maroon/wine', '4. red'),
    ('1. paise', '2. sexyy bodii', '3. intelligence', '4. humour '),
    ('1. K3G', '2. bareily ki barfi', '3. phir hera pheri', '4. go goa gone'),
    ('1. jwellery', '2. indoor date while we cook together put on a movie n i sleep by ur side',
     '3.u track my periods and schedule n plan a trip ', '4. kapdeeeww'),
    ('1. freezing cold me cozyy', '2. windy and cloudy in nature', '3. little little barish and slight sunny',
     '4. crazy barish me cozy')
)

answers = ('4', '1', '3', '3', '2', '3', '2')

score = 0

for i in range(len(ques)):
    print(f"\nQ{i + 1}. {ques[i]}")
    for opt in option[i]:
        print(opt)

    ans = input("Your answer (1-4): ").strip()
    if ans == answers[i]:
        print("Correct!! 💖")
        score += 1
    else:
        print(f"Wronggg. The correct answer was option {answers[i]} 😒")

print("\n----------------- QUIZ ENDED -----------------")

import time

print("\n ur maut ka farman is in the making wait for ur score", end="")
for _ in range(3):
    time.sleep(1)
    print(".", end="")
print("\n")

print(f"Your score: {score}/{len(ques)}")

if score == len(ques):
    print("iloveeyouuuuuu ❤️")
elif (score >= len(ques) // 2):
    print("do you even know me?")
else:
    print("pata tha muje apse kuch nahi hoga🙂")
