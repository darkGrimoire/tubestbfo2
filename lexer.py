import re
import sys
import os.path

class Token(object):
    def __init__(self, type, val, pos):
        self.type = type
        self.val = val
        self.pos = pos

    def __str__(self):
        return f"{self.type}({self.val}) at {self.pos}"

    def __repr__(self):
        return f"{self.type} "


class LexerError(Exception):
    def __init__(self, pos):
        self.pos = pos


class Lexer(object):
    def __init__(self, rules, skip_whitespace=True):
        idx = 1
        regex_parts = []
        self.group_type = {}

        for regex, type in rules:
            groupname = f"GROUP{idx}"
            regex_parts.append(f'(?P<{groupname}>{regex})')
            self.group_type[groupname] = type
            idx += 1
        self.regex = re.compile('|'.join(regex_parts))
        self.skip_whitespace = skip_whitespace
        self.re_ws_skip = re.compile('\S')

    def input(self, buf):
        source = ''
        if os.path.isfile(buf):
            with open(buf, "r") as file:
                lines = file.readlines()
                for line in lines:
                    source += line
                
        else:
            source = buf
        print(source)
        self.buf = source
        self.pos = 0

    def token(self):
        if self.pos >= len(self.buf):
            return None
        else:
            if self.skip_whitespace:
                m = self.re_ws_skip.search(self.buf, self.pos)

                if m:
                    self.pos = m.start()
                else:
                    return None

            m = self.regex.match(self.buf, self.pos)
            if m:
                groupname = m.lastgroup
                tok_type = self.group_type[groupname]
                tok = Token(tok_type, m.group(groupname), self.pos)
                self.pos = m.end()
                return tok

            # if we're here, no rule matched
            raise LexerError(self.pos)

    def tokens(self):
        while 1:
            tok = self.token()
            if tok is None: break
            yield tok


if __name__ == '__main__':
    rules = [
        # COMMENTS
        ('#.*\n',                     'COMMENT'),
        ('"""[\s\S]*"""',             'COMMENT'),
        ("'''[\s\S]*'''",             'COMMENT'),
        # TYPES
        ('\d+\.\d+',             'TYPE_FLOAT'),
        ('\d+',                  'TYPE_INT'),
        ('\"[^"]*\"',            'TYPE_STRING'),
        ("\'[^']*\'",            'TYPE_STRING'),
        ("True",                 'BOOL_TRUE'),
        ("False",                'BOOL_FALSE'),
        ("None",                 'TYPE_NONE'),
        # TYPE HINTING
        ("dict",                'TYPEH_DICT'),
        ("list",                'TYPEH_LIST'),
        ("int",                 'TYPEH_INT'),
        ("str",                 'TYPEH_STR'),
        ("float",               'TYPEH_FLOAT'),
        ("bool",                'TYPEH_BOOL'),
        ("bytes",               'TYPEH_BYTES'),
        ("->",                  'TYPEH_TO'),
        # TABS AND NEW LINE
        # ('\\n',              'NEWLINE'),
        # ('\t',              'ASSOP_PLUS')
        # ASSIGNMENT OPERATOR
        ('\+=',              'ASSOP_PLUS'),
        ('\-=',              'ASSOP_MINUS'),
        ('\*=',              'ASSOP_MULTIPLY'),
        ('\/=',              'ASSOP_DIVIDE'),
        ('%=',               'ASSOP_MODULO'),
        ('\/\/=',            'ASSOP_FLOOR_DIVIDE'),
        ('\*\*=',            'ASSOP_EXPONENTIAL'),
        # ARITH OPERATOR
        ('\/\/',            'OP_FLOOR_DIVIDE'),
        ('\*\*',            'OP_EXPONENTIAL'),
        ('\+',              'OP_PLUS'),
        ('\-',              'OP_MINUS'),
        ('\*',              'OP_MULTIPLY'),
        ('\/',              'OP_DIVIDE'),
        ('%',               'OP_MODULO'),
        # BRACKETS
        ('\(',              'OPEN_PAREN'),
        ('\)',              'CLOSE_PAREN'),
        ('\[',              'OPEN_BRACKET'),
        ('\]',              'CLOSE_BRACKET'),
        ('{',               'OPEN_CBRACKET'),
        ('}',               'CLOSE_CBRACKET'),
        # COMMA and DOT
        ('\.',              'DOT'),
        (',',              'SEPARATOR'),
        # LOGICAL OPERATOR
        ('!',              'LOP_NOT'),
        ('&',              'LOP_AND'),
        ('\|',             'LOP_OR'),
        ('and\s+',            'LOP_AND'),
        ('not\s+',            'LOP_NOT'),
        ('or\s+',             'LOP_OR'),
        # COMPARATOR
        ('==',              'COMP_EQUALS'),
        ('!=',              'COMP_NOT_EQUALS'),
        ('>=',              'COMP_GREATER_EQU'),
        ('<=',              'COMP_LESS_EQU'),
        ('>',               'COMP_GREATER_THAN'),
        ('<',               'COMP_LESS_THAN'),
        # ASSIGNMENT
        ('=',               'ASSIGNMENT'),
        # RESERVED KEYWORDS
        ('from\s+',            'FROM'),
        ('import\s+',          'IMPORT'),
        ('as\s+',           'AS'),
        ('in\s+',              'IN'),
        ('is\s+',              'IS'),
        ('break',           'LOOP_BREAK'),
        ('continue',        'LOOP_CONTINUE'),
        ('class\s+',           'CLASS'),
        ('def\s+',             'DEF'),
        ('pass',            'PASS'),
        ('return\W',          'RETURN'),
        ('if\W',              'IF'),
        ('elif\W',            'ELIF'),
        ('else\W',            'ELSE'),
        ('for\s+',             'FOR'),
        ('while\W',           'WHILE'),
        ('raise\s+',           'RAISE'),
        ('with\s+',            'WITH'),
        (':',               'COLON'),
        # MANY NAMES
        ('[a-zA-Z_]\w*',    'OBJECT'),
    ]
    lx = Lexer(rules, skip_whitespace=True)
    lx.input('input1.txt')

    try:
        with open("lexered.txt", "w") as file:
            for tok in lx.tokens():
                file.write(f"{tok!r}")
                print(f"{tok}")
    except LexerError as err:
        print('LexerError at position %s' % err.pos)