<?php
include "config.php";
include "hint.php";
header("Content-type:text/html;charset=utf-8");

$deal = ['\\\\',"00","\\0","%00","\0","\\\"","\\'","'"];
//$deal = [];


if (isset($_GET["id"])){
    $GET_num = $_GET["id"];
    $GET_num=addslashes($GET_num);
    $GET_num=str_replace($deal,"",$GET_num);
}
else{
    $GET_num = rand(1,4);
}

if (isset($_GET["picture_path"])){
    $picture_where=$_GET["picture_path"];
    $picture_where=addslashes($picture_where);
    $picture_where=str_replace($deal,"",$picture_where);
}
else{
    $picture_path='';
}

$picture_tablename = 'images';

$sql="select * from {$picture_tablename} where id='".$GET_num."' or path='".$picture_where."'";
//echo $sql;
$sql = trim($sql);
if (preg_match("/(load)|(when)|(information)|(join)|(using)|(users)|(password)|(regexp)|(like)|(having)|(sleep)|(benchmark)|(from)|(database)|(if)|(\()|(\))|(case)/i",$sql))
{
    die("No,You can't be a Hacker");
}


$result=mysqli_query($con,$sql);
$row=mysqli_fetch_array($result,MYSQLI_ASSOC);

$path_from_db = $row["path"];

//禁止的路径
$count=preg_match("/(\.\.)/i",$path_from_db);
if ($count>0)
{
    die("No,You can't be a Hacker");
}

#设置返回的文件流
header("Content-Type: image/jpeg");

if($path_from_db==false){
    echo "NO thing Found!";
}
else {
    $picture_where="./" . $path_from_db;
    readfile($picture_where);
}