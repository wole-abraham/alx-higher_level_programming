#!/usr/bin/node

const argv = process.argv.slice(2).map(Number);

for (let i = 0; i < process.argv.length; i++) {
  for (let j = 0; j < process.argv.length - 1; j++) {
    if (argv[j] < argv[j + 1]) {
      const temp = argv[j];
      argv[j] = argv[j + 1];
      argv[j + 1] = temp;
    }
  }
}

console.log(argv[1]);
