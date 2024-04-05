# Cat Swarm Optimization
Python implementation of an Swarm based Optimization algorithm, named Cat Swarm Optimization. This meta heuristic optimization technique was developed by Chu and Tsai (2007).Although there are many modified versions of CSO proposed, the original vanilla version is implemented.

Inspired from the behavior of a population of cats, where they are likely to be in either of the two modes, Seeking or Tracing Mode. Cats rather spend being alert in Seeking mode to conserve their energy to locate the pray before they execute their hunt. This process of locating the solution in a search space elaborates an efficient and accurate hunting behavior of cats.

This algorithm of cats can be utilised by choosing a population of cats interacting with the environment in an __M dimensional__ map with their position *X*<sub>(i,d)</sub> and velocity *v*<sub>(i,d)</sub>. Where *X*<sub>best</sub> is the best position searched by a cat in that search space. 

## *Seeking Mode (Resting)*
During this mode the cat is resting while keeping an eye on its environment. In case of sensing a prey or danger, the cat decides its next move. If the cat decides to move, it does that slowly and cautiously. Just like while resting, in the seeking mode the cat observes into the __M-dimensional__ solution space in order to decide its next move. In this situation, the cat is aware of it own situation, its environment, and the choices it can make for its movement. These are represented in the CSO algorithm by using four parameters: seeking memory pool (__SMP__), seeking range of the selected dimension (__SRD__), counts of dimension to change (__CDC__), and self-position consideration (__SPC__). SMP is the number of the copies made of each cat in the seeking process. SRD is the maximum difference between the new and old values in the dimension selected for mutation.__CDC__ tells how many dimensions will be mutated. All these parameters define the seeking process of the algorithm.__SPC__ is the Boolean variable which indicates the current position of the cat as a candidate position for movement. SPC cannot affect the value of __SMP__.

*X<sub>cn</sub>* = __(1 ± SRD × R) × *X<sub>c</sub>*__

in which,
*X<sub>c</sub>* current position

*X<sub>cn</sub>* new position

*R* a random number, which varies between 0 and 1


The probability parameter ***P<sub>i</sub>*** in the orginal litrature has been modified into aggressive allocation of the best solution among the involved population of cats in the seeking mode.Since this method proved stable and faster convergence towards a solution.

## *Tracing Mode (Movement)*
The tracing mode simulates the cat chasing a prey. After finding a prey while resting (seeking mode), the cat decides its movement speed and direction based on the prey's position and speed. In CSO, the velocity of the cat *k* in demension *d* is given by

__*v<sub>k,d</sub> = v<sub>k,d</sub> + r<sub>1</sub> × c<sub>1</sub>(X<sub>best,d</sub> - X<sub>k,d</sub>)*__

in which, __*v<sub>k,d</sub>*__ = velocity of cat *k* in dimension *d*; __*X<sub>best,d</sub>*__ = position of the cat with the best solution; __*X<sub>k,d</sub>*__ = position of the cat<sub>k</sub>; __*c<sub>1</sub>*__ = a constant; and __*r<sub>1</sub>*__ = a random value in the range [0,1]. Using this velocity, the cat moves in the __M-dimensional__
decision space and reports every new position it takes.If the velocity of the cat is greater than the maximum velocity, its velocity is set to the maximum velocity. The new position of each cat is calculated by

__*X<sub>k,d,new</sub> = X<sub>k,d,old</sub> + v<sub>k,d</sub>*__

in which __*X<sub>k,d,new</sub>*__ new position of cat *k* in dimension *d* ; and

__*X<sub>k,d,old</sub>*__ current position of cat *k* in dimension *d*.

-- *Refrenced from __Advanced Optimization by Nature-Inspired Algorithms by Omid Bozorg-Haddad__*

## Cost Function
One can customize their cost function, it is applicable to any type of __Univariate__ equations.




