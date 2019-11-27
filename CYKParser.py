import os.path
import CFGtoCNF as converter
import argparse

class Node:
    def __init__(self, symbol, child1, child2=None):
        self.symbol = symbol
        self.child1 = child1
        self.child2 = child2

    def __repr__(self):
        return self.symbol

class Parser:
    def __init__(self, grammar):
        self.parse_table = None
        self.prods = {}
        self.grammar = None
        self.read_grammar(grammar)

    def __call__(self, sentence, parse=False):
        self.input = sentence.split()
        if parse:
            self.parse()

    def read_grammar(self, grammar):
        self.grammar = converter.CFGtoCNF(converter.ReadGrammar(grammar))
        # print(self.grammar)

    def parse(self):
        length = len(self.input)
        if length>0:
            self.parse_table = [[[] for x in range(length - y)] for y in range(length)]
            for i, word in enumerate(self.input):
                for rule in self.grammar:
                    # print(rule)
                    if f"'{word}'" == rule[1]:
                        self.parse_table[0][i].append(Node(rule[0], word))
            for words_to_consider in range(2, length + 1):
                for starting_cell in range(0, length - words_to_consider + 1):
                    for left_size in range(1, words_to_consider):
                        right_size = words_to_consider - left_size

                        left_cell = self.parse_table[left_size - 1][starting_cell]
                        right_cell = self.parse_table[right_size - 1][starting_cell + left_size]

                        for rule in self.grammar:
                            left_nodes = [n for n in left_cell if n.symbol == rule[1]]
                            if left_nodes:
                                right_nodes = [n for n in right_cell if n.symbol == rule[2]]
                                self.parse_table[words_to_consider - 1][starting_cell].extend(
                                    [Node(rule[0], left, right) for left in left_nodes for right in right_nodes]
                                )

    def print_tree(self, output=True):
        start_symbol = "S"
        # print(len(self.input))
        if len(self.input) == 0:
            if output:
                print("Nothing to parse! Either comment or it really is empty")
            return True
        else:
            final_nodes = [n for n in self.parse_table[-1][0] if n.symbol == start_symbol]
            if final_nodes:
                if output:
                    print("The given sentence is contained in the language produced by the given grammar!")
                    print("\nPossible parse(s):")
                trees = [generate_tree(node) for node in final_nodes]
                if output:
                    for tree in trees:
                        print(tree)
                    return True
                else:
                    return True
            else:
                if output:
                    print("The given sentence is not contained in the language produced by the given grammar!")
                    print(self.parse_table)
                return False


def generate_tree(node):
    if node.child2 is None:
        return f"[{node.symbol} '{node.child1}']"
    return f"[{node.symbol} {generate_tree(node.child1)} {generate_tree(node.child2)}]"


if __name__ == '__main__':
    argparser = argparse.ArgumentParser()
    argparser.add_argument("grammar",
                           help="File containing the grammar or string directly representing the grammar.")
    argparser.add_argument("sentence",
                           help="File containing the sentence or string directly representing the sentence.")
    args = argparser.parse_args()
    CYK = Parser(args.grammar)
    CYK(args.sentence,True)
    CYK.print_tree()
