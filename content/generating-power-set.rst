Generating Power Set
####################

:date: 2015-01-05
:tags: programming
:category: Programming
:authors: Kushagra Sinha


Iterating over all possible subsets of a set is a problem that can arise not
only in competitive programming but also in day-to-day programming. While the
total number of possible subsets is quite huge (`2^n` where `n` is the
cardinality of the input set), often we want an algorithm that systematically
considers all subsets for small values of `n`.

A `power set <http://en.wikipedia.org/wiki/Power_set>`_ is a set of all subsets
of a given input set. Often we may want to simply iterate over all members of
the power set, but sometimes (if we have enough memory) we may need the power
set itself. In the following post, I have attempted to present some algorithms
(with C++11 implementations) that solve both kinds of problems (simple
iteration and complete power set construction).

Recursive algorithm for power set generation
============================================

Power set generation is a problem that yields naturally to a recursive
algorithm. Consider a set say, :math:`\lbrace 1, 2, 3, 4 \rbrace`. If we had a
function that can generate the power set, :math:`\mathbb{S}`, of
:math:`\lbrace 2, 3, 4 \rbrace` we can generate the power set of the original
input set by appending 1 to each member of :math:`\mathbb{S}` (call the result
:math:`\mathbb{T}`) and then taking the union of :math:`\mathbb{S}` and
:math:`\mathbb{T}`.

As an example, let us try generating the powerset of :math:`\lbrace 1, 2, 3 \rbrace`.
The power set of :math:`\lbrace 2, 3 \rbrace, \mathbb{S},` is
:math:`\lbrace \phi, \lbrace 2 \rbrace , \lbrace 3 \rbrace , \lbrace 2, 3 \rbrace  \rbrace`.
Adding :math:`1` to each member of :math:`\mathbb{S}`, gives us, :math:`\mathbb{T}`,
:math:`\lbrace \lbrace 1 \rbrace, \lbrace 1, 2 \rbrace, \lbrace 1, 3 \rbrace, \lbrace 1, 2, 3 \rbrace \rbrace`.
Union of :math:`\mathbb{S}` and :math:`\mathbb{T}` gives us the required answer:
:math:`\lbrace \phi, \lbrace 2 \rbrace , \lbrace 3 \rbrace , \lbrace 2, 3 \rbrace, \lbrace 1 \rbrace, \lbrace 1, 2 \rbrace, \lbrace 1, 3 \rbrace, \lbrace 1, 2, 3 \rbrace \rbrace`.

Translating the above idea to code (C++11):

.. code-block:: cpp

    // Accepts a set of integers and optionally a position to start reading the
    // array from.
    // Returns the powerset of integers from arr [pos=0 ... arr.size()-1]
    vector< vector<int> > powerset1(const vector<int> &arr, int pos=0) {
        int arr_size = arr.size();
        vector< vector<int> > results;

        if (pos >= arr_size) {
            // Recursion base case
            results.push_back(vector<int>());
            return results;
        }

        vector< vector<int> > rest = powerset1(arr, pos+1);
        results = rest;
        for (auto &subset : rest) {
            subset.push_back(arr[pos]);
            results.push_back(subset);
        }
        return results;
    }

I have assumed a set of integers that do not have duplicates. The code can be
easily modified to accept other datatypes or maybe templates. If the vector has
duplicate elements, just copy and deduplicate it before passing.

Since this method returns the complete power set, the space complexity is of the
order of `2 ^ n`. The time complexity is exponential.

Iterative algorithm, same idea
==============================

.. code-block:: cpp

    vector< vector<int> > powerset2(const vector<int> &arr) {
        int arr_size = arr.size();
    
        vector< vector<int> > pset;
        pset.push_back(vector<int>());
    
        for (int pos = 0; pos < arr_size; pos++) {
            vector< vector<int> > tmp(pset);
            for (auto &subset : tmp)
                subset.push_back(arr[pos]);
            copy(tmp.begin(), tmp.end(), back_inserter(pset));
        }
    
        return pset;
    }

Iterating over power set, using a bitmask (lexical ordering)
============================================================

We can use a bitmask of length = size of input set to denote a subset choice.
For example, a selection of {1, 2} in {1, 2, 3, 4} can be denoted by 0011,
where the LSB (least significant bit) denotes 0th index and MSB denotes the
higest possible index (`arr.size() - 1`). :math:`\phi` is denoted by 0000 and a
selection of all integers is denoted by 1111.

According to this idea, each set in the powerset can be represented by a bitmask.
Therefore, iterating over all possible bitmasks will do the trick. Note that
all possible bitmasks of length `n` is simply [0 ... 2^n - 1].

This solution is sufficient for most practical applications running on a single
computer. I am going to use a 64-bit unsigned long long for this. If you have a
set bigger than this, you cannot do it in a reasonable amount of time on a
single machine.

.. code-block:: cpp

    void powerset3(const vector<int> &arr) {
        int arr_size = arr.size();

        unsigned long long lim = (1 << arr_size) - 1;
        for (unsigned long long i = 0; i <= lim; i++) {
            unsigned long long mask = i;

            for (int idx = 0; idx < sizeof(mask) * 8; idx++) {
                if ((mask >> idx) & 1)
                    cout << arr[idx] << " ";
            }
            cout << "\n";
        }
    }

Iterating over power set, using banker's sequence
=================================================

Using `banker's sequence <http://applied-math.org/subset.pdf>`_ we can generate
subsets in a monotonically increasing order of cardinality. Depending on your
use case, it may be extremely useful. The idea is to use a bitmask as before
but we will consider all bitmasks with set bits = k before we consider any
mask with set bits > k.

.. code-block:: cpp

    void powerset4(const vector<int> &arr) {
        int arr_size = arr.size();
        vector<bool> mask(arr_size, false);
    
        for (int i = 0; i <= arr_size; i++) {
            fill(mask.begin(), mask.end()-i, false);
            fill(mask.end()-i, mask.end(), true);
    
            do {
                for (int j = 0; j < arr_size; j++) {
                    if (mask[j])
                        cout << arr[j] << " ";
                }
                cout << "\n";
            } while(next_permutation(mask.begin(), mask.end()));
        }
    }

Conclusion
==========

As Donald Knuth once remarked, there seems to be as many algorithms for
unsorting data as there are for sorting it. There are many approaches and
algorithms for power set generation. I hope I have provided a decent coverage
of the most popular ones.

As always, comments are welcome.
