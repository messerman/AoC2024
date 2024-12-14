# Part 1
* I liked this one - pretty much just brute forced it
* I up-front calculated where you'd end up by pressing each button x times (from 0-100), and then stored that (for each button) in a dict with the position as the key and the number of presses as the button
* Looped through B's offsets, first, and then checked for what was needed in A's offsets
* cost calculation per machine: `min(map(lambda x: 3*x[0] + x[1], solutions))`

# Part 2
* ugh, my part 1 solution isn't going to work here - it's too slow, I think I'll need to go more mathy
* potential solutions: LCM, binary search (instead of linear) for approaching prize, do equation equalities, etc
* math it is - simple little equation equality solution