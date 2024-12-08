# Part 1
* The description of this problem was the most confusing one of the year so far
* I sketched out a rough algorithm on the board - basically loop through all pairs of nodes, and then:
    * remove non-matching pairs
    * remove pairs that are not in a straight line
    * calculate distance between nodes of the pair
    * antinodes will be on either side of the pair at (distance) away from closest node to that side
* wait...by definition, any two points are always in a straight line - does that make this easier or harder?
* once I worked through a bunch of dumb errors, this worked out easily

# Part 2
* again, a confusing description
* easy enough - actually had to get rid of the logic for the whole twice the distance stuff
* find all in-bounds position on the line between each two nodes of the same frequency