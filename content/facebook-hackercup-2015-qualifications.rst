Facebook Hacker Cup 2015 Qualification Round Solutions
######################################################

:date: 2015-01-12
:tags: programming, facebook hackercup 2015
:category: Programming
:authors: Kushagra Sinha


Facebook recently organized the qualification round of Hacker Cup 2015. They
posed some interesting problems and anyone who could get at least one problem
right can move to the next round.

I managed to get a rank of 217, with a perfect score of 100. I have posted my
solutions below with a little bit of commentary. You can access the problems
`here <https://www.facebook.com/hackercup/problems.php?round=742632349177460>`_.

Cooking the Books (15 points)
=============================

This was the easiest question. Since the constraints were so small, it suffices
to use brute force and try all possible swaps. Care has to be taken however to
make sure that a number never starts with 0.

Max number of digits in the input number is 9. Therefore we have 36 possible
swaps. For 100 test cases, we have a limit of 3600. Therefore we can easily
apply brute force.

.. code-block:: cpp

   #include <iostream>
   #include <algorithm>
   #include <string>

   using namespace std;

   int main() {
     int T;
     cin >> T;

     for (int t = 1; t <= T; t++) {
       long long N;
       cin >> N;

       string str = to_string(N);
       int len = str.length();

       string smallest(str), largest(str);
       for (int i = 0; i < len; i++) {
         for (int j = i+1; j < len; j++) {
           string tmp(str);
           swap(tmp[i], tmp[j]);

           if (tmp[0] != '0')
             smallest = min(smallest, tmp);
           largest = max(largest, tmp);
         }
       }

       cout << "Case #" << t << ": ";
       cout << smallest << " " << largest << "\n";
     }
     return 0;
   }

New Year's Resolution (30 points)
=================================

On the surface, it looks like a ghastly version of
`subset sum problem <http://en.wikipedia.org/wiki/Subset_sum_problem>`_ which
happens to be NP-complete.

However, if we look at the constraints of the problem we will notice that the
max number of food items is 20. Therefore, total possible number of food
choices is 2 ^ 20 = 1048576. Therefore, we will simply iterate over the power
set of all food items and try to find a combination that sums exactly to the
macro nutrients we need. I have covered power set generation in a separate
`blog post <|filename|generating-power-set.rst>`_.

.. code-block:: cpp

   #include <iostream>
   #include <fstream>
   #include <algorithm>
   #include <utility>
   #include <map>
   #include <set>
   #include <vector>
   #include <bitset>
   #include <string>
   #include <iomanip>
   #include <sstream>
   #include <queue>
   #include <stack>

   using namespace std;

   typedef long long int64;

   int64 P[20], C[20], F[20];

   int main() {
     ios_base::sync_with_stdio(0);
     cin.tie(0);

     int T;
     cin >> T;

     for (int t = 1; t <= T; t++) {
       int64 gp, gc, gf;
       cin >> gp >> gc >> gf;

       int N;
       cin >> N;
       for (int i = 0; i < N; i++) {
         cin >> P[i] >> C[i] >> F[i];
       }

       unsigned long long lim = (1UL << N) - 1;
       bool possible = false;
       for (unsigned long long mask = 0;
            mask <= lim; mask++) {
         int64 p, c, f;
         p = c = f = 0;

         for (int i = 0; i < N; i++) {
           if ((mask >> i) & 1) {
             p += P[i];
             c += C[i];
             f += F[i];
           }
         }

         if (p == gp && c == gc && f == gf) {
           possible = true;
           break;
         }
       }

       cout << "Case #" << t << ": ";
       if (possible)
         cout << "yes\n";
       else
         cout << "no\n";
     }
     return 0;
   }

Laser Maze (55 points)
======================

Let us forget about the lasers for now. This restricted version of the problem
can be solved using BFS. Adding lasers brings two complications:

1. We need to check for `safe` spaces. At any point in time, we cannot occupy
   a space which is being targeted by a laser.
2. The board's state is not a function of just player position anymore. It is
   now dependent on laser turrets configuration as well. Fortunately for us,
   all lasers turn simultaneously and can have only 4 possible states.

Taking these 2 modifications into consideration, we can now write a modified
BFS.

.. code-block:: cpp

   #include <iostream>
   #include <fstream>
   #include <algorithm>
   #include <utility>
   #include <map>
   #include <set>
   #include <vector>
   #include <bitset>
   #include <string>
   #include <iomanip>
   #include <sstream>
   #include <queue>
   #include <stack>

   using namespace std;

   typedef long long int64;

   char maze[100][100];
   bool visited[100][100][4];
   int64 dist[10000][4];
   const int64 INF = 1000000000000000000L;
   int N, M;

   inline int is_laser(int row, int col) {
     switch (maze[row][col]) {
       case '<':
         return 0;
       case '^':
         return 1;
       case '>':
         return 2;
       case 'v':
         return 3;
     }
     return 4;
   }

   bool is_safe(int row, int col, int state) {
     state = state % 4;
     if (row < 0 || row >= M || col < 0 || col >= N)
       return false;

     if (maze[row][col] != '.' && maze[row][col] != 'S' &&
            maze[row][col] != 'G')
       return false;

     // There should not be any laser in this row facing
     // in this direction
     for (int co = 1; col + co < N; co++) {
       int nr = row, nc = col + co;
       if (maze[nr][nc] == '#')
         break;

       int laserconf = is_laser(nr, nc);
       if (laserconf != 4) {
         int newstate = (laserconf + state) % 4;
         if (newstate == 0)
           return false;
         break;
       }
     }
     for (int co = -1; col + co >= 0; co--) {
       int nr = row, nc = col + co;
       if (maze[nr][nc] == '#')
         break;

       int laserconf = is_laser(nr, nc);
       if (laserconf != 4) {
         int newstate = (laserconf + state) % 4;
         if (newstate == 2)
           return false;
         break;
       }
     }
     // There should not be any laser in this col facing
     // in this direction
     for (int ro = 1; row + ro < M; ro++) {
       int nr = row + ro, nc = col;
       if (maze[nr][nc] == '#')
         break;

       int laserconf = is_laser(nr, nc);
       if (laserconf != 4) {
         int newstate = (laserconf + state) % 4;
         if (newstate == 1)
           return false;
         break;
       }
     }
     for (int ro = -1; row + ro >= 0; ro--) {
       int nr = row + ro, nc = col;
       if (maze[nr][nc] == '#')
         break;

       int laserconf = is_laser(nr, nc);
       if (laserconf != 4) {
         int newstate = (laserconf + state) % 4;
         if (newstate == 3)
           return false;
         break;
       }
     }
     return true;
   }

   int main() {
     ios_base::sync_with_stdio(0);
     cin.tie(0);

     int T;
     cin >> T;

     for (int t = 1; t <= T; t++) {
       cin >> M >> N;

       int source, dest;
       for (int i = 0; i < M; i++) {
         cin.ignore();
         for (int j = 0; j < N; j++) {
           cin >> maze[i][j];

           if (maze[i][j] == 'S')
             source = i * N + j;
           else if (maze[i][j] == 'G')
             dest = i * N + j;
         }
       }

       for (int i = 0; i < M; i++) {
         for (int j = 0; j < N; j++)
           for (int k = 0; k < 4; k++)
             visited[i][j][k] = false;
       }

       for (int i = 0; i < N*M; i++)
         for (int j = 0; j < 4; j++)
           dist[i][j] = INF;

       queue< pair<int, int> > Q;
       Q.emplace(source, 0);
       visited[source / N][source % N][0] = true;
       dist[source][0] = 0;

       while (!Q.empty()) {
         auto data = Q.front();
         int node = data.first;
         int state = data.second;
         Q.pop();

         int row = node / N, col = node % N;
         for (int ro = -1; ro <= 1; ro++) {
           for (int co = -1; co <= 1; co++) {
             if (!(ro * co) && (ro != co) &&
                 is_safe(row+ro, col+co, state+1) &&
                 !visited[row+ro][col+co][(state+1)%4]) {
               int child = (row + ro) * N + col + co;
               int newstate = (state + 1) % 4;
               dist[child][newstate] = min(
                 dist[child][newstate],
                 dist[node][state] + 1);
               visited[row+ro][col+co][(state+1)%4]=true;
               Q.emplace(child, (state+1) % 4);
             }
           }
         }
       }

       cout << "Case #" << t << ": ";
       int64 mindist = INF;
       for (int i = 0; i < 4; i++)
         mindist = min(mindist, dist[dest][i]);
       if (mindist != INF)
         cout << mindist << "\n";
       else
         cout << "impossible\n";
     }
     return 0;
   }

As always, comments are welcome.
