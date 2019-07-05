import random

name = input("What is your name?   ")
print("Hello, {}!".format(name))

print("Rolling the dice・・・")
all = 0
for i in range(2):
    num = random.randint(1,6)
    print("Die {}: {} ".format(i + 1,num))
    all += int(num)
print("Total value: {}".format(all))

if all > 7 :
    print("{} Won".format(name))
    print("やるやん。明日は俺にリベンジさせて。では、どうぞ")
else:
    print("{} Lose".format(name))
    print("負けは次につながるチャンスです！never give up！ほな、いただきます！")
