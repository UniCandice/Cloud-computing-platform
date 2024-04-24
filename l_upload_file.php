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

if(isset($_POST[upsubmit])){
   $randtime=mt_rand(0,10000000);

   $x1=$_POST[uploaduser];
   $x2=$_POST[up_number];
   $x3=$_POST[casename];
   

$upload_path=cfd_prefix."/uploadfiles/".$_SESSION['username']."/".$x3."_".$randtime;
   if (is_dir($upload_path)){
       echo "Sorry !".$upload_path." is exists.";}
   else{
       mkdir($upload_path);
   }
   
   $con=mysql_connect(my_host,my_user,my_password);
   if (!$con){
       die('Counld not connect: '.mysql_error());
   }
   mysql_select_db(my_db1,$con);

   $cp_table=db1_table;
   date_default_timezone_set('PRC');
   $y=date("Y-m-d h:i:s");

   //$solvername=$_FILES["usrfile"]["name"][0];
	//we get solvername from jar 
require_once("/data2/Cloud/java/Java.inc");
$test = new Java("lly.FileLLY");  
$solvername=$test->showdialog(cfd_prefix,"uploadfiles",$_SESSION['username'],$x3,$randtime);

echo "save data to database"."<br />";
   $r1=mysql_query("select * from ".$cp_table." where Type='Upload' and Random=".$randtime);
   $q1=mysql_fetch_array($r1);
   if($q1){
      $randtime=mt_rand(10000000,20000000);
      /*mysql_query("delete from ".$cp_table." where Type='Upload' and Random=".$randtime);*/
   }
   mysql_query("insert into ".$cp_table." (Type,User_name,Solver,Random,Amount,Case_name,Time) 
             values ('Upload','$x1','$solvername','$randtime','$x2','$x3','$y')");
   mysql_close($con);
   
   echo "save file to: ".$upload_path.'<br/>';
   echo "user: ".$_POST[uploaduser].'<br/>';
}
?>


</body>
</html>
