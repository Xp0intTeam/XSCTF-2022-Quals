<?php
include "config.php";
include "function.php";
header("Content-type:text/html;charset=utf-8");

$username="";

if (!is_login() && (!isset($_POST["username"]) || !isset($_POST["password"])))
{
    header('Location: index.php');
    die;
}

if (is_login() && (!isset($_POST["username"]) || !isset($_POST["password"]))){
    $jwt = Jwt::getInstance();
    $status = $jwt->verifyToken($_COOKIE['JWT'])['status'];
    if ($status!='admin'){
        echo "<div>";
        echo "你的身份是guest，请先登录获取admin身份以进行下一步操作~~";
        echo "</div>";
        echo "<br>";
        echo '<img src="./images/guest.jpg">';
        exit();
    }
    else{
        echo "<div>";
        echo "你的身份是admin，恭喜！！！~~";
        echo "</div>";
        echo "<br>";
        echo "<div>";
        echo "请大佬赶快进入webshell控制台界面："."<a href='./miao_king_manager_shell.php'>miao_king_manager_shell.php</a>";
        echo "</div>";
        echo "<br>";
        echo '<img src="./images/admin.jpg">';
        exit();
    }
}



    $stmt=$con->prepare("select * from users where username=?");
    $stmt->bind_param("s",$_POST["username"]);
    $stmt->execute();
    $result=$stmt->get_result();
    $row=$result->fetch_assoc();
    if ($row["password"]===$_POST["password"])
    {
        $username=$_POST["username"];
        $status = 'admin';
        $jwt = Jwt::getInstance();
        $jwt->setPayLoad(1,$status);
        $jwt_payload = $jwt->getToken();
        setcookie("JWT",$jwt_payload);
        header('Location: user.php');
    }
    else
    {
        header('Location: index.php');
        die;
    }
