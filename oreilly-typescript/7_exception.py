class InvalidDateFormatError extends RangeError {}
class DateIsInTheFutureError extends RangeError {}

function ask() {
  return prompt("When is your birthday?");
}

function parse(
  birthday: string
): Date | InvalidDateFormatError | DateIsInTheFutureError {
  let date = new Date(birthday);
  if (!isValid(date)) {
    return new InvalidDateFormatError("Enter a date in the form YYYY/MM/DD");
  }
  if (date.getTime() > Date.now()) {
    return new DateIsInTheFutureError("Are you a timelord?");
  }
  return date;
}

// 与えられた日付が有効かどうかチェックします
function isValid(date: Date) {
  return (
    Object.prototype.toString.call(date) === "[object Date]" &&
    !Number.isNaN(date.getTime())
  );
}

let result = parse("asdf");
if (result instanceof Error) {
  console.error(result.message);
} else {
  console.info("Date is", result.toISOString());
}

function aask() {
  let result = prompt("When is your birthday?");
  if (result === null) {
    return [];
  }
  return [result];
}

function pparse(birthday: string): Date[] {
  let date = new Date(birthday);
  if (!isValid(date)) {
    return [];
  }
  return [date];
}

interface Option<T> {
  flatMap<U>(f: (value: T) => None): None;
  flatMap<U>(f: (value: T) => Option<U>): Option<U>;
  getOrElse(value: T): T;
}

function option<T>(value: null | undefined): None;
function option<T>(value: T): Some<T>;
function option<T>(value: T): Option<T> {
  if (value == null) {
    return new None();
  }
  return new Some(value);
}

class Some<T> implements Option<T> {
  constructor(private value: T) {}
  flatMap<U>(f: (value: T) => None): None;
  flatMap<U>(f: (value: T) => Some<U>): Some<U>;
  flatMap<U>(f: (value: T) => Option<U>): Option<U> {
    return f(this.value);
  }
  getOrElse(): T {
    return this.value;
  }
}
class None implements Option<never> {
  flatMap(): None {
    return this;
  }
  getOrElse<U>(value: U): U {
    return value;
  }
}

let result2 = option(6) // Some<number>
.flatMap(n => option(n * 3)) // Some<number>
.flatMap(n => new None) // None
  .getOrElse(7) // 7

aask()
  .flatMap(new Some(parse))
  .flatMap(date => new Some(date.toISOString())) // Option<string>
  .flatMap(date => new Some('Date is ' + date)) // Option<string>
  .getOrElse('Error parsing date for some reason') // string
