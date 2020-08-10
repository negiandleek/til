// test.d.ts
export declare namespace BarBaz {
  export type UserID = string & { readonly brand: unique symbol };
  export function getUserId(): UserID;
}
export = BarBaz;
export as namespace BarBaz;

// test.js
export function getUserId() {
  return "aGVsbG8gd29ybGQ=";
}

// test2.d.ts
export function getUserId(): number;

// test2.js
export function getUserId() {
  return 0;
}

// TODO
// test3.d.ts
declare type UserID = string & { readonly brand: unique symbol };
declare type GetUserId = () => UserID;

// test3.ts
const userId = "aaa" as UserID;
export const getUserId: GetUserId = function () {
  return userId;
};

// index.ts
import { getUserId } from "./test";
import { getUserId as getUserId2 } from "./test2";
console.log(getUserId()); // BarBaz.UserID
console.log(getUserId2()); // number
