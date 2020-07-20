// TODO:
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

interface Option<T>{}
class Some<T> implements Option<T>{
  constructor(private value: T){}
}

aask()
  .flatMap(parse)
  .flatMap(date => _.toISOString())
  .forEach((_) => console.info("Date is", _));
