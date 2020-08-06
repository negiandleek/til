# memo
# https://www.nnn.ed.nico/courses/143/chapters/1873 - 12 

# 初級
case class Student(val name: String, val grade: Int) {}

# 中級
sealed abstract class DayOfWeek
case object Sunday extends DayOfWeek
case object Monday extends DayOfWeek
case object Tuesday extends DayOfWeek
case object Wednesday extends DayOfWeek
case object Thursday extends DayOfWeek
case object Friday extends DayOfWeek
case object Saturday extends DayOfWeek

object DayOfWeek{
  def toNum(day: DayOfWeek): Int = {
    day match{
      case Sunday => 1
      case Monday => 2
      case Tuesday => 3
      case Wednesday => 4
      case Thursday => 5
      case Friday => 6
      case Saturday => 7
    }
  }
  def nextDayOfWeek(day: DayOfWeek): DayOfWeek = {
    day match{
      case Sunday => Monday
      case Monday => Tuesday
      case Tuesday => Wednesday
      case Wednesday => Thursday
      case Thursday => Friday
      case Friday => Saturday
      case Saturday => Sunday
    }
  }
}

