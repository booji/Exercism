#include "gigasecond.h"
namespace gigasecond {
    ptime advance(ptime dateTime){
        return dateTime + seconds(1000000000);
    }
}
