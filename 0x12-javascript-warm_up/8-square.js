#!/usr/bin/node

const arg = parseInt(process.argv[2]);

if (arg) {
    for (let i = 0; i < arg; i++)
    {
        let out = '';
        for (let j = 0; j < arg; j++)
        {
            out = out + 'X';
        }
        console.log(out);
    }
} else {
    console.log("Missing size");
}
