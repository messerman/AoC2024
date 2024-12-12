# Part 1
* brute force seems like an easy way to do this - and we'll worry about efficiency afterwards
* no need for efficiency in part 1

# Part 2
* let's see how long it takes to go 3 times bigger
* uh-oh - even the sample is taking a long time
* ok, time to start caching things
    * that didn't help - at least not the way I did the caching
* looking at the profiler, I see several built-in methods taking ages (due to how often they're called)
    * I tried optimizing a few of those out (operating on one term at a time, operating only on ints (instead of str conversions), the other way w/ operating only on strs, and using `list.append()` instead of `list.insert()` (this one actually helped somewhat))
    * I think I need to combine caching with some of those improvements
* caching idea: dict w/ `tuple[value: int, depth: int]` to `number_of_stones: int`
* A few things I realized:
    1. the ordering of the stones does not matter - so I didn't need to do a `list.insert()`, which is slow
    2. my original caching solution was to cache the initial value and its result (e.g. `{0:1, 1:2024, 2024:[20,24]}`, etc, which really did not help at all - instead I had to use my cache to map the stones value and its "depth" to the number of stones that stone would produce after `depth==maxdepth`, e.g. (for a stone with value 0 and `maxdepth=4`: `{(2, 4): 1, (0, 4): 1, (20, 3): 2, (4, 4): 1, (24, 3): 2, (2024, 2): 4, (1, 1): 4, (0, 0): 4}`
    3. (I knew this, but always forget) recursion is not always the bottleneck (I was actively avoiding recursion calls, even though I knew it'd be easier to write the code that way, so I could try to flatten the recursion stack)
* final solution took it from "this will never finish" to 0.02s (CPU time, it was 0.2s user-time)
