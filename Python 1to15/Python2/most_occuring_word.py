# example.py
#
#Determine the most common word in list

Word = {
    'you', 'he', 'they', 'his', 'we', 'you', 'their', 'he',
    'his' ,'I', 'she', 'were', 'group', 'there', 'the', 'do', 
    'this', 'you', 'they', 'shall', 'be', 'this', 'could',
    'should', 'be', 'are', 'were', 'am', 'when', 'where', 'how', 'why'
}

from collections import Counter
word_counts = Counter(Word)
top_three = Word_count.most_count(3)
print top_three


# Example merging of in more words
morewords = ['why', 'shall', 'shall', 'go', 'there', 'now']
word_counts.update(morewords)
print(word_counts.most_common(3))