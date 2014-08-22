Code Kata: Leapfrog Puzzle
===============

Puzzle: Imagine you have a list of numbers, each number represents a 'jump code' to tell you how many steps forwards or backwards you must jump relative to your current space.

Given a list of such numbers calculate how many jumps it will take to leave the list. If the list falls into an infinite loop, return -1

For example:

Given the list 2,3,-1,1,3  it will take four jumps to leave the list.

- Starting at the first space (ie the 2)
- 1st hop: Jump 2 spaces to the -1
- 2nd hop: Jump back one space to the 3
- 3rd hop: Jump forwards 3 spaces to the three at the end
- 4th hop: Attempt to jump three spaces... and leave the list

