part 1:

- I learned how to use python dataclasses. i was bit by them not being hashable.
  in this program i could make them eq and frozen, maybe I'll do that next time
  if i expand the vector class.
- i took too long because I didn't use width and height vars to start, and was
  running the test input on the full grid size. and I wasn't printing the map as
  early as I should have when I was running into problems
- i wish i had the mul method in my back pocket, another improvement.

part 2:

- wow was this making me start to feel lost
- i tried a couple heuristics to pause the simulation so I could look at it
- what worked was hoping that there would be a line on y=44, since i saw that
  almost form a few times. turned out to get me there quickly, but I spent a lot
  of time prior hitting enter on worse heuristics (mainly expecting the tree to
  be symmetrical down the middle of the map, which it wasn't)
- i had to rename my input method (for reading input.txt), and I'll probably
  keep that rename since I never edit that line anyway

other solutions:

- apparently the first frame where the robots are all in unique positions is the
  tree frame. this seems like a lucky hunch for those that tried it
- the danger score from part 1 is minimized when the tree forms. in my input,
  the tree is almost entirely in the 4th quadrant. this seems more like it was
  "intended" since it builds on part 1 directly.
