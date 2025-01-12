# Part 1
* summary: It's a LAN party, and there's a bunch of computers, identified by 2-letter codes. We get a list of pairs of connections between computers as our input. We need to find all the sets of three inter-connected computers containing at least one computer with a name that starts with t.
* seems relatively straightforward for part 1, part 2 will probably be super hard
* it was incredibly straightforward, but I made several overcomplications that caused a million bugs
* the biggest unnecessary complication: trying to fully map the network, for no reason

# Part 2
* summary: actually we need to find the biggest connected network, and return its computer names sorted and comma-separated, because that's "the password"
* this seems like it shouldn't be too hard. I'm thinking sets, and a while loop or recursion
* TIL: you can type hint an arbitrary number of items in a set/list/etc, like `x: list[SomeClass, ...] = []`
* I'm making more dumb errors, but I'm having fun tracking them down, because I'm learning a lot about some deeper parts of python I don't normally touch (e.g. I'm subclassing `set()` right now)
* TODO: I should make my template file a class, instead, and have `./generate.sh` create a subclass instead of the functions it currently does
