# Part 1
* seems like a brute force approach is the right way for part 1, given that I have no idea what part 2 will be
* making a Guard class that will walk around my Grid as instructed
* got wrapped around the axle on some order-of-operations issues when trying to handle the "guard goes out of bounds" case, but eventually got it right - these problems are hard when you're tired

# Part 2
* oh, this seems like a headache
* the only way I can think of to solve this is to first implement loop detection, and then loop through each cell in the lab_map, and try to make an obstacle there, and then run the guard through their whole patrol again, counting which work, along the way
* there must be a more efficient way
* I think that only spots in the initial route marked with an X (except the starting position) are places where we can place an obstacle to make the loop (since otherwise it wouldn't have hit them anyway)
* loop detection: keep a map of repr(guard), and if it repeats, we've hit a loop