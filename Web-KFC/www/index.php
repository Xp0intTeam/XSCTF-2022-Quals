<?php
function parse_headers(){
    $headers = [];
    foreach ($_SERVER as $name => $value)
    {
        if (substr($name, 0, 5) == 'HTTP_')
        {
            $headers[str_replace(' ', '-', ucwords(strtolower(str_replace('_', ' ', substr($name, 5)))))] = $value;
        }
    }
    return $headers;
}
header("money: 0");
$locals = array("127.0.0.1", "localhost");
$local_urls = array("http://www.kfc.com.cn", "http://www.kfc.com.cn/", "www.kfc.com.cn");

if (isset($_SERVER['HTTP_X_FORWARDED_FOR'])){
	if(in_array($_SERVER['HTTP_X_FORWARDED_FOR'], $locals)){
		if(isset($_SERVER['HTTP_REFERER'])){
			for ($i=0; $i < count($local_urls) ; $i++) 
			{ 
				if (strpos($_SERVER['HTTP_REFERER'],$local_urls[i]) !== Flase) {
					$header_s=parse_headers();
					if($header_s['Money']=="50")
					{
						echo '<p style="text-align: center;"><img src="./run.jpg" alt="" width=500px height=340px> </p>';
						die("<p>flag{0k_!_G1v3_Y0u_th3_f1l@g_!_!} </p>");
					}
					echo '<p style="text-align: center;"><img src="./v50.jpg" alt="" width=132px height=188px> </p>';
					die("Have you v me 50?");
				}
			}
			die("<p>tip：点点KFC.png?(Referer:****.cn)</p>");
		}
		echo '<p style="text-align: center;"><a href="http://www.kfc.com.cn"><img src="./kfc.png" alt="" width=400px height=400px></a></p>';
		die("<p>Are you jump from KFC's website?(http:****.cn)</p>");
	}
	echo '<p style="text-align: center;"><img src="./127.gif" alt="" width=360px height=312px> </p>';
}
echo '<p style="text-align: center;"><img src="./127.gif" alt="" width=360px height=312px> </p>';
die("Are you come from localhost?");
?>