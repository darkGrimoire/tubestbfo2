from os.path import isfile as isExist
import lexer
import CYKParser
import lexer_rules

""" FLAGS """
isBlockComment = False
isSkipUntilNextBC = False
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
                lexered = lexered[:posBC-1:]
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