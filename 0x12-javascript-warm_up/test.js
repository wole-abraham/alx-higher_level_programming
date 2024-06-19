#!/usr/bin/node

function print (){
	console.log("hey")

}

function mul(a, b){
	for (let i = 0; i < a; i++){
		b();
	}
}

mul(6, print);



