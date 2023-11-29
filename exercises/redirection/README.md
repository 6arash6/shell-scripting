# Description

You've got a copy of the yellow-pages (it's like google for old people).
You need to write a couple of scripts that extract some data from the yellow
pages.


The tast is to create 4 scripts:

```
num-doctors.sh
#
# this script should find the number of doctors in the yellow pages and print
# the answer to stdout

num-dr-smith.sh
#
# this script should find the number of dr smiths in the yellow pages and print
# the answer to stdout


first-engineer.sh
#
# this script should find the record for the first engineer and print it to
# stdout

last-5-records.sh
#
# this script should find the last five records in yellow pages and print to
# stdout
```


## Test runner

It's a good idea to use the test runner for testing your scripts.
To see if your scripts pass the tests, run the `./test-redirection.sh" script.

Each test contains a description that will let you know on which script the test
is based:

```bash
cat tests/1.desc
this should test if the script num-doctors.sh outputs correct number

cat tests/2.desc
this should check the output of num-dr-smith.sh

cat tests/3.desc
this should check the output of first-engineer.sh

cat tests/4.desc
this should check the output of last-5-records.sh
```

