//
// Created by 周磊 on 05/09/2017.
//

int Index(String S, String T, int pos) {
    int n, m, i;
    String sub;
    if (pos > 0) {
        n = StrLength(S);
        m = StrLength(T);
        i = pos;
        while (i <= n - m + 1) {
            SubString(sub, S, i, m);
            if (StrCompare(sub, T) != 0) {
                i++;
            } else {
                return i;
            }
        }
    }
}

int Index2(String S, String T, int pos) {
    int i = pos;
    int j = 1;
    while (i <= S[0] && T[j]) {
        i++;
        j++;
    }
}