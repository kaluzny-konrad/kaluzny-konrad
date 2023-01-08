using System;

namespace KataCsharp;

public class Hamming
{
    public static long hamming(int n)
    {
        var hamming = new long[n];
        hamming[0] = 1;

        long x2 = 2, x3 = 3, x5 = 5;
        int i = 0, j = 0, k = 0;
        for (int index = 1; index < n; index++)
        {
            hamming[index] = Math.Min(x2, Math.Min(x3, x5));
            if (hamming[index] == x2) x2 = 2 * hamming[++i];
            if (hamming[index] == x3) x3 = 3 * hamming[++j];
            if (hamming[index] == x5) x5 = 5 * hamming[++k];
        }
        return hamming[n - 1];
    }
}