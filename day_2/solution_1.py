OUTCOMES = {
    'X': (1, 'C', 'A'),
    'Y': (2, 'A', 'B'),
    'Z': (3, 'B', 'C')
}

WIN_VAL = 6
DRAW_VAL = 3
LOSS_VAL = 0


def main(strategy_path: str):
    with open(strategy_path, 'r', encoding='utf-8') as handle:
        strategy = handle.read().split('\n')
    
    total = 0
    for round in strategy:
        opp = round[0]
        user = round[2]
        selection_val, win_condition, draw_condition = OUTCOMES[user]
        
        if opp == draw_condition:
            total += (selection_val + DRAW_VAL)
        elif opp == win_condition:
            total += (selection_val + WIN_VAL)
        else:
            total += (selection_val + LOSS_VAL)

    print(total)

if __name__ == '__main__':
    main('day_2/input.txt')