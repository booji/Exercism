#include "difference_of_squares.h"

namespace squares{
    int square_of_sum(int num){
        int total = 0;
        for (int i = 1; i < num+1; ++i){
            total += i;
        }

        return int(pow(total,2));
    }

    int sum_of_squares(int num){
            int total = 0;
            for (int i = 1; i < num+1; ++i){
                total += int(pow(i,2));
            }
            return total;
    }

    int difference(int num){
        return square_of_sum(num)-sum_of_squares(num);
    }
}
