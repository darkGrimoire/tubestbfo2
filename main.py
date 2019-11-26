from os.path import isfile as isExist
import lexer
import CYKParser
import lexer_rules

""" FLAGS """
isBlockComment = False
isAccepted = True

""" MAIN PROGRAM """
inputfile = input('input file: ')
grammarfile = input('grammar file: ')
if isExist(inputfile) and isExist(grammarfile):
    lx = lexer.Lexer(lexer_rules.rules, skip_whitespace=True)
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
        # Parse lexered line
        CYK = CYKParser.Parser(grammarfile, lexered)
        CYK.parse()
        CYK.print_tree()
else:
    print("file not exist!")