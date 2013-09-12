http://127.0.0.1:8000/

For post data to server
jQuery.post('/emp/',JSON.stringify({name:'n',role:'sse',exp:2}),function(){console.log(arguments)})

for get data from server
jQuery.get('/emp/',function(){console.log(arguments)})

