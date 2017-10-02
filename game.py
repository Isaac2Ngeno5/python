import random


def simulate_roll(current_score, current_points, current_die, dice_count):
    print("Rolling", dice_count, "die")
    rolled_die = roll_die(current_die, dice_count)
    print("Rolled:", rolled_die, "\n")

    for r in get_repeating(rolled_die):
        print(rolled_die.count(r), "x", r, "worth", rolled_die.count(r) * r, "points. Set aside these die?")
        if get_choice("Enter 'yes' or 'no': ", ("yes", "no")) == "yes":
            print("Setting aside", rolled_die.count(r), "x", r, "for", rolled_die.count(r) * r, "points\n")
            current_points += rolled_die.count(r) * r
            dice_count -= rolled_die.count(r)
            current_die.remove(r)
        else:
            print("Keeping die\n")
    if dice_count == len(rolled_die):
        print("No die set aside - turn over!", current_points, "points lost!")
        return current_score
    elif dice_count <= 2:
        current_score += current_points
        print(current_points, "points secured.\n")
        return current_score

    print("You have", dice_count, "die remaining and", current_points, "points on the line")
    print("Roll remaining die or end turn to secure points?")
    if get_choice("Enter 'roll' or 'end': ", ("roll", "end")) == "roll":
        print("Rolling again...\n")
        return simulate_roll(current_score, current_points, current_die, dice_count)
    else:
        current_score += current_points
        print(current_points, "points secured.\n")
        return current_score


def get_choice(prompt, valid_choices):
    choice = input(prompt)
    if choice in valid_choices:
        return choice
    else:
        return get_choice(prompt, valid_choices)


def get_repeating(values):
    repeating_values = []
    for v in values:
        if values.count(v) > 1 and v not in repeating_values:
            repeating_values.append(v)
    return repeating_values


def roll_die(available_die, die_count):
    random_roll = []
    while len(random_roll) < die_count:
        r = random.randint(min(available_die), max(available_die))
        if r in available_die:
            random_roll.append(r)
    random_roll.sort()
    return random_roll

print("Starting game!\n")
if get_choice("Select difficulty level.\nEnter 'normal' or 'easy': ", ('normal', 'easy')) == "easy":
    turns = 4
else:
    turns = 3
score = 0
for turn in range(turns):
    print("Turn", turn + 1, "of", turns)
    print("Current Score:", score, "\n")
    points = 0
    die = [1, 2, 3, 4, 5, 6]
    score = simulate_roll(score, points, die, 6)

if score >= 60:
    print("Game over. Final score", score, "Excellent score, well done!")
elif score >= 50:
    print("Game over. Final score", score, "Great score!")
elif score >= 40:
    print("Game over. Final score", score, "Good score!")
else:
    print("Game over. Final score", score)
