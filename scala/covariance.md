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
