#!/usr/bin/node

if (process.argv.length - 2  === 0){
	console.log("Missing number of occurences");
}

else {
	const string = parseInt(process.argv[2]);

	if (isNaN(string)){
		console.log("Missing number of occurences");
	}

	else{
		let t = 0;
		while (t < string){
			console.log("C is fun");
			t++;
		}
	
	}
}



