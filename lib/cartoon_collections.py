def roll_call_dwarves(dwarf_names):
    i = 1
    while i <= len(dwarf_names):
        for name in dwarf_names:
            print(f"{i}. {name}")
            i += 1

def summon_captain_planet(planeteer_calls):
    excited_calls = [f"{call.title()}!" for call in planeteer_calls]
    return excited_calls

def long_planeteer_calls(planeteer_calls):
    call_lengths = [len(call) for call in planeteer_calls]
    longest_call = max(call_lengths)
    if longest_call > 4:
        return True
    else:
        return False

def find_the_cheese(list_of_strings):
    cheese_list = []
    for string in list_of_strings:
        if string == ("cheddar" or "gouda" or "camembert"):
            cheese_list.append(string)
    if len(cheese_list) > 0:
        return cheese_list[0]
    else:
        return None
