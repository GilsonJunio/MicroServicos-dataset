const req = fetch('https://1agu4qhsa5.execute-api.us-east-2.amazonaws.com/default/primeirafuncao',{
	headers:{
		'Access-Control-Allow-Origin':"*"
	}
})

console.log(req)