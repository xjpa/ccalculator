#include <stdio.h>
#include <math.h>
#include <gperftools/profiler.h>

// arithmetic functions
int add(int a, int b)
{
    return a + b;
}

int subtract(int a, int b)
{
    return a - b;
}

int multiply(int a, int b)
{
    return a * b;
}

float divide(float a, float b)
{
    if (b != 0)
    {
        return a / b;
    }
    else
    {
        return -1; // error case for division by zero
    }
}

// advanced math functions
// ----------------------------
double power(double base, double exponent)
{
    return pow(base, exponent);
}

double square_root(double number)
{
    if (number < 0)
    {
        return -1; // error case for square root of negative number
    }
    return sqrt(number);
}

int factorial(int number)
{
    if (number < 0)
    {
        return -1; // error case for negative numbers
    }
    int result = 1;
    for (int i = 2; i <= number; i++)
    {
        result *= i;
    }
    return result;
}

int is_prime(int number)
{
    if (number <= 1)
    {
        return 0;
    }
    for (int i = 2; i * i <= number; i++)
    {
        if (number % i == 0)
        {
            return 0;
        }
    }
    return 1; // prime
}

__attribute__((constructor)) void start_profiling()
{
    ProfilerStart("profile.prof");
}

__attribute__((destructor)) void stop_profiling()
{
    ProfilerStop();
}