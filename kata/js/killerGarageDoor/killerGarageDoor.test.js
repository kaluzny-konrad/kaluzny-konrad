const Test = require('@codewars/test-compat');
const door = require('./killerGarageDoor');

describe("Normal operation", function() {
  it ("should open completely and stay open", function() {
    Test.assertEquals(door('P....'+'.'.repeat(10)),'12345'+'5'.repeat(10));
  });
  
  it ("should open completely, then stay open, then close", function() {
    Test.assertEquals(door('P......P......'),
                           '12345554321000');
  });
});

describe("Pause", function() {
  it ("should start opening and pause on second buttonpress", function() {
    Test.assertEquals(door('P.P..'),
                           '12222');
  });
  it ("should resume opening on third buttonpress", function() {
    Test.assertEquals(door('P.P.P....'),
                           '122234555');
  });
});

describe("Obstacle", function() {
  it ("should reverse while opening", function() {
    Test.assertEquals(door('P.O....'),
                           '1210000');
  });
});

describe("Obstacle + Pause", function() {
  it ("should reverse while opening (and allow pause)", function() {
    Test.assertEquals(door('P..OP..P..'),
                           '1232222100');
  });
});

describe("Example", function() {
  it ("should start opening and reverse when obstacle", function() {
    Test.assertEquals(door('..P...O.....'),
                           '001234321000');
  });
});
