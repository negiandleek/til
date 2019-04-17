```js
export default function() {
  console.log('animal');
}

export function cat() {
  console.log('meow!');
}
```
```js
import animals, { cat } from './animals.js';

animals(); // "animal"
cat();     // "meow"
```
