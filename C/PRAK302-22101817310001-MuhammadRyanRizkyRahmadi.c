#include <stdio.h>

int main (){
    int nilai;
        printf("Nilai\t=");
        scanf("%d", &nilai);
         if (nilai>=80 && nilai<=100){
            printf("Nilainya adalah A");
         }
         else if (nilai>=70 && nilai <=79){
            printf("Nilainya adalah B");
         }
         else if (nilai>=60 && nilai <=69){
            printf("Nilainya adalah C");
         }
         else if (nilai>=50 && nilai <=59){
            printf("Nilainya adalah D");
         }
         else{
            printf("Nilainya adalah E");
         }
}