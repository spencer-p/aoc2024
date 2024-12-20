todo list for later

1. download input script needs to parse away html formatting
2. backprop any util.py changes

thoughts at midnight

- big breakthrough I missed was that *the spot you start cheating at* is part of
  the node for path traversal
- I will have to sleep on this to see if bfs really would have done better
- my solution was slow. but it did work. a few minutes is better than heat death
  of universe time.

next day thoughts

- a more careful reading is "how many ways are there to jump forward on the
  single track" (such that you save 100ns). that phrasing makes it more explicit
  that your search space is limited (and also that the walls are irrelevant).
- saw folks on reddit simply iterating over the combinations of points. i wrote
  a part 3 based on that, and found restricting with my cheat2 or cheat20 funcs
  makes it even faster.
- but this is conceptually very similar to my DFS-in-name-only solution, so why
  does that run so slow?
- turns out because it returns a list of scores (lots of allocs, stack space)
  instead of the count of scores that save 100ns. changing the return type made
  it match the runtime of my part 3 solution. neat!
