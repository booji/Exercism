// #if !defined(LEAP_H)
// #define LEAP_H
namespace leap {
    bool is_leap_year(int year) {
        bool flag = false;
        if(year % 4 == 0 && (year % 100 != 0 || year % 400 == 0)){
            flag = true;
        }
        return flag;
    }
}
