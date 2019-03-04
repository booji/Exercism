#include <string>
#include <map>
#include <stdexcept>
namespace dna{
    class counter
    {
        std::map<char,int> nucleotide;
    public:
        counter(const std::string& DNAString) :
        nucleotide(std::map<char, int>({
            {'A', 0},
            {'T', 0},
            {'C', 0},
            {'G', 0}}))

        {
        for(char c: DNAString)
            ++nucleotide[c];
        }
    std:: map<char,int> nucleotide_counts() const
    {
        return nucleotide;
    }
    int count(char c) const
    {
        if(nucleotide.find(c) == nucleotide.end())
            throw std::invalid_argument(std::string("invalid nucleotide: ") + c);

        return nucleotide.at(c);
    }
    };

}
