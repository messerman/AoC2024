# Part 1
* I liked this one - pretty much just a mathy approach
* I up-front calculated where you'd end up by pressing each button x times (from 0-100), and then stored that (for each button) in a dict with the position as the key and the number of presses as the button
* Looped through B's offsets, first, and then checked for what was needed in A's offsets
* cost calculation per machine: `min(map(lambda x: 3*x[0] + x[1], solutions))`

# Part 2
* 