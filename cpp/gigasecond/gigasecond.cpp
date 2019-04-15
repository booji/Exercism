#include "gigasecond.h"
namespace gigasecond {
    ptime advance(ptime dateTime){
        return dateTime + seconds(static_cast<int>(1e9));
    }
}
