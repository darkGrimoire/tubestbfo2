from os.path import isfile as isExist
import lexer
import CYKParser
import lexer_rules

""" FLAGS """
isBlockComment = False
isSkipUntilNextBC = False
isDef = False
isIfLevel = []
level = 0
isAccepted = True


""" MAIN PROGRAM """
inputfile = input('input file: ')
grammarfile = input('grammar file: ')
if isExist(inputfile) and isExist(grammarfile):
    # Setup Lexer and CYK Grammar
    lx = lexer.Lexer(lexer_rules.rules, skip_whitespace=True)
    CYK = CYKParser.Parser(grammarfile)
    # Open File
    with open(inputfile, 'r') as file:
        lines = file.readlines()
    for line in lines:
        lexered = ''
        # Lexer each line in file
        lx.input(line)
        try:
            for tok in lx.tokens():
                lexered += f'{tok!r}'
                # print(lexered)
        except lexer.LexerError as err:
            print(f'LexerError at position {err.pos}')
        # Remove Comment, check block comments
        print(lexered)
        if "BBCOMMENT" in lexered:
            lexered = lexered.replace("BBCOMMENT ","")
        if "BCOMMENT" in lexered:
            if not isSkipUntilNextBC:
                isBlockComment = True
                posBC = lexered.find("BCOMMENT")
                if posBC == 0:
                    lexered = ''
                else:
                    lexered = lexered[:posBC:]
            else:
                isSkipUntilNextBC = False
                posBC = lexered.find("BCOMMENT")
                lexered = lexered[posBC+9::]
        # print(isBlockComment)
        if isSkipUntilNextBC:
            continue
        if "COMMENT" in lexered:
            lexered = lexered.replace("COMMENT ","")
        print(lexered)
        # if DEF is in lexered
        # if "DEF" in lexered:
        #     level+=1
        #     isDef = True
        #
        # if IF is in lexered
        if "IF" in lexered:
            level+=1
            isIfLevel.append(level)
        # Elif and else must be followed with if first
        if ("ELIF" or "ELSE") in lexered:
            print('uwu')
            if level not in isIfLevel:
                isAccepted = False
                break
            elif "ELSE" in lexered:
                isIfLevel.remove(level)
                level-=1
        # Parse lexered line
        CYK(lexered,parse=True)
        isAccepted = CYK.print_tree(output=True)
        if not isAccepted:
            break
        if isBlockComment:
            isSkipUntilNextBC = True
            isBlockComment = False
    if isAccepted:
        print("Accepted")
    else:
        print("Syntax Error")
else:
    print("file not exist!")