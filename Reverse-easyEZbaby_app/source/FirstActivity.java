package com.example.activitytest;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.Toast;

import java.security.MessageDigest;
import java.security.NoSuchAlgorithmException;

public class FirstActivity extends AppCompatActivity implements View.OnClickListener{

    Button button;
    EditText username;
    EditText password;

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.first_layout);

        button = (Button)findViewById(R.id.login_button);
        username = (EditText)findViewById(R.id.username);
        password = (EditText)findViewById(R.id.password);
        button.setOnClickListener(this);
    }

    @Override
    public void onClick(View v) {
        String username1 = username.getText().toString();
        String password1 = password.getText().toString();
        String ok = "登录成功";
        String fail = "登录失败";
        if (checkUsername(username1) && checkPass(password1)){
            Toast.makeText(FirstActivity.this,ok,Toast.LENGTH_SHORT).show();
            Toast.makeText(FirstActivity.this,"flag{"+username1+password1+"}",Toast.LENGTH_SHORT).show();
        }else {
            Toast.makeText(FirstActivity.this,fail,Toast.LENGTH_SHORT).show();
        }
    }

    public boolean checkUsername(String username) {
        if (username != null) {
            try {
                if (username.length() == 0 || username == null ) {
                    return false;
                }
                MessageDigest digest = MessageDigest.getInstance("MD5");
                digest.reset();
                String name="zhishixuebao";
                digest.update(name.getBytes());
                byte[] bytes = digest.digest();
                String hexstr = toHexString(bytes, "");
                StringBuilder sb = new StringBuilder();
                for (int i = 0; i < hexstr.length(); i += 2) {
                    sb.append(hexstr.charAt(i));
                }
                String userSN = sb.toString();
                return new StringBuilder().append(userSN).toString().equals(username);
            } catch (NoSuchAlgorithmException e) {
                e.printStackTrace();
                return false;
            }
        }
        return false;
    }

    public boolean checkPass(String password) {
        if (password != null) {
            char[] pass = password.toCharArray();
            if (pass.length != 15) {
                return false;
            }
            for (int len = 0; len < pass.length; len++) {
                pass[len] = (char) (((255 - len+2) - 98) - pass[len]);
                if (pass[len] != '0' || len >= 15) {
                    return false;
                }
            }
            return true;
        }
        return false;
    }


    private static String toHexString(byte[] bytes, String separator) {
        StringBuilder hexString = new StringBuilder();
        for (byte b : bytes) {
            String hex = Integer.toHexString(b & 255);
            if (hex.length() == 1) {
                hexString.append('0');
            }
            hexString.append(hex).append(separator);
        }
        return hexString.toString();
    }


}