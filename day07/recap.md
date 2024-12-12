i nearly had it today, i could have gotten really quick

i was right to go recursive to start, but i wrote some bugs

1. binding right operations first, when it should have been left
2. not discarding floats. integer division was wrong because it coerced.
   i should have detected and failed.
3. for the concat part, i forgot to do the op in reverse (trim suffix instead of
   concat)
