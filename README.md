# eecs482-Min-Tests
A script that gives you the smallest number of files that give you maximum points on the EECS 482 Autograder

## Usage
create a file called `"testcase_results.txt"` with the following format (unix newline and space separated as shown):
```
[All bugs caught]
[testcase_name_1] [list of bugs caught]
[testcase_name_2] [list of bugs caught]
...
```

An example file would look like this:
```
ABCabc
test_1.cpp ab
test_2.cpp ABabc
test_3.cc ABCc
```

Then, run `python 482AG_testcases.py` and the script will output a list of the shortest number of files that will get you all the bugs you've entered on the first line.

## When to use
The best way to use this script is to speed up the autograder response time on submits that you need fast feedback for. This script is also very useful if you quickly need to reduce the size of your test case suite to make room for new tests.

However, keep in mind that the autograder gives useful warnings about which test cases are exposing bugs in your code. A file that's been excluded from the list generated by this script may be the only one exposing certain bugs from your entire test suite, even if it doesn't catch any new instructor bugs. Keep that in mind if you're trying to get hints from the auto grader.

##Enjoy :)