this one really scratched an itch. i enjoyed figuring out the efficient way to
solve it. took me 25m in total which mightve ranked well if i started at 9.

observations to get the better solution:
1. stones are never affected by their neighbor and can be solved in isolation
2. the tree of stones created from one stone is deterministic and only changes
   with the number of blinks.
3. we don't care about the actual stone numbers at the end
4. so we can memoize subtrees stone counts and reuse for repeated stones
