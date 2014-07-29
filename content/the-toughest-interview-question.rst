The toughest interview question
###############################

:date: 2014-07-29
:tags: programming, interviews
:category: Programming
:authors: Kushagra Sinha


What is the output of the following C code snippet?

.. code-block:: c
   :linenos: none

   int n = 1;
   printf("%d %d %d\n", n++, ++n, n++ + ++n);

This is a tricky question. Any attempt to answer this question requires either
a deep understanding of your compiler's parser or a complete ignorance of C.
Even if you fall under the first category and know the ins and outs of your
favorite compiler, how do you know which is your *interviewer's* favorite
compiler?

The ANSI C language specification, you see, specifies neither the evaluation
order of function arguments nor the exact *side effect* evaluation time of
prefix and postfix operators. The answer to the above problem depends on the
compiler being used.

Unfortunately, these kinds of puzzles form the bulk of programming interview
questions for IT companies in India. They are even common in term papers in
colleges.

I could never fathom the utility of such questions. The correct answer,
*Depends on the compiler* is *never* an option for this question. What am I
supposed to do with this? Should I just evaluate from left to right and
calculate the side effects ASAP or should I try to second guess my interviewer
and assume that he/she is terribly confused by the C function call stack
convention and thinks that the compiler always evaluates from right to left?

One day I chanced upon a book that actually taught that C compilers evaluate
function arguments from right to left. This gem of a book is quite famous in
India. Its called *Let Us C*, written by the renowned
`Yashwant Kanetkar <https://en.wikipedia.org/wiki/Yashavant_Kanetkar>`_, who
according to his Wikipedia page,

    " ... has created, moulded and groomed many IT professionals in the last decade and half."

How poetic ...

If there is a single most important factor behind the stagnation of the Indian
IT industry, I think it is this book. Forget about complying to ANSI C
standards, it professes and quizzes on the areas of C that have deliberately
been left to the compiler. Professors and interviewers who unfortunately never
got a chance to study *K&R C* think of *Let Us C* as *the* authority on the C
programming language. Most of their questions are a straight copy-paste from
this book.

This is a sad state of affairs. Mainly because the people who *actually* know
C are *never* able to answer this question correctly. If you are one of them,
Congrats! You are on the right path towards mastering C.
