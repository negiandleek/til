# Variances
[VARIANCES](https://docs.scala-lang.org/tour/variances.html)

```scala
class Vegetable;
class Carrot extends Vegetable;
class Ginseng extends Carrot;

class InvarianceTest[A];
class CovarianceTest[+A];
class ContravarianceTest[-A];

var a: InvarianceTest[Vegetable] = new InvarianceTest[Vegetable];
// b = new InvarianceTest[Carrot];  //error
var b: CovarianceTest[Carrot] = new CovarianceTest[Ginseng];
b = new CovarianceTest[Carrot];
// b = new ConvarianceTest[Vegetable]; //error

var c: ContravarianceTest[Carrot] = new ContravarianceTest[Vegetable];
// c = new ContravarianceTest[Ginseng]; //error
```

# Upper Type & Lower Type Bounds
[Upper Type Bounds](https://docs.scala-lang.org/tour/upper-type-bounds.html)
[Lower Type Bounds](https://docs.scala-lang.org/tour/lower-type-bounds.html)
```scala
class Animal;
class Dog extends Animal;
class Golden extends Dog;

class UpperBoundTest[U<:Dog];
class LowerBoundTest[L>:Dog];

var dog = new UpperBoundTest[Golden];
// var dog2 = new UpperBoundTest[Animal]; error

var animal = new LowerBoundTest[Animal];
// var anima2 = new LowerBoundTest[Golden]; error
```
