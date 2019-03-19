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
