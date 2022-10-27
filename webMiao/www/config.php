<?php
//close error report
error_reporting(0);

/* mysql connection */
$mysql_host="localhost";
$mysql_username="root";
$mysql_password="xxx123abc";
$mysql_dbname="2022XSCTF_webMiao";
$con=mysqli_connect($mysql_host,$mysql_username,$mysql_password,$mysql_dbname);
//var_dump($con);
//secret
$JWT_secret="miao_pa_si";

$username="";