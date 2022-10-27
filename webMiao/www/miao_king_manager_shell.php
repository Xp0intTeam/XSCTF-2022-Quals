<?php
include "function.php";
header("Content-type:text/html;charset=utf-8");

error_reporting(0);
ini_set('display_errors', 0);

if (is_login()==false){
    echo "必须先登录成功取得admin身份才能使用shell控制台！";
    exit();
}
else{
    $jwt = Jwt::getInstance();
    $status = $jwt->verifyToken($_COOKIE['JWT'])['status'];
    if ($status!='admin'){
        echo "必须先登录成功取得admin身份才能使用shell控制台！";
        exit();
    }
}


if(isset($_POST['miao'])){
    $miao= $_POST['miao'];
    $check = 0;
    if(is_array($miao)==false){
        if(preg_match('/\^|\+|\~|\$|\[|\]|\{|\}|glob|\&|-|\`|\||scandir|\'|\"|\./i', $miao)){
                $check=$check+1;
        }
        if($check==0){
            eval($miao);
            $clear = ob_get_contents();
            ob_end_clean();
        }
    }
}
else{
    highlight_file(__FILE__);
}

?>