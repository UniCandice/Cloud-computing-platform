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

$con=mysql_connect(my_host,my_user,my_password);
if (!$con){
   die('Counld not connect: '.mysql_error());
}
mysql_select_db(my_db,$con);

$cp_table=db1_table;
$is_superuser = 0;
//判断用户是否是管理员 is_superuser
$sql = "select is_superuser from auth_user where username = '".$_SESSION['username']."' ";
$result = mysql_query($sql);
while($q = mysql_fetch_array($result)){
	$is_superuser = $q['is_superuser'];
}
mysql_select_db(my_db1,$con);
//如果是管理员 取出所有
if($is_superuser == "1"){
	$sql = "select * from ".$cp_table."  order by id asc";
}else{ //如果不是管理员 只取用户自己的
	$sql = "select * from ".$cp_table." where User_name = '".$_SESSION['username']."' order by id asc";
}
/*echo $sql;*/
$result=mysql_query($sql);
$menu_table='<table class="bordered">
    <thead>
    <tr>
        <th>ID</th>        
        <th>Filename</th>
        <th>Solver</th>
        <th>User</th>
	<th>Time</th>
        <th>Case</th>
	<th>Option</th>
	<th>Status</th>
	<th>Result</th>
    </tr>
   </thead>';

while($q=mysql_fetch_array($result)){ //取出每个表里的内容
$id=$q[id];
$user=$q[User_name];
$solver=$q[Solver];
$time=$q[Time];
$amount=$q[Amount];
$case=$q[Case_name];
$type=$q[Type];
$random=$q[Random];
$name=$type.'_'.$random;

if($type=="Test"){
   $tcase_table='tcase'.$random;
   $t1=mysql_query("select * from ".$tcase_table);

   $menu_table.='<tr>
                  <td>'.$id.'</td>        
                  <td>'.$name.'</td>
                  <td>'.$solver.'</td>
		  <td>'.$user.'</td>
		  <td>'.$time.'</td>
                  <td>
                      <dl>';
    while($c1=mysql_fetch_array($t1)){
         $menu_table.='<dt>'.$c1[Case_name].'</dt>';
    }             
		       $run = '<dt><a href="/a_run.php?fid='.$id.'" style="text-decoration:none">'.'Run'.'</a></dt>';
		       $run .= '<dt><a href="/a_check.php?fid='.$id.'" style="text-decoration:none">'.'Check'.'</a></dt>';
		       $run .= '<dt><a href="/a_kill.php?fid='.$id.'" style="text-decoration:none">'.'Kill'.'</a></dt>';
    			if($solver=='ch19'){
       				$run.='<dt><a href="/a_rerun.php?fid='.$id.'" style="text-decoration:none">'.'Rerun'.'</a></dt>';
   			 }
    			$run.='<dt><a href="/a_delete.php?fid='.$id.'" style="text-decoration:none">'.'Delete'.'</a></dt>';

    $menu_table.='   </dl>
                  </td>
		  <td>
		     <dl>
			'.$run.'
		     </dl>
		  </td>
		  <td>
		      <dl>
		       <dt><a href="/a_status.php?fid='.$id.'" style="text-decoration:none">'.'Status'.'</a></dt>
		      </dl>
		  </td>
		  <td>
		    <dl>
		      <dt><a href="/a_download.php?fid='.$id.'" style="text-decoration:none">'.'Download'.'</a></dt>
		      <dt><a href="/a_map.php?fid='.$id.'" style="text-decoration:none">'.'Map'.'</a></dt>
                      <dt><a href="/a_analyse.php?fid='.$id.'" style="text-decoration:none">'.'Analyse'.'</a></dt>
		    </dl>
		  </td>
             </tr>';        
}
elseif($type=="Upload"){

    $menu_table.='<tr>
                  <td>'.$id.'</td>        
                  <td>'.$name.'</td>
                  <td>'.$solver.'</td>
		  <td>'.$user.'</td>
		  <td>'.$time.'</td>
                  <td>
                     <dl>';
    for($i=1;$i<=$amount;$i++){
         $menu_table.='<dt>'.$case.$i.'</dt>';
        }
    $menu_table.='</dl>
                  </td>
		  <td>
		     <dl>
		       <dt><a href="/b_run.php?fid='.$id.'" style="text-decoration:none">'.'Run'.'</a></dt>
		       <dt><a href="/b_check.php?fid='.$id.'" style="text-decoration:none">'.'Check'.'</a></dt>
		       <dt><a href="/b_kill.php?fid='.$id.'" style="text-decoration:none">'.'Kill'.'</a></dt>';
    if($solver=='ch19'){
       $menu_table.='<dt><a href="/b_rerun.php?fid='.$id.'" style="text-decoration:none">'.'Rerun'.'</a></dt>';
    }
    $menu_table.='<dt><a href="/b_delete.php?fid='.$id.'" style="text-decoration:none">'.'Delete'.'</a></dt>
		     </dl>
		  </td>
		  <td>
		      <dl>
		       <dt><a href="/b_status.php?fid='.$id.'" style="text-decoration:none">'.'Status'.'</a></dt>
		      </dl>
		  </td>
		  <td>
		    <dl>
		      <dt><a href="/b_download.php?fid='.$id.'" style="text-decoration:none">'.'Download'.'</a></dt>
		      <dt><a href="/b_map.php?fid='.$id.'" style="text-decoration:none">'.'Map'.'</a></dt>
		    </dl>
		  </td>
             </tr>';        
}
}
$menu_table.='</table>';
echo $menu_table;

mysql_close($con);
?>     
</body>
</html>
