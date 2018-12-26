# Basic
```scala
val ary = Seq(1000,2000,3000);
val salaryAtUsa = ary.map(x => "$" + x);
val salaryAtJapn = ary.map("¥" + _ * 100);
println(salaryAtUsa, salaryAtJapn)
```

# Method
```scala
class Payment(salary: Seq[Int], locale: String){
  def getNotaion(locale: String):String = {
    if(locale == "en")
      return "$"
    else(locale == "ja")
      return "¥"
  };
  private def calcSalary(num: Int, notation: String): String = notation + num
  def calcSalaries(): Seq[String] = 
    salary.map(x => calcSalary(x, getNotaion(locale)))
}

val payments = new Payment(Seq(100,200,300), "en")
val results = payments.calcSalaries();
println(results)
```
