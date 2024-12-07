# Part 1
* Seems very straightforward (probably recurse, if the lists are small enough)
* I have some ideas of what part 2 will be, and I'm dreading it
* a couple of real dumb errors, but it worked more-or-less the way I expected it to
* the biggest boneheaded mistake I made was I was doing `solve(total - subtotal, values[2:])` but needed to do `solve(total, [subtotal] + values[2:])`

# Part 2
* easiest change to make part 2 work, ever
* added the `||` operator to my map, and then passed in the number of operators to use to my `solve()` method (and passed it down to recursive calls)