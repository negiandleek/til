# Basic
```ts
/* interface */
enum Sex{ man, woman };
interface User {
	name: string,
	age: number,
	sex: Sex,
	country?: string 
};

function getUser(user: User): {name: string, country: string}{
	let obj = {...user, country: ""};
	if(!user.country){
		obj.country = "English"
	}

	return {
		name: obj.name,
		country: obj.country
	}
}

const user = {
	name: "anly",
	age: 20,
	sex: Sex.woman,
};

const r = getUser(user);
```
# Read only
```ts
interface Student{
	readonly name: string,
	readonly id: number
}

const rstudent: Student = {name: "hoge", id: 0};
const student: {name: string, id: number} = {name: "fuga", id: 1};
const overrided = student as any;
overrided.name = "a";

const teacher: [string, number] = ["bar", 0];
const rteacher: Readonly<[string, number]> = teacher;
```
# Function
```ts
interface CombineUser{
	(name: string, age: number): string
}
const combineUser: CombineUser = function(name, age) {
	return `${name} is ${age} years`;
};

const r = combineUser("hoge", 23);
```

# Indexable
```ts
interface StringArray{
	[index: number]: string
}
const stringArray: StringArray = ["0","1","2"];

interface StringDictionary{
	[index: string]: string,
	name: string,
	// id: number
}
const stringDictionary: StringDictionary = {
	name: "hoge"
}
```
# Constructor
```ts
interface AnimalConstructor{
	new (type: string): AnimalInterface
}

interface AnimalInterface{
	walk(): number
}

class Homo implements AnimalInterface{
	type: string;
	constructor(type: string){
		this.type = type;
	}
	walk(){
		return 4
	}
}

function createHomo(Ctor: AnimalConstructor, type:string): AnimalInterface{
	return new Ctor(type); 
}

const r = createHomo(Homo, "monky").walk();
```
# Extends
```ts

interface Vehicle{
	tire: number
};

interface Car extends Vehicle{
	brand: string
}

const car = <Car>{};
car.brand = "BMW";
car.tire = 4;

interface Bike{
	(gasoline: number): void;
	tier: number;
	move(): void;
}

function LargeMotorcycle(): Bike{
	const bike = <Bike>function (charge: number){};
	bike.tier = 4;
	bike.move = ()=>{};
	return bike;
}
```
