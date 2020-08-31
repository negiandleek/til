import money.Dollar

class MoneyTest{
  @Test
  def testMultiplication(): Unit ={
    val five = new Dollar(5)
    val product = five.times(2)
    assertEquals(10, product.amount)
    product = five.times(3)
    assertEquals(15, product.amount)
  }
}