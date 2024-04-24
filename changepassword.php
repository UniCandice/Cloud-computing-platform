<html>
<title>Change your password</title>
<head>
<link href="css/changepass.css" rel="stylesheet" rev="stylesheet" type="text/css" media="all" />
</head>
<body style="background-color:green">
<br />
<br />
<br />
<br />
<br />
<form action="./dochangepasswd.php" method="post">
	<div class="cform" >
		<div class="t"><h3>Change your password</h3></div>
		<div class="pass">
			input  your new password:
			<input type="password" name="pass1" onmouseover="this.style.borderColor='black';this.style.backgroundColor='#FFC0CB'"
style="width: 206; height: 21" 
onmouseout="this.style.borderColor='black';this.style.backgroundColor='#ffffff'" style="border-width:1px;border-color=black" />
		</div>
			<br />
		<div class="pass">
			input  your new password again:
			<input type="password" name="pass2" onmouseover="this.style.borderColor='black';this.style.backgroundColor='#FFC0CB'"
style="width: 206; height: 21" 
onmouseout="this.style.borderColor='black';this.style.backgroundColor='#ffffff'" style="border-width:1px;border-color=black" />
		</div>
		<div >
			<br />
			<input class="button" type="submit" value="Submit" />
		</div>
	</div>
</form>
</body>
</html>
