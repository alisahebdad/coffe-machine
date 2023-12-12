# TODO 1: prepare resource
Menu = {
    'espresso': {
        'ingredients': {
            'water': 50,
            'coffe': 18,
        },
        'cost': 1.5
    },
    'latte': {
        'ingredients': {
            'water': 200,
            'milk': 150,
            'coffe': 24,
        },
        'cost': 2.5
    },
    'cappuccino': {
        'ingredients': {
            'water': 250,
            'milk': 100,
            'coffe': 24,
        },
        'cost': 3.0
    }
}

resource = {
    'water': 300,
    'milk': 200,
    'coffe': 100,
    'money': 0
}

unit = {
    'water': 'ml',
    'milk': 'ml',
    'coffe': 'g',
    'money': '$',
}


# TODO 2: Print report

def report():
    for key in resource:
        print(f'{key}: {resource[key]}{unit[key] if key in unit else ""}')


# TODO 3: Check resource sufficient

def check_resource(order: str):
    if order in Menu:
        for item in Menu[order]['ingredients']:
            if item in resource:
                if Menu[order]['ingredients'][item] > resource[item]:
                    print(f'Sorry there is not enough {item}.')
                    return False
            else:
                return False
        return True
    return False


# TODO 4: Process coin

def process_coin():
    coins = [('quarter', 0.25), ('dim', 0.10), ('nickle', 0.05), ('pennie', 0.01)]
    print('Please insert coins  ')
    total = 0
    for coin in coins:
        c = int(input(f'How many {coin[0]}s ? '))
        total = total + c * coin[1]
    return total


# TODO 5: Check transaction successful

# TODO 6: Make Coffe

def make_coffe(order: str):
    for item in Menu[order]['ingredients']:
        resource[item] = resource[item] - Menu[order]['ingredients'][item]
    resource['money'] = resource['money'] + Menu[order]['cost']
    print(f'Here is your {order} enjoy.')


# TODO 7: Command Prompt
def cmd():
    while True:
        _cmd = input(f'What would you like ({f"{[i for i in Menu.keys()]}"[1:-1]}) ? ')
        if _cmd == 'report':
            report()
        else:
            if _cmd not in Menu:
                print(f'command {_cmd} is not recognized ')
            else:
                if check_resource(_cmd):
                    payment = process_coin()
                    if payment > Menu[_cmd]['cost']:
                        make_coffe(_cmd)
                        print(f'Here is {round(payment - Menu[_cmd]["cost"],2)} in change.')
                    else:
                        print('Sorry that is not enough money.Money refused.')


if __name__ == '__main__':
    cmd()
