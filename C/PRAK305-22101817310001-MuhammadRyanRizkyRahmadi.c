#include <stdio.h>
int main (){
    int detik,hari,jam,menit,detikI,mA,mB;
        printf("Sebuah bilangan yang merepresentasikan detik\t=");
        scanf("%d", &detik);
            hari=detik/(3600* 24);
            mA= detik % (3600* 24);
            jam= mA/3600;
            mB= detik % 3600;
            menit= mB/60;
            detikI=detik % 60;
             if(detik>=1 && detik<60){
                printf("00:00:%.2d", detikI);
             }
             else if (detik>=60 && detik<3600){
                printf("00:%.2d:%.2d",menit,detikI);
             }
             else if (detik>=3600 && detik<86400){
                printf("%.2d:%.2d:%.2d", jam,menit,detikI);
             }
             else {
                printf("%d Hari %.2d:%.2d:%.2d", hari,jam,menit,detikI);
             }
}            