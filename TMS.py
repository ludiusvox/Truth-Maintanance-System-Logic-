# -*- coding: utf-8 -*-
"""
Created on Wed Feb  3 17:47:21 2021

@author: cflynch
"""
import re
import sys
import regex
from utils4e import *
from logic4e import *
from notebook4e import psource


def KB_AgentProgram(KB):
    """A generic logical knowledge-based agent program. [Figure 7.1]"""
    steps = itertools.count()

    def program(percept):
        t = next(steps)
        KB.tell(make_percept_sentence(percept, t))
        action = KB.ask(make_action_query(t))
        KB.tell(make_action_sentence(action, t))
        return action

    def make_percept_sentence(percept, t):
        return Expr("Percept")(percept, t)

    def make_action_query(t):
        return expr("ShouldDo(action, {})".format(t))

    def make_action_sentence(action, t):
        return Expr("Did")(action[expr('action')], t)

    return program
def loadfile(Infile):
    with open(Infile, 'r') as f:
        lines = f.readlines()

    lines = [l.replace("\n", "") for l in lines]
    lines = [l.replace("Retract: ", "~") for l in lines]
    lines = [l.replace("Tell:", "") for l in lines]
    lines = [l.replace("+", "&") for l in lines]
    lines = [l.replace(">", "==>") for l in lines]
    lines = [l.replace(" ", "") for l in lines]


    return lines

    # Load a file.
    # Iterate over the file;
    #   For an add

    return False
def pl_fc_entails(KB, q):
    """Use forward chaining to see if a PropDefiniteKB entails symbol q.
    [Figure 7.15]
    >>> pl_fc_entails(horn_clauses_KB, expr('Q'))
    True
    """
    count = {c: len(conjuncts(c.args[0]))
             for c in KB.clauses
             if c.op == '==>'}
    inferred = defaultdict(bool)
    agenda = [s for s in KB.clauses if is_prop_symbol(s.op)]
    while agenda:
        p = agenda.pop()
        if p == q:
            return True
        if not inferred[p]:
            inferred[p] = True
            for c in KB.clauses_with_premise(p):
                count[c] -= 1
                if count[c] == 0:
                    agenda.append(c.args[1])
    return False
if __name__ == '__main__':
    InFile = sys.argv[1]
    l = loadfile(InFile)
    import logic4e

    clauses = ['A==>B',
               'C==>D',
               'A',
               '(C & B)==>E',
               '(E & D)==>F',
               'C',
               'A==>W',
               'retract(C)',
               '(A & C)==>D',
               'D'
               '(B & G)==>E',
               'G',
               'Z',
               'retract(A)']

    TT_kb = PropKB()
    (A, B, C, D, E, F, G, W, Z) = symbols('A, B, C, D, E, F, G, W, Z')
    (A, B, C, D, E, F, G, W, Z) = expr('A, B, C, D, E, F, G, W, Z')

    for clause in clauses:
        TT_kb.tell(clause)
    TT_kb.retract('A')
    TT_kb.retract('C')
    print(TT_kb.clauses)
    data = TT_kb.clauses
    eliminate_implications
    move_not_inwards
    distribute_and_over_or



    horn_clauses_KB = PropDefiniteKB()
    for clause in clauses:
        horn_clauses_KB.tell(expr(clause))
    print("A,B,C,D,E,F,G,W,Z")
    horn_clauses_KB.retract(C)
    horn_clauses_KB.retract(A)
    horn_clauses_KB.tell(D)
    print(pl_resolution(horn_clauses_KB,A),(pl_resolution(horn_clauses_KB,B)),(pl_resolution(horn_clauses_KB,C)),
    (pl_resolution(horn_clauses_KB, D)),(pl_resolution(horn_clauses_KB,E)),(pl_resolution(horn_clauses_KB,F)),
                                                                          (pl_resolution(horn_clauses_KB, G)),
                                                                           (pl_resolution(horn_clauses_KB, W)),
                                                                            (pl_resolution(horn_clauses_KB, Z)))











