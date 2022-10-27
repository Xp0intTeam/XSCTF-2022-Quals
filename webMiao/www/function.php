<?php
include "config.php";
header("Content-type:text/html;charset=utf-8");

function is_login()
{
    global $username,$secret;
    if (!isset($_COOKIE["JWT"]))
        return false;
    $jwt = Jwt::getInstance();
    if($jwt->verifyToken($_COOKIE["JWT"]) == false)
        return false;

    return true;
}

//function get_real_ip() {
//    $ip = false;
//    if (!empty($_SERVER["HTTP_CLIENT_IP"])) {
//        $ip = $_SERVER["HTTP_CLIENT_IP"];
//    }
//    if (!empty($_SERVER['HTTP_X_FORWARDED_FOR'])) {
//        $ips = explode(", ", $_SERVER['HTTP_X_FORWARDED_FOR']);
//        if ($ip) {
//            array_unshift($ips, $ip);
//            $ip = FALSE;}
//        for ($i = 0; $i < count($ips); $i++) {
//            if (!eregi("^(10│172.16│192.168).", $ips[$i])) {
//                $ip = $ips[$i];
//                break;
//            }
//        }
//    }
//    return ($ip ? $ip : $_SERVER['REMOTE_ADDR']);
//}

class Jwt
{
    //使用HMAC生成信息摘要时所使用的密钥(自定义)
    private static $key;
    private static $instance = null;

    //头部
    private static $header = [
        'alg' => 'HS256', //生成signature的算法
        'typ' => 'JWT'    //类型
    ];

    private static $payload = [];


    private function __construct()
    {
        global $JWT_secret;
        self::$key = $JWT_secret;
    }

    private function __clone()
    {
        // TODO: Implement __clone() method.
    }

    public static function getInstance()
    {
        if(!self::$instance){
            self::$instance = new self();
        }
        return self::$instance;
    }

    /**
     * @desc  设置$payload jwt载荷
     * @param array $payload jwt载荷   格式如下非必须
     * [
     *  'iss'=>'jwt_admin',  //该JWT的签发者
     *  'iat'=>time(),  //签发时间
     *  'exp'=>time()+7200,  //过期时间
     *  'nbf'=>time()+60,  //该时间之前不接收处理该Token
     *  'sub'=>'www.admin.com',  //面向的用户
     *  'jti'=>md5(uniqid('JWT').time())  //该Token唯一标识
     * ]
     * @param int $uid
     */
    public static function setPayLoad($uid = 0,$status='guest')
    {
        self::$payload = [
            'uid' => $uid,         // 用户id
            'iss' => 'miao_king',  //该JWT的签发者
            'iat' => time(),       //签发时间
            'status' => $status,    //默认是顾客
            //'exp' => time() + 7200,  //过期时间
            //'nbf' => time() + 60,  //该时间之前不接收处理该Token
            //'sub' => 'www.admin.com',  //面向的用户
            //'jti' => md5(uniqid('JWT') . time())  //该Token唯一标识
        ];
    }

    /**
     * 获取jwt token
     * @return bool|string
     */
    public static function getToken()
    {
        $base64header = self::base64UrlEncode(json_encode(self::$header, JSON_UNESCAPED_UNICODE));
        $base64payload = self::base64UrlEncode(json_encode(self::$payload, JSON_UNESCAPED_UNICODE));
        return $base64header . '.' . $base64payload . '.' . self::signature($base64header . '.' . $base64payload, self::$key, self::$header['alg']);
    }


    /**
     * 验证token是否有效,默认验证exp,nbf,iat时间
     * @param string $Token 需要验证的token
     * @return bool|string
     */
    public static function verifyToken($Token)
    {
        $tokens = explode('.', $Token);
        if (count($tokens) != 3)
            return false;

        list($base64header, $base64payload, $sign) = $tokens;

        //获取jwt算法
        $base64decodeheader = json_decode(self::base64UrlDecode($base64header), JSON_OBJECT_AS_ARRAY);
        if (empty($base64decodeheader['alg']))
            return false;

        //签名验证
        if (self::signature($base64header . '.' . $base64payload, self::$key, $base64decodeheader['alg']) !== $sign)
            return false;

        $payload = json_decode(self::base64UrlDecode($base64payload), JSON_OBJECT_AS_ARRAY);

        //签发时间大于当前服务器时间验证失败
        if (isset($payload['iat']) && $payload['iat'] > time())
            return false;

        //过期时间小于当前服务器时间验证失败
        if (isset($payload['exp']) && $payload['exp'] < time())
            return false;

        //该nbf时间之前不接收处理该Token
        if (isset($payload['nbf']) && $payload['nbf'] > time())
            return false;

        return $payload;
    }

    /**
     * HMACSHA256签名   https://jwt.io/  中HMACSHA256签名实现
     * @param string $input 为base64UrlEncode(header).".".base64UrlEncode(payload)
     * @param string $key
     * @param string $alg 算法方式
     * @return mixed
     */
    private static function signature($input,$key,$alg = 'HS256')
    {
        $alg_config = [
            'HS256' => 'sha256'
        ];
        if($alg != 'HS256'){
            exit("no！！！you can't change the alg");
        }
        return self::base64UrlEncode(hash_hmac($alg_config[$alg], $input, $key, true));
    }


    /**
     * Encodes to base64url
     *
     * @param string $data
     * @return string
     */
    public static function base64UrlEncode($data)
    {
        return str_replace('=', '', strtr(base64_encode($data), '+/', '-_'));
    }

    /**
     * Decodes from base64url
     *
     * @param string $data
     * @return string
     */
    public static function base64UrlDecode($data)
    {
        if ($remainder = strlen($data) % 4) {
            $data .= str_repeat('=', 4 - $remainder);
        }

        return base64_decode(strtr($data, '-_', '+/'));
    }
}

class Request {
    public function get($par){
        return $_GET[$par];
    }

    public function post($data){
        return $_POST[$data];
    }

    public function cookie($cook){
        return $_COOKIE[$cook];
    }

}

// 简单调用
//class Test2 {
//    //  生成token
//    public function getToken()
//    {
//        $jwt = Jwt::getInstance();
//        $jwt->setPayLoad(1);
//        $jwtToken = $jwt->getToken();
//        var_dump($jwtToken);
//    }
//
//    // 校验token
//    public function verifyToken(Request $request)
//    {
//        $token = $request->get('token');
//        $jwt = Jwt::getInstance();
//        $result = $jwt->verifyToken($token);
//        var_dump($result);
//    }
//}
