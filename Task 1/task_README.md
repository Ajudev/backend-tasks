# Algorithm Test

- I have implemented queue data structure using deque of collections module to store the order information since deque implements queue using a doubly linked list and the time and space complexity for using a queue implemented using linked list is O(1) for both enqueue and dequeue operations.

- I am also using threads to optimize the execution of orders using futures class from concurrent module which will help manage threads by implementing a thread pool. I am using threads to avoid scenarios where I/O latency does not delay unrelated parts of the application. This way I am able to process the orders to the database much faster than the original algorithm.

- The original algorithm takes 8 minutes to complete processing 1000 orders whereas the new algorithm takes 1.36 seconds to finish processing 1000 orders.

## Code Setup

- There is no need of installing any additional packages since all modules used are in built modules. Please make sure you are using Python version 3.9 or greater
