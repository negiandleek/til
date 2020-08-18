case class Course(id: Int)
case class Driver(name: String)
object NoDriver extends Driver("no-driver")

trait Ridable {

  def ride(driver: Driver): Unit

}

trait Runnable {

  def run(course: Course): Unit

}

class Bicycle extends Ridable with Runnable{
  private[this] var name: String = ""
  def ride(driver: Driver): Unit = {
    name = driver.name
  }

  override def run(course: Course): Unit = {
    println(s"${name} ${course.id}")
  }
}