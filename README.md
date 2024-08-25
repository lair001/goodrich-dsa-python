# Solutions for *Data Structures and Algorithms in Python 1st Edition* by Goodrich, Tamassia, and Goldwasser

## Installation

1. Install pyenv
2. Install pipenv
3. Clone the repo
4. From the root of the repo, run  `pipenv sync`

## Usage

From the root of the repo, run the command `./run [scrip-id] [args]`

Example 1: `./run ch1/ex1 4` will run the script for Chapter 1 Exercise with the argument `k = 4`.

Example 2: `./run ch2/ex22 "[1,2,3]" "[4,5,6]"` will run the script for Chapter 2 Exercise 22 with the arguments
`seq1 = [1,2,3]` and `seq2 = [4,5,6]`.

Example 3: `./run ch5/ex11 "[[1,2],[3,4]]"` will run the script for Chapter 5 Exercise 11 with the matrix

$$M = \left[ {\begin{array}{cc}
1 & 2\\
3 & 4\\
\end{array} } \right]$$

When there are multiple scripts for a given exercise, the identifiers for the additional scripts will have `/2`, `/3`,
etc. appended. Although the identifier for a given script is often noted in a comment at the beginning of the script,
the identifiers are determined by the alias definition file for each chapter.

Example 4: `/aliases/ch1_def.txt` contains the following for Exercise 1:
```
ex1 using_modulo
ex1 without_modulo
```

Therefore,

`./run ch1/ex1 4 2` will run the `using_modulo` script for Chapter 1 Exercise 1 with the arguments `n = 4` and `m = 2`.

`./run ch1/ex1/2 4 2` will run the `without_modulo` script for Chapter 1 Exercise 1 with the arguments
`n = 4` and `m = 2`.

## Testing

In order to run all tests, run the command `./test` from the root of the repo.  You may also specify particular
tests to run.

Example 1: `./test unit/ch6` will run all unit tests for Chapter 6.

Example 2: `./test integration/ch1` will run all integration tests for Chapter 1.

Example 3: `./test integration/ch4/ex17` will run all integration tests for Chapter 4 Exercise 17.

`integration` may be abbreviated to `int`.

Example 4: `./test int/ch3/ex54` will run all integration tests for Chapter 3 Exercise 54.

## Troubleshooting

If you run into issues, one potential problem may be that `Pipfile.lock` is not compatible with your system. If this is
the issue, you may attempt to resolve it by running the following commands from the root of the repo:

1. `rm Pipfile.lock`
2. `pipenv lock`
3. `pipenv sync`

## Contributing

If you have a question, found an error in a solution, or want to request a solution to a particular problem, feel free
to [open an issue](https://github.com/lair001/goodrich-dsa-python/issues) or
[fork the goodrich-dsa-python repository](https://github.com/lair001/goodrich-dsa-python/fork)
and [submit a pull request](https://github.com/lair001/goodrich-dsa-python/pulls).  You may also email me (Samuel Lair)
at lair001@gmail.com.