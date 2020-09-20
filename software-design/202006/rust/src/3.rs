trait GeoCalculator{
  fn area(&self) -> f64;
  fn length(&self) -> f64;
}

struct RightTriangle {
  base: f64,
  perdendicular: f64,
}

impl GeoCalculator for RightTriangle{
  fn area(&self) -> f64{
    (self.base * self.perdendicular) * 0.5
  }
  fn length(&self) -> f64{
    self.base + self.perdendicular + (self.base.powi(2) + self.perdendicular.powi(2)).sqrt()
  }
}

struct Rectangle {
  width: f64,
  height: f64,
}

impl GeoCalculator for Rectangle{
  fn area(&self) -> f64 {
    self.width * self.height
  }
  fn length(&self) -> f64 {
    (self.width + self.height) * 2.0
  }
}

// fn printval<T: GeoCalculator>(poly: &T){
fn printval(poly: &dyn GeoCalculator){
  println!("{}", poly.area());
  println!("{}", poly.length());
}

fn main() {
  let tri = RightTriangle {
    base: 3.0,
    perdendicular: 4.0,
  };
  printval(&tri);

  let rec = Rectangle {
    width: 3.0,
    height: 4.0,
  };
  printval(&rec);
}