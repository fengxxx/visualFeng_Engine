/*
#include <stdio.h>

int main()
{
     const int n = 5;
     int i, j, temp;
     int gap = 0;
     int a[] = {5, 4, 3, 2, 1};
     while (gap<=n)
     {
          gap = gap * 3 + 1;
     }
     while (gap > 0)
     {
         for ( i = gap; i < n; i++ )
         {
             j = i - gap;
             temp = a[i];
             while (( j >= 0 ) && ( a[j] > temp ))
             {
                 a[j + gap] = a[j];
                 j = j - gap;
             }
             a[j + gap] = temp;
         }
         gap = ( gap - 1 ) / 3;
     }

    for(i=0;i<5;i++){
        printf("%i ",a[i]);
        printf(",");
    }

 }
*/
