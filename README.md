<h6>Requirements</h6>
pip install djangorestframework<br/>
pip install pygments  <br/>
pip install requests <br/>

manage.py syncdb

manage.py runserver

http://127.0.0.1:8000/

Using firebug

For post data to server<br/>
<h6>jQuery.post('/emp/',JSON.stringify({name:'n',role:'sse',exp:2}),function(){console.log(arguments)})</h6>

For get data from server<br/>
<h6>jQuery.get('/emp/',function(){console.log(arguments)})</h6>

For upload file<br/>
<h6>python employee/test.py [emp_id] [file path]</h6>
<div>file will store @ <b>tutorial/media/img/emp_thum/</b></div>