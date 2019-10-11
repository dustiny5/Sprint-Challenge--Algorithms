#### Please add your answers to the ***Analysis of  Algorithms*** exercises here.

## Exercise I

a) O(1) time complexity. Mutiplying n doesn't increase time complexity. This just compares two numbers


b) O(n^2) time complexity. We have two loops meaning we recieve an input which recieves another input(n*n)


c) O(n) time complexity. Similar to having one loop. Depending on the size of n the output is n

## Exercise II

egg_breaks = 0
egg_intact = 0

while egg_breaks == 0:
    for floor in floors:
        if floor >= f:
            egg_breaks += 1
        else:
            egg_intact += 1
print(egg_intact)

Time complexity of O(n^2) because I have two loops. The lowest possible of broken eggs is 0 and when 1 egg breaks then we break out of the loop getting the minimum eggs broken

