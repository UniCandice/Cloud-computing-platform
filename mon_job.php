<?php
session_start();
?>
<!DOCTYPE HTML>
<html>
<head>
  <title><?php echo "CFD Cloud Management Center";?></title>
  <link rel="stylesheet" href="menu.css">
  <link rel="stylesheet" href="table.css">
  <script type="text/javascript" src="menu.js"></script>
</head>
<body>
<h5 align="right">
<?php echo "UserName:&nbsp;&nbsp;".$_SESSION['username'];?>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="./changepassword.php">Password</a>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
<a href="./index.php">LoginOut</a>
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;
</h5>
<h1 align="center">CFD Cloud Management Center</h1>
<br/>
<?php print include("menu_main.php"); ?>
<br/>
<br/>
<br/>
<br/>
<br/>
<br/>
<hr/>
<br/>

<?php
require_once("common.php");

$cmd="cd ".PYTHON_PATH.";python monitoring.py -j";
exec($cmd);
$file = fopen(cfd_prefix.'/'.'mon_job.txt', "r") or exit("Unable to open file!");
//Output a line of the file until the end is reached
while(!feof($file))
  {
  echo fgets($file). "<br />";
  }
fclose($file);
?>
</body>
</html>
