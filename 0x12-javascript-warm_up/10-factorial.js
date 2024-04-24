#!/usr/bin/node

const arg = parseInt(process.argv[2]);

function factorial(a){
    return factorial(a - 1);
}

