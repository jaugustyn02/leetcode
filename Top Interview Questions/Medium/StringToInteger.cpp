# 8. String to Integer (atoi)
# Implement the myAtoi(string s) function, which converts a string to a 32-bit signed integer (similar to C/C++'s atoi function).


class Solution {
public:
    int myAtoi(string s) {
        int i=0;
        while(s[i] == ' ') ++i;
        int sign = 1;
        if(s[i] == '+' || s[i] == '-'){
            sign = (s[i] == '-' ? -1 : 1);
            ++i;
        }
        long num = 0;
        while(isdigit(s[i])){
            num *= 10;
            num += int(s[i]) - 48;
            if (num > INT_MAX || (sign == 1 && num == INT_MAX))
                return (sign == 1 ? INT_MAX : INT_MIN);
            ++i;  
        }
        return sign * num;
    }
};
