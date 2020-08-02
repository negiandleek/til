// namespace
namespace A {
  export namespace B {
    export let c = 3;
  }
}
import d = A.B.c; // 3

const sum = d * 5; // 15

// コンパニオンオブジェクト
enum Color {
  RED = "#ff0000",
  GREEN = "#00ff00",
  BLUE = "#0000ff",
}

namespace Color {
  export function print(to: string): Color {
    return Color[to];
  }
}

Color.print("RED");
