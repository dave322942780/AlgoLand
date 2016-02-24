# http://www.careercup.com/question?id=15556758
# There is an island which is represented by square matrix NxN. 
# A person on the island is standing at any given co-ordinates (x,y).
# He can move in any direction one step right, left, up, down on the island.
# If he steps outside the island, he dies.
# 
# Let island is represented as (0,0) to (N-1,N-1) (i.e NxN matrix);
# person is standing at given co-ordinates (x,y).
# He is allowed to move n steps on the island (along the matrix).
# What is the probability that he is alive after he walks n steps on the island?
# 
# Write a psuedocode &amp; then full code for function
# " float probabilityofalive(int x,int y, int n) ".

def solution(x, y, size, step):
    if step == 0 and 0 <= x < size and 0 <= y < size:
        return 1
    elif step > 0 and 0 <= x < size and 0 <= y < size:
        return (solution(x + 1, y, size, step - 1) +
                solution(x - 1, y, size, step - 1) +
                solution(x, y + 1, size, step - 1) +
                solution(x, y - 1, size, step - 1)) / 4.0
    return 0
