// アンビエント変数宣言
declare let env: {
  NODE_ENV: "development" | "production";
};

env.NODE_ENV;
// NODE_ENV: "development" | "production"

// アンビエントモジュール宣言
declare module "module-name" {
  export type CustomType = string;
}

import module from "module-name";

const a: module.CustomType = "a";
// CustomType: string
