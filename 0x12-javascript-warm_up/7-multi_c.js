#!/usr/bin/node

const arg = parseInt(process.argv[2]);

if (arg) {
    for (let i = 0; i < arg; i++){
        console.log('C is fun');
    }
}else{
    console.log('Missing number of occurences');
}

