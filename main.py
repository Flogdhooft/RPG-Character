full_dot = '●'
empty_dot = '○'

def create_character(character_name, strength, intelligence, charisma):
    
    if isinstance(character_name, str) != True:
        return 'The character name should be a string'
    if len(character_name) <= 0:
        return 'The character should have a name'
    if len(character_name) > 10:
        return 'The character name is too long'
    if character_name.count(' '):
        return 'The character name should not contain spaces'

    if isinstance(strength, int) != True or isinstance(intelligence, int) != True or isinstance(charisma, int) != True:
        return 'All stats should be integers'
    if strength < 1 or intelligence < 1 or charisma < 1:
        return 'All stats should be no less than 1'
    if strength > 4 or intelligence > 4 or charisma > 4:
        return 'All stats should be no more than 4'
    if strength + intelligence + charisma != 7:
        return 'The character should start with 7 points'

    else:
        strength = 'STR ' + (full_dot * strength) + (empty_dot * (10 - strength))
        intelligence = 'INT ' + (full_dot * intelligence) + (empty_dot * (10 - intelligence))
        charisma = 'CHA ' + (full_dot * charisma) + (empty_dot * (10 - charisma))
        return f"{character_name}\n{strength}\n{intelligence}\n{charisma}"

print(create_character('ren', 4, 2, 1))