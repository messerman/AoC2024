# Part 1
* ugh, have to drag out my pygrid class from last year and see if I can make it work for this
* my pygrid class is apparently not very good, I may start from scratch
* built up a new Grid class (kept my old Position class, and extended it to a GridCell)
* Grid class has a `search_from` that allows me to get n-length strings starting from any cell, and in all directions (diagonals optional)

# Part 2
* that is NOT where I thought part 2 was going to go - I thought we'd have to deal with wrapping around the edges of the grid - the X thing is surprising
* I think I'm going to monkey-patch (or at least subclass) a "find X-MAS" method to my Grid class, and use that
* find all As, and search NW+SE, and NE+SW - both need to have both an M and an S to count
* subclass worked great