# Selection: (Value, Win condition, Lose condition)
SELECTIONS = {
    'A': (1, 'C', 'B'),
    'B': (2, 'A', 'C'),
    'C': (3, 'B', 'A')
}

WIN = 6
DRAW = 3
LOSS = 0

OUTCOMES = {
    'X': LOSS,
    'Y': DRAW,
    'Z': WIN
}


def main(strategy_path: str):
    with open(strategy_path, 'r', encoding='utf-8') as handle:
        strategy = handle.read().split('\n')
    
    total = 0
    for round in strategy:
        opp = round[0]
        desired_outcome = OUTCOMES[round[2]]

        if desired_outcome == DRAW:
            user = opp
        elif desired_outcome == WIN:
            user = SELECTIONS[opp][2]
        else:
            user = SELECTIONS[opp][1]
        
        total += (SELECTIONS[user][0] + desired_outcome)

    print(total)

if __name__ == '__main__':
    main('day_2/input.txt')