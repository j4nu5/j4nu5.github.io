USACO setup
###########

:date: 2016-03-28
:tags: programming, usaco
:category: Programming
:authors: Kushagra Sinha


`USACO <http://www.usaco.org/>`_ is fun. Though it is fairly easy to get up
and running on the platform, there remain a few repetitive steps during
problem solving that can be automated. Here is a brief summary of my
automation steps:

1. Use a template. `Here <https://gist.github.com/j4nu5/d2b23dcdc20c9de48715>`_
   is mine. Save it as `template.cpp`:

.. gist:: j4nu5/d2b23dcdc20c9de48715 usaco_template.cpp c++

2. Save this script as `solve.sh` in the same directory as above:

.. gist:: j4nu5/55005626c282e056b753 usaco_solve.sh bash

3. All done!
   Whenever you're ready to begin coding a solution, simply execute
   `./solve.sh PROBLEM_NAME`

All the best!