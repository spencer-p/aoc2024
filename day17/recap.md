wow, this one was fun. rank 1056 for part 2, pretty stoked about that.

i had to really read and understand my program to figure out how to do this. the
part 2 solution doesn't even work for the part 1 example (is there a solution
for the part 1 example?)

(well done eric to subtly call attention to the program properties by changing the
example input in the text)

key observations about my program:
1. B and C don't matter, everything is derived from A
2. the low 3 bits of A have the most importance, but the cdv instruction is
   capable of bringing some high bits into the mix
3. the loop shifts A down three bits and goes to the beginning

first i tried choosing an A value for each iteration of the loop that would get
the value needed. then I could compose all those A values by shifting up 3 bits
and adding in the next (in reverse order of course).

but then i noticed some of my values were greater than 8 (thanks to that cdv
instruction). so I refactored to build the A value as i go, shifting up and
adding in each new experimental value. this time the series of values shifted in
must be different, and the test uses the full A value to verify.

i think this is what i had in mind in the beginning, but couldn't grasp how i'd
be able to run the whole program in reverse. turns out the only part i needed to
reverse was the shift right before the jump.


part 3:

I rewrote the vm with a match statement, nice and succinct.
I also wrote my search function as a proper backtracking recursive search. My
original solution could only "backtracking" by incrementing A upwards until
previous values (bits above the 3 lowest) got tampered with, which could be slow
for more complex cases.

I think this solution could still be slow for complex cases since there are
possibly 8^n solutions. The input is well crafted to have low branchiness.
