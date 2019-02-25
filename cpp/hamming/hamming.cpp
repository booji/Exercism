#include "hamming.h"

int hamming::compute(const std::string originalDNA, const std::string replicantDNA){
    int count =0;
    if (originalDNA.length() != replicantDNA.length()){
        throw std::domain_error("DNA strings have to be of equal length");
    }
    for (std::string::size_type i = 0; i < originalDNA.size(); ++i){
        if (originalDNA[i] != replicantDNA[i]){
            count++;
        }
    }
    return count;
}
