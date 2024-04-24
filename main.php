<!DOCTYPE HTML>
<html>
<head>
  <title><?php echo "CFD Cloud Management Center";?></title>
  <link rel="stylesheet" href="menu.css">
  <link rel="stylesheet" href="table.css">
  <script type="text/javascript" src="menu.js"></script>
</head>
<body>
<h1 align="center">CFD Cloud Management Center</h1>
<br/>
<?php print include("menu_main.php");?>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<hr/>
<br/>
<h3>Welcome to CFD World.</h3>
<?php
date_default_timezone_set('PRC');
$y=date("Y-m-d h:i:s");
echo 'The time is '.$y.'<br/>';
?>
</body>
</html>
