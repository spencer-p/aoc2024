nice bait and switch, i feel i should have seen part 2 coming but I have been
excited for a dynamic programming problem.

i did the derivation for the button presses by hand, and I had to do it twice
to get it right.

weirdly they are equivalent, but the second was a simpler form. I suspect there
were floating point errors in my first attempt.

first sub-2k for both parts, with a 43m time. not bad!

after sleeping on it:

I reached for dynamic programming based on the strong hint in part 1 that we had
to minimize cost. Part 1 conveniently doesn't mention that there is only one
possible cost to reach the prize (although there could be a large number of
paths, since you can rearrange the button presses as much as you like).

But with two equations and two variables we have to have only one possible cost,
with the exception of the case where `(Ay*Bx - Ax*By) = 0`. Which never occurs
in the problem input.

I think that case is when `(Ax, Ay)` is a multiple of `(Bx, By)`, i.e. the two
buttons move in the exact same direction.

Then there's a couple cases, I would just compute the cost of each and return
the most effective:
0. The prize isn't on the vector; it's unreachable.
1. All A alone or all B can reach the target.
2. All A just before overshooting, then use B to reach the target.
3. Same as 2 but swap A and B.
