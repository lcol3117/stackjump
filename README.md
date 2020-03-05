# stackjump
a stack based but also functional language

# syntax

only symbols, no keywords to remember

\.\@\~\_\+\-\*\/\%\&\|\!\\\$\:\;\^\[\]

\.

PUT: Puts a value to the stack

\@

RET: Returns the top value over stdout

\~

REM: Removes the top value of the stack

\_

SWP: Swaps the top two elements on the stack

\+

ADD: Adds the top two elements, removes them, and adds the result

\-

SUB: Subtracts instead of adding

\*

MLT: Multiplies instead of subtracting

\/

DIV: Divides instead of multiplying

\%

MOD: Modulo instead of dividing

\&

AND: AND gate (logical)

\|

LOR: Logical OR gate

\!

NOT: NOT gate (Logical)

\\

NIL: The nil, null, or None value

\$

DEF: Defines a function

\:

END: Ends a function definition

\;

RUN: Runs a function

\^

RIF: Runs if the top value of the stack is 1

\[

CYC: Cycles the bottom value to the new top value of the stack

\]

LEN: Length of the stack is added to the stack
