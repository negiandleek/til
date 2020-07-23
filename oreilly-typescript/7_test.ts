TODO: 
type UserID = {
  id: string
  name: string
}

class NullError extends Error{}
class Base64Error extends Error{}

type CustomError = NullError | Base64Error

function getId(): UserID | null{
  const bit = Math.round(Math.random());
  return [{id: "dGVzdA==", name: "test"}, null][bit]
}

class API {
  getLoggedInUserID(): UserID | NullError{
    const id = getId()
    if(id == null){
      return new NullError("null")
    }
    return id
  };
  getUserName(userID: UserID): string | Base64Error{
    const name = userID.name
    try{
      return window.atob(name)
    }catch(e){
      return new Base64Error("decoded error")
    }
  };
}

interface Option<T>{}
class Some<T> implements Option<T>{
  constructor(value: T){}
}
class None implements Option<never>{}

function option<T>(value: null | undefined): None
function option<T>(value: T): Some<T>
function option<T>(value: T): Option<T>{
  if (value instanceof NullError || value instanceof Base64Error){
    console.error(value)
    return new None()
  }
  if(value == undefined || value == null){
      return new None()
  }
  return new Some(value)
}


function main(){
  const api = new API()
  const userId = option(api.getLoggedInUserID())
    if (typeof userId UserID) {
        const name = option(api.getUserName(userId))
    }
  console.log(name)
}
main()
