<html>

<head>
</head>

<h1>Files</h1>

<?
$handle = opendir(".");
while($entry = readdir($handle)) {
	if(is_dir($entry) || $entry == "index.php") {
		continue;
	}
	$size = filesize($entry);
	if($size > 1048576) {
		$size = floor($size / 1048576);
		echo "<a href=\"$entry\">$entry</a> [$size MB]<br />\n";
	}
	else {
		echo "<a href=\"$entry\">$entry</a> [$size]<br />\n";
	}
}
closedir($handle)
?>



</html>
