from .lexer import Lexer
from .pars import Parser
from .postfix_notation import PostfixNotation
from .stack_machine import StackMachine
from .triad_processing import Triad
from .thread_manager import ThreadManager
from .thread import Thread

def run(file: str, multithreaded: bool) -> list:
    print('\nlexer:')
    l = Lexer()
    tokens = l.lex(file)

    p = Parser(tokens)
    pars = p.lang()
    print('\nparser:', pars)

    if pars:
        pn = PostfixNotation(tokens)
        transfer, fun = pn.to_postfix()

        tr = Triad(transfer, fun)
        t, val = tr.triad_op()

        for i in range(len(fun)):
            print("\nFunctions triads processing:")
            triad = Triad(fun[i][-1], fun)
            fun[i][-1] = triad.triad_op(False)

        sm = StackMachine(t, val, fun)

        if multithreaded:
            main_th = Thread('main', StackMachine(t, val, fun))
            th_manager = ThreadManager([main_th])
            return th_manager.run()
        else:
            return sm.run()