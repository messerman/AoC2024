# Part 1
* this is either going to be trivial, or a huge pain - we'll find out
* initial thought: make a map of (page number) -> [dependency1, dependency2, ...], and then use that to determine if I can print a given page
* this is a good use of sets
* sets are great, but they don't keep order - had to do a lot of converting between types to get this to work
* finally had a good reason to use pylint, to try to figure out where I was getting things wrong (I need to figure out how to make that work in VSCode, automatically)
* final solution was pretty much my initial thought, but using `not dependencies.intersection(set(remaining))` as my filter (ooh, I could have used `filter()`)

# Part 2
* 