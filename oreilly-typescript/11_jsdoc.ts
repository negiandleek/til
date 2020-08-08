// one.js
/**
 * @param word {string} 変換する入力文字列
 * @returns {string} パスカルケースの文字列
 */
export function toPascalCase(word) {
  return word.replace(
    /w+/g,
    (a, ...b) => a.toUpperCase() + b.join("").toLowerCase()
  );
}

// two.ts
import {toPascalCase} from './one'
// (alias) function toPascalCase(word: string): string
// import toPascalCase
