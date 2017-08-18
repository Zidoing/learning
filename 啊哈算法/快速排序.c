/*************************************************************************
	> File Name: 快速排序.c
	> Author: 
	> Mail: 
	> Created Time: Fri Aug 18 23:32:54 2017
 ************************************************************************/

#include<stdio.h>
int a[101], n ;
void quicksort(int left, int right){

    int i, j , t, tmp;
    if(left>right) return;

    tmp = a[left];
    i=left;
    j = right;
    while(i!=j){
        while(a[j]>=tmp && j>i){
            j--;
        }
        while(a[i]<=tmp && i<j){
            i++;
        }
        if (i<j){
            t=a[i];
            a[i] = a[j];
            a[j] = t;
        }

    }
    a[left] = a[i];
    a[i] = tmp;
    quicksort(left,i-1);
    quicksort(i+1,right);
}

int main(){
    int i, j, t;
    scanf("%d", &n);
    for(i=1;i<=n;i++){
        scanf("%d",&a[i]);
    }
    quicksort(1,n);
    for(i=1;i<=n;i++){
        printf("%d", a[i]);
    }
    getchar();getchar();
    return 0;
}
