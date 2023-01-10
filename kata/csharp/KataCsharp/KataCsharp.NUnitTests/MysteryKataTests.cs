using NUnit.Framework;
using System;
using System.Collections.Generic;

namespace KataCsharp.NUnitTests;

[TestFixture]
public class MysteryKataTests
{
    [Test]
    public void Is_It_Sane()
    {
        var sanity = new Dictionary<string, string> { { "sanity", "hello" } };
        Assert.AreEqual(MysteryKata.Mystery(), sanity, "Mystery has not returned to sanity.");
    }
}
