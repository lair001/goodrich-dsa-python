Function example4 can be found in exercises.py located in the vendor files for ch03.

Let us count array reads and addition as our primitive operations. We read each element once to add it to our prefix
We then add our prefix to our running total. Hence, there are $3n$ primitive operations and example4 is $O(n)$.