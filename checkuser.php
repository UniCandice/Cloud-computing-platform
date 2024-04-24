<?php
require_once("common.php");
session_save_path(cfd_prefix.'/session');
session_start();
$con=mysql_connect(my_host,my_user,my_password);
if (!$con){
   die('Counld not connect: '.mysql_error());
}
mysql_select_db(my_db,$con);

$cp_table="auth_user";
$username = $_POST['username'];
$passwd = $_POST['passwd'];
$sql = " select password,is_superuser from ".$cp_table." where username = '".$username."' ";
$result=mysql_query($sql);
while($row = mysql_fetch_array($result)){
	$passdb = $row['password'];
	$is_superuser = $row['is_superuser'];
}
	if($passdb == md5($passwd)){ //密码正确
		$_SESSION["username"] = $username;
		$_SESSION["is_superuser"] = $is_superuser;
		header("Location:task.php");
	}else{  //密码错误
		header("Location:index.php?msg=loginfail");
	}
?>
