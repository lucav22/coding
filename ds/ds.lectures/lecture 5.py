'''

version II the same function can be ran except the range will be (1,num/2 +1) so it now stops at the midpoint
and takes the midpoint as well

version III takes the square root of the number as a potential factor

proof by contradiction shows that num > num and since that is a contradiction,
in each complementary pair at least is less than or equal to square root of num

the implementation of is_prime will change by the range again being sqrt(num)

the time of each function can be read as T(n) since runtime analysis is based on size of the input

runtime analysis depends on the amount of ram that is being used

however, any primitive operation such as +,-,x,=,sqrt is constant time

instead of taking the number of primitive operation, we take the growth of the number of operation
this is asymptotic analysis instead of runtime analysis

after finding the runtime analysis, you can ignore the number values associated to it and instead look at the
constant that is occurring due to the input

talking more about asymptotic analysis next time


'''