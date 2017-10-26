//
// Created by 周磊 on 30/09/2017.
//

int sequential_search(int *a, int n, int key) {
    for (int i = 1; i < n; ++i) {
        if (a[i] == key) {
            return i;
        }
    }
    return 0;
}


/*
 * 有哨兵的顺序查找，可以减少每次都判断数组是否越界
 */

int sequential_search2(int *a, int n, int key) {
    int i;
    a[0] = key;
    i = n;
    while (a[i] != key) {
        i--;
    }
    return i;
}