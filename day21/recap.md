this problem was really difficult.

solutions i tried:
- find the shortest sequence at each level and go up. this does not work,
  sometimes a longer sequence sooner results in a shorter sequence higher up the
  chain.
- search the state space directly (way too slow)
- construct the sequence directly (too complicated, though apparently it's
  possible?)
- try to divide and conquer (split the sequence in half, solve, cache results).
  this doesn't work because the split in half might not be stateless.

before going to bed I spent some time looking at the example sequences, and
worked out that every time a button is pushed, all of the higher-order robots
are pressing A, which returns them to their starting position.

```
<vA<AA>>^AvAA<^A>A<v<A>>^AvA^A<vA>^A<v<A>^A>AAvA^A<v<A>A>^AAAvA<^A>A
  v <<   A >>  ^ A   <   A > A  v  A   <  ^ AA > A   < v  AAA >  ^ A
         <       A       ^   A     >        ^^   A        vvv      A
                 0           2                   9                 A
```

then i slept on it.

because A is the start position (the state is reset), we can cut the sequence
by As to solve subproblems. now divide and conquer works! we also have to return
the min length (int) and not the sequence itself, because the sequences would
not fit in memory.

I also verified that some of the subsequences are repeated, which means we can
memoize results.

so the solution is roughly

```
@cache
def solve(wantseq, depth):
    if wantseq is empty: return 0
    if wantseq is 'A': return 1
    if depth is 0: return len(wantseq)
    for all sequences that generate wantseq:
        split the sequence by A
        sum(solve(subproblem+'A', depth-1))
        save the lowest sum
    return the lowest sum
```
