# Queues

## Introduction

## What is a Queue?
To help identify exactly what a queue is, lets use some real world examples.

**Example 1:**

If you have ever worked fast food, you know that the older food has to be used before the newest food. This is called FIFO (First In, First Out). 

**Example 2:**

I would think that it's fair to assume that every person on the planet has been to some sort of a grocery store or even a market. What happens when you're ready to purchase your groceries? You go to the Cashier to pay for everything you're wanting to buy. What if there's people already there? You wouldn't just push everyone aside and get to the front, right? You may feel like doing that at times, but you wouldn't actually do it, I would hope. No! Instead you would wait in line until it's your turn to pay.

Both of these examples are in reality, a queue. Something or someone has to start it, and it can only be removed from the front of the queue. There are some times where you could remove from the back, but those are more rare.

In either case, whether removing from the front or the back of the queue, this is called a dequeue (de-queue), simply meaning that something is being removed. There is a similar aspect called enqueue (en-queue), where something is being added to the queue, which is always done to the end of the queue.

Now with all of that out of the way, let's look at some code! We are programmers, after all, aren't we?

## Programming Examples

Here's an example of a enqueue operation:
```python
    my_queue.append(value)
```
Since that this is simply adding or appending something to the end of the queue, which is a Python list, this is ***O(1) performance***, which you may recall is the quickest in performance available!

Here's 2 dequeue operations:
```python
    # Method 1
    value = my_queue[0]
    del my_queue[0] # del is deleting the specified index

    # Method 2
    value = my_queue.pop(0) #.pop(value) is also removing at the specified index 
```
First thing to note here is that both of these methods are doing the same thing, and both are ***O(n) performance***. The reason why these are O(n), is because the program first has to find, then remove the index given. It's a 2 step process. The first method takes an additional step, but that's ok. I will point out that the second method is more widely used. However, in your code, you are free to choose whichever method you prefer.

## Problem to Solve
**Instructions:**

In this problem, you are given a queue of customers to pay for their groceries. You have to adjust or write the code for the enqueue and dequeue functions.

Download the following file: [queue-problem.py](queue-problem.py), then go to the functions that need editiing, and write in the code to get the program to work as expected.

When finished and the program works as expected, or if you get stuck and need some help, feel free to look at the Sample Solution.

## Sample Solution
Here is just one possible solution to this problem and should not be used as a standard solution.

Download the following to view the sample solution: [queue-solution.py](queue-solution.py)