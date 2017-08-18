/*************************************************************************
	> File Name: 顺序表.c
	> Author: 
	> Mail: 
	> Created Time: Fri Aug 18 17:09:13 2017
 ************************************************************************/

#include<stdio.h>
#include<stdlib.h>
/*
#define MaxSize 100
ELemType Sqlist[MaxSize];
int len;
*/

#define MaxSize 100
typedef int Ele



typedef struct{
    Sqlist * elem;
    int length;
    int listsize;
}Sqlist;





void initSqlist(Sqlist * L){
    L->elem = (int *)malloc(MaxSize*sizeof(Sqlist));
    if(!L->elem) exit(0);
    L->length = 0;
    L->listsize = MaxSize;
    
}


int main(void){

}
