## Project 2 introduction

1. Demonstrate inheritance by extending the calculator
2. Demonstrate encapsulation by having the calculator have methods and a result property
3. Demonstrate abstraction by layering your code and using static methods.  Object methods should call static methods to perform the operation.
4. Check values for being valid numbers and not strings
5. Throw an exception for divide by zero 
6. Throw exception for empty list
7. Use random data for tests and be able to increase the number of calculations required i.e. be able to increase the list of numbers that the mean calculation is done on.  You can actually use built-in libraries or 3rd party libraries to check the calculations that you complete yourself.  i.e. you can use the standard deviation function from a stats library to compute the correct value for your list of random numbers and then use that to test that your own calculation is correct for that list.

## Statistic calculation required
1. Mean
2. mode
3. median
4. variance
5. standard deviation

- more information please find in this link
[click here](https://stattrek.com/statistics/formulas.aspx)


## Running program

#### build images


```shell
# go to Dockerfile dir
cd <Dockerfile_dir>
```

run docker bulid

```shell
docker build -t project2:latest
```

#### run images

```shell
docker run -it project2:latest
```

![image](https://github.com/jinhongtan/calculator3/blob/main/Project%202%20success%20run.png?raw=true)
