# Part 1
* easy parsing
* hardest part was keeping my logic straight with all my "nots" and "xors"
* `return sum(map(isSafe, data))`
# Part 2
* There are several ways I could approach this, but I'm going to take the inefficient one, because I believe I can do it quickly, and the data set isn't too bad
* That worked - my easy approach was to simply pop out each element in the list, one at a time, check if its safe, and if not, then I put it back in and try with the next one