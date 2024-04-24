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

<form action="b_upload_file.php" method="post" enctype="multipart/form-data">
<table class="upload">
<tr>
   <td>User</td>
<?php
echo '<td><input type="text" name="uploaduser" value="'.$_SESSION['username'].'"></td>';
?>
</tr>
<tr>
   <td>Case</td>
   <td><input type="text" name="casename"></td>
</tr>
<tr>
   <td>Number</td>
   <td><input type="number" name="up_number" min="1" max="1000"></td>
</tr>
<tr>
   <td><label for="file">Solver</label></td>
   <td><input type="file" name="usrfile[]" id="file"/></td>
</tr>
<tr>
   <td><label for="file">Grid</label></td>
   <td><input type="file" name="usrfile[]" id="file"/></td>
</tr>
<tr>
   <td><label for="file">Control_File</label></td>
   <td><input type="file" name="usrfile[]" id="file"/></td>
</tr>
<tr>
   <td><label for="file">Status_Form</label></td>
   <td><input type="file" name="usrfile[]" id="file"/></td>
</tr>
<tr>
<td></td>
<td><input type="submit" name="upsubmit" value="Submit" /></td>
</tr>
</table>
</form>

</body>
</html>
