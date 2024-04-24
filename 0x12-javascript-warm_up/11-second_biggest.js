#!/usr/bin/node
const argl = process.argv.length;
const arg = process.argv;
if (argl - 2 === 0 || argl - 2 === 1) {
  console.log(0);
} else {
  for (let n = 2; n < argl; n++) {
    for (let j = 2; j < argl - 1; j++) {
      if (parseInt(arg[j]) < parseInt(arg[j + 1])) {
        const temp = arg[j];
        arg[j] = arg[j + 1];
        arg[j + 1] = temp;
      }
    }
  }
  console.log(arg[3]);
}
