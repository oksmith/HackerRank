"""
Problem 'New Year's Chaos'
"""

def minimumBribes(N, array):
    """
    Print minimum amount of bribes to get to this position.
    Note: ignore all possibilities where people bribe each others
       and switch to their original positions. We look for minimum
       number only.
    """

    # positions_dict = {
    #     i + 1: array.index(i + 1) + 1 for i in range(N)
    # }

    bribe_count = 0
    for keypos, key in enumerate(array):
        keypos += 1  # for interpretability
        if key - keypos > 2:
            print('Too chaotic')
            return
        else:
            # count number of 'places' they have leapfrogged
            for x in range(1, key):
                if array.index(x)+1 > keypos:
                    print('{} has beaten {} in the queue'.format(key, x))
                    bribe_count += 1

    print(bribe_count)



t = int(input())
for _ in range(t):
    N = int(input())
    array = [int(x) for x in input().split(' ')]
    minimumBribes(N, array)