"""
Вариант 15
Есть класс "Боксёр". От него создаются два экземпляра. Обоим боксёрам устанавливается здоровье в 100 очков.
В случайном порядке они бьют друг друга. Тот, кто бьет, здоровья не теряет. У того, кого бьют, 
оно уменьшается на 20 очков от одного удара. После каждого удара надо выводить сообщение, 
какой боксёр атаковал, и сколько у противника осталось здоровья. Как только у кого-то заканчивается ресурс здоровья, 
программа завершается сообщением о том, кто одержал победу. Историю и результаты боя записать в файл.

Доп. задание: добавить выбор удара и выбор блока
"""
# import boxer_KP
import boxer_KP1
import datetime
from random import randint as ri

#Game parameters
log = 'game_log.txt' #Log name
p_health = 100 #Start player's health points
c_health = 100 #Start computer's health points
damage = 20 #Damage value

#Log creating
f = open(log, 'w')
f.write('Start Logging\n')
f.close()


# receiving player's name
p_name = input(str(print("Hello, please enter your name:")))
p_name = p_name.capitalize()
if p_name:
    print("Hello, " + p_name)
else:
    print("Your name will be anonymous")
    p_name = "Anonymous player"

c_name = 'Computer'


pr = "Player's name: " + p_name + ', health = ' + str(p_health)
boxer_KP1.pr_to_file(pr, log)
pr = "Computer's name: " + c_name + ', health = ' + str(c_health)
boxer_KP1.pr_to_file(pr, log)

pr = ('Starting battle: ' + p_name + ' VS ' + c_name)
boxer_KP1.pr_to_file(pr, log)

# Choose the order of battle start
# Set up the play again loop
winner = None

# Choosing the first turn between computer and player
turn = ri(1, 2)
if turn == 1:
    p_turn = True
    c_turn = False
    pr = (p_name + " starts first.")
    boxer_KP1.pr_to_file(pr, log)
else:
    p_turn = False
    c_turn = True
    pr = (c_name + " starts first.")
    boxer_KP1.pr_to_file(pr, log)

# pr = (p_name + "'s" + " health: " + str(p_health) + "; " + c_name + "'s" + " health: " + str(c_health))
# boxer_KP1.pr_to_file(pr, log)

while p_health > 0 or c_health > 0:
    if p_turn:
        attack = input(str(print("Please choose the hit point: head(1), body(2) or legs(3)")))
        defend = str(ri(1, 3))
        if attack == defend:
            c_health = c_health
            pr = 'Attack: ' + str(attack) + 'Defend: ' + str(defend)
            boxer_KP1.pr_to_file(pr, log)
        else:
            c_health = c_health - damage
            pr = 'Attack: ' + str(attack) + 'Defend: ' + str(defend)
            boxer_KP1.pr_to_file(pr, log)
        if c_health <= 0:
            break
    if c_turn:
        attack = str(ri(1, 3))
        defend = input(str(print("Please choose the defend point: head(1), body(2) or legs(3)")))
        if attack == defend:
            p_health = p_health
            pr = 'Attack: ' + str(attack) + 'Defend: ' + str(defend)
            boxer_KP1.pr_to_file(pr, log)
        else:
            p_health = p_health - damage
            pr = 'Attack: ' + str(attack) + 'Defend: ' + str(defend)
            boxer_KP1.pr_to_file(pr, log)
        if p_health <= 0:
            break


    pr = (p_name + "'s" + " health: " + str(p_health) + "; " + c_name + "'s" + " health: " + str(c_health))
    boxer_KP1.pr_to_file(pr, log)

    turn = ri(1, 2)
    if turn == 1:
        p_turn = True
        c_turn = False
        pr = ("Next turn is " + p_name + "'s")
        boxer_KP1.pr_to_file(pr, log)
    else:
        p_turn = False
        c_turn = True
        pr = ("Next turn is " + c_name + "'s")
        boxer_KP1.pr_to_file(pr, log)
if p_health == 0:
    pr = (c_name + ' WON')
    boxer_KP1.pr_to_file(pr, log)
else:
    pr = (p_name + ' WON')
    boxer_KP1.pr_to_file(pr, log)
quit()

