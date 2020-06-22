```css
:root {
   --color: pink; 
}

.bar{
  --color: lightblue;
  background-color: var(--color); /* blue */
}

.hoge{
  position: absolute;
  --i: 20;
  z-index: var(--i);
  --i: calc(var(--i) + 1);
  z-index: var(--i);
  background-color: var(--color); /* red */
  /* z-index: 20; */
 }
 
 .fuga{
   position: absolute;
   z-index: 10;
   background-color: lightgreen;
 }
```

```html
<div class="bar">
   bar
</div>
<div class="container">
  <div class="fuga">
    fuga
  </div>
  <div class="hoge">
    hogehogehoge
  </div>
</div>
```
![Imgur](https://i.imgur.com/MusQbMP.png)
