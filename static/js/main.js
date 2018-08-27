console.log("Don't push the button")

document.getElementById("js-clicker").addEventListener("click", ()=> {
	fetch('http://127.0.0.1:8000/birthdays')
		.then(function(response) {
		return response.json();
	})
	.then(function(myJson) {
		console.log(JSON.stringify(myJson));
	});
		console.log("You pushed the button")
})