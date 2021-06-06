COMMAND LINE TOOLS Programming Test
===================================

Identifying words by frequency

A bigram is sequence of two consecutive tokens. The previous sentence, for example, contains the
bigrams: (a bigram), (bigram is), (is sequence), (sequence of), (of two), (two consecutive), and
(consecutive tokens).
Across the entire corpus find (1) the top 50 most frequent unigrams (single tokens), and (2) the top 50 most frequent bigrams.
The output should be a list of 100 lines, where the first 50 lines contain a single term each (i.e. one word - unigram - per line), in order
of frequency, followed by 50 lines containing two terms each (two words - bigram - per line), in order of the bigram frequency.

Please use command line tools of your choice (e.g. grep, awk, sort, etc.)


grep -o '[[:alnum:]]*' corpus.txt | sort | uniq -c | sed -E 's/[[:space:]]*([0-9]+) (.+)/\2@\1/'
cat corpus.txt | tr '[:upper:]' '[:lower:]' | sort | uniq -c | sort -rn


cat corpus.txt | tr '[:upper:]' '[:lower:]' | tr -d '[:punct:]' | tr ' ' '\n' 



  
  
  
  
  
  
{tr -sc "[A-Z][a-z][0-9]'" '[\012*]' < "corpus.txt" | \
  tr '[A-Z]' '[a-z]' | \
  sort | uniq -c | sort -nr |sed 's/[0-9]*//g'| tr -d "[:blank:]"| \
  head -n10 & \
  tr -sc "[A-Z][a-z][0-9]'" '[\012*]' < "corpus.txt" | \
  tr '[A-Z]' '[a-z]' | \
  awk -- 'prev!="" { print prev,$0; } { prev=$0; }' | \
  sort | uniq -c | sort -nr | sed 's/[0-9]*//g'|awk '{$1=$1;print}'|\
  head -n10 ; } > tmp.txt
  
  
  tr -sc "[A-Z][a-z][0-9]'" '[\012*]' < "corpus.txt" | \
  tr '[A-Z]' '[a-z]' | \
  awk -- 'prev!="" { print prev,$0; } { prev=$0; }' | \
  sort | uniq -c | sort -nr |sed 's/[0-9]*//g'| \
  head -n10|awk '{$1=$1};1'
  
