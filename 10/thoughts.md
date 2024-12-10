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
* 