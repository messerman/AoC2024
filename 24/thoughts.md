# Part 1
* this seems like a good "just follow the directions" one, so I'm starting with that approach
* ah, we don't necessarily know all the wire values before starting, so we need to be careful about when to execute each instruction
    * might be worth working backwards from the zs, and doing a "what do I need to get this" approach
* I just kept looping over the list of instructions and executing + removing any that I had enough information to execute

# Part 2
* yeesh
* The obvious (and wrong) approach to solve this would be to find every possible combination of 8 wires that could be swapped, and test each case individually.
    * That's > 1 million pairs to check for sample1.txt, and > 2 trillion pairs in the real input.
* off the top of my head, I can't think of a more clever way to do it, though....