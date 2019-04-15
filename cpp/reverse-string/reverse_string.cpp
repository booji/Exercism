#include "reverse_string.h"

namespace reverse_string {
    std::string advance(std::string& stringToReverse){
        int stringLength = stringToReverse.length()
        for (int i=0,i<stringLength/2; i++){
            std::swap(stringToReverse[i], stringToReverse[stringLength-i-1]);
        }

        return stringToReverse;
    }
}
