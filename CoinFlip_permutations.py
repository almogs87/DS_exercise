import numpy as np


def tossing_perm_contest(toss_times, print_res=False):
# generating coin tossing results 0 stands for Head, 1 stand for Tails
    tossing_results = np.random.randint(0,2,toss_times)
    alice = 0
    bob = 0

    #Points loop
    # HH sequence or 00 will grant alice a point
    # HT sequence of 01 will grand bob a point

    for k in range(1,toss_times,1):
        if tossing_results[k - 1] == 0:
            if tossing_results[k] == 0:
                alice += 1
            else:
                bob += 1
    if print_res is True:
        msg_bob = "bob received {} points".format(bob)
        msg_alice = "alice received {} points".format(alice)
        print(tossing_results)
        print(msg_bob)
        print(msg_alice)

    return alice,bob

draw = 0
winner_bob = 0
winner_alice = 0
iter = 100000

toss_times = 100

for k in range(iter):
    alice,bob=tossing_perm_contest(toss_times)
    if bob == alice:
        draw = 1
    elif bob > alice:
        winner_bob += 1
    else:
        winner_alice += 1

winner_bob = round(100*winner_bob/iter,2)
winner_alice = round(100*winner_alice/iter,2)

msg_bob = "bob won {}% of contests".format(winner_bob)
msg_alice = "alice won {}% contests".format(winner_alice)
print(msg_bob)
print(msg_alice)