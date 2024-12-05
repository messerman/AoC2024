# Part 1
* this is either going to be trivial, or a huge pain - we'll find out
* initial thought: make a map of (page number) -> [dependency1, dependency2, ...], and then use that to determine if I can print a given page
* this is a good use of sets
* sets are great, but they don't keep order - had to do a lot of converting between types to get this to work
* finally had a good reason to use pylint, to try to figure out where I was getting things wrong (I need to figure out how to make that work in VSCode, automatically)
* final solution was pretty much my initial thought, but using `not dependencies.intersection(set(remaining))` as my filter (ooh, I could have used `filter()`)
* I decided to clean up the code and use filter and map and sum - looks nicer, but a waste of time

# Part 2
* I understood what needed to be done, immediately, but got tired (I actually worked on these soon after they came out, instead of waiting until morning)
* I basically did a bubble sort-style algorithm to re-order the pipelines. Otherwise, I was basically able to re-use everything I wrote for part 1
* ugly code, but it works