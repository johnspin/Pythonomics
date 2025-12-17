import random as rnd
import sys

def PrintRNL(left, right, data):
    print('left', left, '|', end='')
    print('right', right)
    print(' data', data)
    print()

def DoAShuffle(left, right):
    ret = []
    l = len(left)
    curr_l = 0
    r = len(right)
    curr_r = 0
    # tot = len(left) + len(right)
    # for i in range(tot):
    while curr_l < l and curr_r < r:
        if rnd.randint(0,99) < 50:
            ret.append(left[curr_l])
            curr_l += 1
        else:
            ret.append(right[curr_r])
            curr_r += 1

    if curr_r == r:
        last = left[curr_l:]
    else:
        last = right[curr_r:]

    ret.extend(last)
    return ret

def CalcSplit(datLen, splitError=4):
    return (datLen / 2) + rnd.randint(-1 * splitError, splitError)

def SplitData(list):
    split = CalcSplit(len(list))
    print()
    print('Data size', len(list), ' Split location', split)
    print()
    return (list[0: split], list[split:])

def RunRandRiffleShuffle(data,times=5):
    rnd.SystemRandom()
    left, right = SplitData(data)
    print('Iter 0')
    PrintRNL(left, right, data)

    for i in range(1, times):
        data = DoAShuffle(left, right)

        left, right = SplitData(data)
        print('Iter ', i)
        PrintRNL(left, right, data)
        left, right = SplitData(data)

        if sys.version >= (3,):
            text = input('Waiting...')  # Python 3 and up
        else:
            text = raw_input('Waiting...')  # Python 2.7 minor=13 and below

def main():
    data = range(0,20)
    RunRandRiffleShuffle(data,8)

if __name__ == "__main__":
    main()
