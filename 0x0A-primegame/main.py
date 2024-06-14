#!/usr/bin/python3

isWinner = __import__('0-prime_game').isWinner
test = __import__('test').isWinner

print("Winner: {}".format(isWinner(5, [2, 5, 1, 4, 3])))
print("Winner: {}".format(isWinner(5, [])))
print("Winner: {}".format(isWinner(5, [1])))
print("Winner: {}".format(isWinner(5, [1,2])))
print("Winner: {}".format(isWinner(5, [2,3])))
print("#######################")
print("Winner: {}".format(test(5, [2, 5, 1, 4, 3])))
print("Winner: {}".format(test(5, [])))
print("Winner: {}".format(test(5, [1])))
print("Winner: {}".format(test(5, [1,2])))
print("Winner: {}".format(test(5, [2,3])))

