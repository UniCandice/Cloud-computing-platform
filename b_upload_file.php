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
   

   $upload_path=cfd_prefix.'/Upload'.$x1."_".$randtime;
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

   $solvername=$_FILES["usrfile"]["name"][0];

   $r1=mysql_query("select * from ".$cp_table." where Type='Upload' and Random=".$randtime);
   $q1=mysql_fetch_array($r1);
   if($q1){
      $randtime=mt_rand(10000000,20000000);
      /*mysql_query("delete from ".$cp_table." where Type='Upload' and Random=".$randtime);*/
   }
   mysql_query("insert into ".$cp_table." (Type,User_name,Solver,Random,Amount,Case_name,Time) 
             values ('Upload','$x1','$solvername','$randtime','$x2','$x3','$y')");
   mysql_close($con);
   
   echo $upload_path.'<br/>';
   echo $_POST[uploaduser].'<br/>';
   $file_count=count($_FILES["usrfile"])-1;
   echo $file_count;
   echo "<br/>";
   for($i=0;$i<$file_count;$i++)
{
/*if ((($_FILES["file"]["type"] == "image/gif")
|| ($_FILES["file"]["type"] == "image/jpg")
|| ($_FILES["file"]["type"] == "image/pjpeg"))
&& ($_FILES["file"]["size"] < 20000))
  {
*/
  
  if ($_FILES["usrfile"]["error"][$i] > 0)
    {
    echo "Return Code: " . $_FILES["usrfile"]["error"][$i] . " Kb<br />";
    }
  else
    {
    echo "Upload: " . $_FILES["usrfile"]["name"][$i] . "<br />";
    echo "Type: " . $_FILES["usrfile"]["type"][$i] . "<br />";
    echo "Size: " . $_FILES["usrfile"]["size"][$i] . " Kb<br />";
    echo "Temp file: " . $_FILES["usrfile"]["tmp_name"][$i] . "<br />";

/*    if (file_exists($upload_path.'/'.$_FILES["usrfile"]["name"][$i]))
      {
      echo $_FILES["usrfile"]["name"][$i] . " already exists. ". "<br />";
      }
    else
      {*/
      move_uploaded_file($_FILES["usrfile"]["tmp_name"][$i],$upload_path.'/'.$_FILES["usrfile"]["name"][$i]);
      echo "Stored in: " .$upload_path.'/'.$_FILES["usrfile"]["name"][$i]."<br/>";
      
    }
/*  }
else
  {
  echo "Invalid file";
  }*/
}
}
?>


</body>
</html>
