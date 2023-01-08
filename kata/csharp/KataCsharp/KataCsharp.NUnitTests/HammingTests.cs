using System;
using NUnit.Framework;

namespace KataCsharp.NUnitTests;

[TestFixture]
public class HammingTests
{

    [Test]
    [TestCase(1, 1)]
    [TestCase(2, 2)]
    [TestCase(3, 3)]
    [TestCase(4, 4)]
    [TestCase(5, 5)]
    [TestCase(6, 6)]
    [TestCase(7, 8)]
    [TestCase(8, 9)]
    [TestCase(9, 10)]
    [TestCase(10, 12)]
    [TestCase(11, 15)]
    [TestCase(12, 16)]
    [TestCase(13, 18)]
    [TestCase(14, 20)]
    [TestCase(15, 24)]
    [TestCase(16, 25)]
    [TestCase(17, 27)]
    [TestCase(18, 30)]
    [TestCase(19, 32)]
    public void Test1(int input, int expected)
    {
        var output = Hamming.hamming(input);
        Assert.That(output, Is.EqualTo(expected),
            $"hamming({input}) should be {expected}");
    }
}