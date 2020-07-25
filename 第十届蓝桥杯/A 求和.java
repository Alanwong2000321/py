package com.company;

import javax.swing.*;
import java.awt.*;
import java.util.*;

public class Main {
    public static void main(String[] args) {
        int count=0,temp=0;
        for (int i = 1; i <=2019; i++) {
            int b = i;
            temp=i;
            while(b!=0){
                int a = b%10;
                if(a==2 || a==0||a==1||a==9){
                    count+=temp;
                    break;
                }
                b/=10;
            }
        }
        System.out.println(count);
    }
        }
