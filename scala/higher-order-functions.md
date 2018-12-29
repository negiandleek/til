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

# Object
```scala
object payment {
  def show(salary:Int, sign: String): String = {
    val display = sign + salary;
    println(display);
    display;
  }
  def payEn(salaries: Seq[Int], sign: String): Seq[String] = {
    salaries.map(x => show(x, sign))
  }
  def payJa(salaries: Seq[Int], sign: String): Seq[String] =
    salaries.map(x => show(x * 100, sign))
}
val american:Seq[Int] = Seq(100,200,300);
val dollar: String = "$";
payment.payEn(american, dollar);

val japanese:Seq[Int] = Seq(100,200,300);
val yen: String = "¥";
payment.payJa(japanese, yen);
```
