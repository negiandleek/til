declare module "react" {
  export type CustomType = string;
}

import React, { CustomType } from "react";

const a: CustomType = "a";
