import random
def Guess(participants):
    my_participant_dict = {}
    for participant in participants:
        my_participant_dict[participant] = random.randint(1, 9)
        try:
            if "Larry" in my_participant_dict:
                if my_participant_dict['Larry'] == 9:
                    return True
                else:
                    raise KeyError("Poda dai")
        except KeyError as e:
                    print(e)
                    return None
participants = ['Cathy','Fred','Jack','Tom']
print(Guess(participants))