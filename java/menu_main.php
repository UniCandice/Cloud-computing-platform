<?php
$menu = '
<noscript>
JavaScript is turned off in your web browser. Turn it on to take full advantage of this site, then refresh the page.
</noscript>
<table width="100%">
<tr>
<td>
<ul class="show" id="mainmenu">';


$menu .= '
<li>
<a href="http://127.0.0.1:8000/admin/" target="new">'.
'Admin'.
'</a>
</li>';

$menu.='
<li>'.
'Monitoring'.
       '<ul>';
$menu .= '
	<li><a  href="/mon_node.php">'.'Nodes'.'</a></li>
        <li><a  href="/mon_job.php">'.'Jobs'.'</a></li>';
$menu .= '
 	</ul>
</li>';

$menu .= '
<li>
<a href="/a_testcase.php">'.
'TestCase'.
'</a>
</li>';

$menu .= '
<li>
<a href="/l_upload.php" target="_blank">'.
'Upload'.
'</a>
</li>';

$menu .= '
<li>
<a href="/task.php">'.
'Task'.
'</a>
</li>';

$menu .= '
<li>
<a href="/acfdra.php">'.
'ACFDRA'.
'</a>
</li>';

$menu .='</ul>';

return $menu;
?>
