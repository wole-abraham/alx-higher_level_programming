#!/usr/bin/node
const arg = process.argv;
let str = parseInt(arg[2]);
if (str){
    console.log(`My number: ${str}`);
} else {
    console.log('Not a number');
}

