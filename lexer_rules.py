rules = [
        # COMMENTS
        ('#.*',                     'COMMENT'),
        ('"""[^"]*"""',           'BBCOMMENT'),
        ("'''[\s\S]+'''",           'BBCOMMENT'),
        ('"""',                     'BCOMMENT'),
        ("'''",                     'BCOMMENT'),
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
        ('\.',             'DOT'),
        (',',              'SEPARATOR'),
        # BINARY OPERATOR
        ('~',            'BINOP_NEGATE'),
        ('\^',            'BINOP_XOR'),
        ('<<',           'BINOP_LEFTSHIFT'),
        ('>>',           'BINOP_RIGHTSHIFT'),
        # LOGICAL OPERATOR
        ('!',            'LOP_NOT'),
        ('&',            'LOP_AND'),
        ('\|',           'LOP_OR'),
        ('and\s+',       'LOP_AND'),
        ('not\s+',       'LOP_NOT'),
        ('or\s+',        'LOP_OR'),
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
        ('as\s+',              'AS'),
        ('in\s+',              'IN'),
        ('is\s+',              'IS'),
        ('break',              'LOOP_BREAK'),
        ('continue',           'LOOP_CONTINUE'),
        ('class\s+',           'CLASS'),
        ('def\s+',             'DEF'),
        ('pass',               'PASS'),
        ('return\W',           'RETURN'),
        ('if\W',               'IF'),
        ('elif\W',             'ELIF'),
        ('else',               'ELSE'),
        ('for\s+',             'FOR'),
        ('while\W',            'WHILE'),
        ('raise\s+',           'RAISE'),
        ('with\s+',            'WITH'),
        (':',                  'COLON'),
        # MANY NAMES
        ('[a-zA-Z_]\w*',    'OBJECT'),
    ]