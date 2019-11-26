import os.path
GLOB_RULES = {}

def ReadGrammar(source):
    # Read CFG either from file or string
    if os.path.isfile(source):
        with open(source) as cfg:
            lines = cfg.readlines()
    else:
        lines = source.split("\n")
    return [x.replace(" -> ","").split("|") for x in lines]

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
            # Rule is in form A -> X|B or A -> X|a

S -> FROM OBJ IMPORT OBJ AS OBJ

for i in range()
# GRAMMAR: ASSIGNMENT
S -> VAR EQU_SIGN STR
S -> VAR EQU_SIGN INT
S -> VAR EQU_SIGN FLOAT
S -> VAR EQU_SIGN ARRAY
ASSIGNMENT TYPE_VAR
VAR EQU_SIGN STR
VAR EQU_SIGN ARRAY