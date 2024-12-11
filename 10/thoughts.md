# Part 1
* I generally don't like route finding problems, but this one seems straightforward
* my quick whiteboarded pseudocode solution before I had to take Sav to school today:
```
parse -> Grid
n = '0'
trailheads = grid.find(n)
for th in trailheads:
    get neighbors(str(int(n)+1))
    if n == 9:
        return success
return fail
```
* re-reading the problem statement, I'm going to have to do a bit more than I originally planned, since i can't just stop at the first 9 I find, but need to track how many I find - easy modification

# Part 2
* not too big of a shift, and one I almost did as part of part 1, anyway, hopefully it won't be too much change
* now that I think about it, this is really a DP-type problem...not sure I want to deal with doing it that way, we'll see how bad my other way is
* that turned out to be EASIER than the DFS I wrote in part 1 (I just return 1 for each time I hit 9, and sum my scores as I go back down the recursion stack), and did not require DP - it was very fast as-is
