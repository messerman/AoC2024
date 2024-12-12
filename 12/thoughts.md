# Part 1
* was a bit confused about the rules regarding shared fences, but since each costs separately, it was easier to do
* added two new methods to `Grid` - `connected_group()` and `groups()`.
    * `connected_group` returns the contiguous region containing only the same cell value as the starting cell
    * `groups` returns the list of all `connected_group`s in the grid
* ended up w/ a hacky solution for the last part, where I iterated over each cell in each group, and added its fence location (which I represented w/ coords 1/2 way between it and its neighbor, e.g. `(4.5, 3)` is to the fence to the East of `(4, 3)` and west of `(5, 3)`

# Part 2
* 