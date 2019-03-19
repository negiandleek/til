|書き方|	意味 |
|---|---|
|(?=regex) |	直後にregexがある|
|(?!regex) |	直後にregexが無い|
(?<=regex) |	直前にregexがある|
(?<!regex) |	直前にregexが無い|

[こんどこそわかる(肯|否)定(先|後)読み](https://qiita.com/tohta/items/2ba7ecde5636b38ef1f6)

```md
肯定的前方読み(?=pattern)
.*(?=hoge)
`a`hogea

否定的前方読み(?!=pattern)
a(?!hoge)
ahoge`a`

肯定的戻り読み(?<=pattern)
[0-9]{3}(?<=.{6})ba
000ba`000ba`

肯定的戻り読み(?<=pattern)
[0-9]{3}(?<!.{6})ba
`000ba`000ba
```
