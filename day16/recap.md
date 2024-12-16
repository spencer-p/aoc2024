this was rough

I need to brush up weighted graph traversal. I fumbled through the
implementation and took a long time to remember i had to use a priority queue.

then part 2 I did not think clearly. I tried a couple variations of searching
the space and reusing the costs computed from part 1.

My solution does DFS starting from the endpoint with final cost and only takes
valid steps backwards, which finds all possible paths from the end to the
beginning which must have the same (minimal) cost.

enumerating all paths from the start to end with DFS is not feasible for the
graph size given, it's pretty much brute force. I tried running this while
working and it never terminated.

conviently my puzzle inputs all end with the bot facing north? I wonder if this
was true for everyone.

I still got sub 5k, which I think is not bad.
