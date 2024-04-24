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
mysql_select_db(my_db1,$con);

$cp_table=db1_table;

$fid=$_GET['fid'];
$result=mysql_query("select * from ".$cp_table." where id=".$fid);

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

while($q=mysql_fetch_array($result)){
      $id=$q[id];
      $user=$q[User_name];
      $solver=$q[Solver];
      $time=$q[Time];
      $amount=$q[Amount];
      $case=$q[Case_name];
      $type=$q[Type];
      $random=$q[Random];
      $name=$type.'_'.$random;

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
$menu_table.='</table>';
echo $menu_table;

mysql_close($con);
?> 

<br/>
<?php
require_once("common.php");

$con=mysql_connect(my_host,my_user,my_password);
if (!$con){
   die('Counld not connect: '.mysql_error());
}
mysql_select_db(my_db1,$con);

$cp_table=db1_table;

$fid=$_GET['fid'];
$result=mysql_query("select * from ".$cp_table." where id=".$fid);

while($row=mysql_fetch_array($result)){
    $x=$row[User_name];
    $y=$row[Solver];
    $z=$row[Random];
    $amount=$row[Amount];
    $casename=$row[Case_name];
}

$fcase='<table class="bordered">';
for($i=1;$i<=$amount;$i++){
$fcase.= '
	<tr>
		<td>'.$casename.$i.'</td>
		<td><a  href="/b_residual.php?case_id='.$casename.$i.'&fid='.$fid.'" style="text-decoration:none">'.'Residual error'.'</a></td>
		<td><a  href="/b_errlog.php?case_id='.$casename.$i.'&fid='.$fid.'" style="text-decoration:none">'. 'Errlog'.'</a></td>
	</tr>';
}
$fcase.='</table>';
echo $fcase;
mysql_close($con);

echo "<br/>";
$testfile='Upload'.$x.'_'.$z;

$case_id=$_GET['case_id'];
$out_path=$testfile.'/'.$case_id.'/output.txt';
function FileLastLines($filename,$n){
    if(!$fp=fopen($filename,'r')){
        echo "open fail,maybe the path is wrong";
        return false;
    }
    $pos=-2;
    $eof="";
    $str="";
    while($n>0){
        while($eof!="\n"){
            if(!fseek($fp,$pos,SEEK_END)){
                $eof=fgetc($fp);
                $pos--;
            }else{
                break;
            }
        }
        $str.=fgets($fp);
        $eof="";
        $n--;
    }
    return $str;
 }
echo nl2br(FileLastLines($out_path,20));
?>
</body>
</html>
