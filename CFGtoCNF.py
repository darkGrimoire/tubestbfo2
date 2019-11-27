import os.path
GLOB_RULES = {}

def ReadGrammar(source):
    # Read CFG either from file or string
    if os.path.isfile(source):
        with open(source, 'r') as cfg:
            lines = cfg.readlines()
    else:
        lines = source.split("\n")
    return [x.strip().replace("->","").split() for x in lines]

def AddRule(rule):
    # Add rule to the GLOB_RULES
    global GLOB_RULES

    if rule[0] not in GLOB_RULES:
        GLOB_RULES[rule[0]] = []
    GLOB_RULES[rule[0]].append(rule[1:])

def CFGtoCNF(grammar):
    # Setup
    global GLOB_RULES
    unitProductions, result = [], []
    idx = 0

    # Main Algorithm
    for rule in grammar:
        newRules = []
        if len(rule) == 2 and rule[1][0] != "'":
            # Rule is already in form A -> x
            unitProductions.append(rule)
            AddRule(rule)
            continue
        elif len(rule) > 2:
            # Rule is in form A -> X B C or A -> X a.
            terminals = [(item, i) for i, item in enumerate(rule) if item[0] == "'"]
            if terminals:
                for item in terminals:
                    # Create a new non terminal symbol and replace the terminal symbol with it.
                    # The non terminal symbol derives the replaced terminal symbol.
                    rule[item[1]] = f"{rule[0]}{str(idx)}"
                    newRules += [f"{rule[0]}{str(idx)}", item[0]]
                idx += 1
            while len(rule) > 3:
                newRules += [f"{rule[0]}{str(idx)}", rule[1], rule[2]]
                rule = [rule[0]] + [f"{rule[0]}{str(idx)}"] + rule[3:]
                idx += 1
        # Adds the modified or unmodified (in case of A -> x i.e.) rules.
        AddRule(rule)
        result.append(rule)
        if newRules:
            result.append(newRules)
    # Handle the unit productions (A -> X)
    while unitProductions:
        rule = unitProductions.pop()
        if rule[1] in GLOB_RULES:
            for item in GLOB_RULES[rule[1]]:
                newRule = [rule[0]] + item
                if len(newRule) > 2 or newRule[1][0] == "'":
                    result.append(newRule)
                else:
                    unitProductions.append(newRule)
                AddRule(newRule)
    # print(result)
    with open('CNF.txt', 'w') as file:
        for element in result:
            if len(element)==3:
                file.write(f'{element[0]} -> {element[1]} {element[2]}\n')
            elif len(element)==2:
                file.write(f'{element[0]} -> {element[1]}\n')
    return result