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

if(isset($_POST[commit])){
   $randtime=mt_rand(0,10000000);
   echo $randtime.'<br/>';

   $con=mysql_connect(my_host,my_user,my_password);
   if (!$con){
       die('Counld not connect: '.mysql_error());
   }
   mysql_select_db(my_db1,$con);

   $cp_table=db1_table;
   date_default_timezone_set('PRC');
   $y=date("Y-m-d h:i:s");
   $x1=$_POST[testuser];
   $x2=$_POST[solver];

   $r1=mysql_query("select * from ".$cp_table." where Type='Test' and Random=".$randtime);
   $q1=mysql_fetch_array($r1);
   if($q1){
      $randtime=mt_rand(10000000,20000000);
      /*mysql_query("delete from ".$cp_table." where Type='Test' and Random=".$randtime);*/
   }
   mysql_query("insert into ".$cp_table." (Type,User_name,Solver,Random,Time) 
             values ('Test','$x1','$x2','$randtime','$y')");

   $tcase_table='tcase'.$randtime;
   mysql_query('drop table if exists '.$tcase_table,$con);
   $sql1="create table ".$tcase_table."
   (
   Case_id  int not null auto_increment,
   primary key(Case_id),
   Case_name   varchar(50)
   )";
   
   mysql_query($sql1,$con);
   echo "User:";
   echo $_POST[testuser]."<br/>";
   echo "Solver:";
   echo $_POST[solver]."<br/>";
   echo "Case:"."<br/>";
   foreach($_POST["case"] as $x){
          echo $x."<br/>";
          mysql_query("insert into ".$tcase_table." (Case_name) values ('$x')");
   }
   mysql_close($con);
   $testfile='Test'.$_POST[testuser].'_'.$_POST[solver].'_'.$randtime;
   echo $testfile; 
}
?>
</body>
</html>
