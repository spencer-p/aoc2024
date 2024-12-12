sub 3k rank for a 1h10m time today. that's something, guess it was hard.

my solution keeps a mapping of "coords on the perimeter and the facing
direction" to "side index". checking new spots inherit adjacent indices.
this requires processing all the indices in order.

i suspect there must be some neat divide and conquer algorithm to count the
faces. maybe I will try writing that later

I need to organize my coordinate hacking methods. I probably wasted the most
time on fiddling with coordinate math.
