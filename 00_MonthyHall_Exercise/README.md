# Monthy Hall Exercise
The main idea of this exercise was to simulate the Monthly Hall problem and find the solution programatically

## The solution
On this repo you will find a Python script to simulate the Monthy Hall program.
The simulation was imported [from a post on the Towards Data Science Medium](https://medium.com/swlh/simulate-the-monty-hall-problem-using-python-7b76b943640e) with some minor changes.
It was examined an executed to ensure that the results provided were correct.

## To run it
```bash
docker build -t monthy-hall .
docker run --tty --interactive monthy-hall
```