# The following code causes an infinite loop (a loop that never stops iterating). Why?



counter = 0

while counter < 5:
    print(counter    # The problem occurs in the loop body. We never increment
                     # counter, so counter < 5 always returns a truthy value.
