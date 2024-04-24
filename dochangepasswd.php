<?php
session_start();
	$p1 = $_POST['pass1'];
	echo "p1:".$p1."         ";
	$p2 = $_POST['pass2'];
	if($p1 == $p2){
		$p1 = md5($p1);
		//do change in db
		require_once("common.php");
		$con=mysql_connect(my_host,my_user,my_password);
		if (!$con){
			die('Counld not connect: '.mysql_error());
		}
		mysql_select_db(my_db,$con);

		$cp_table="auth_user";
		$sql = " update  ".$cp_table." set password = '".$p1."' where username = '".$_SESSION['username']."' ";
		mysql_query($sql);
		header("Location:./index.php");
		$_SESSION['username']="";
		exit(0);
	}else{
		header("Location:./changepassword.php?msg=wrong");
		exit(0);
	}
?>
