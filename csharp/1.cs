/*
 * Problem 1
 * -------------------------------------------------------------------
 * If we list all of the natural numbes below 10 that are multiples of
 * 3 or 5, we get, 3, 5, 6, and 9 . The sum of these multiples is 23 .
 *
 * Find the sum of all the multiples of 3 or 5 below 1000 .
 */

using System;

public class Problem1
{
  public static void Main()
  {
    int answer = SumOfMultiples(3, 1000) + SumOfMultiples(5, 1000)
        - SumOfMultiples(3 * 5, 1000);
    Console.WriteLine("1\t: " + answer);
  }

  public static int SumOfMultiples(int multiple, int upper)
  {
    int answer = 0;
    for (int i = 1; i < upper; i++)
    {
      if (i % multiple == 0)
      {
        answer += i;
      }
    }
    return answer;
  }
}

