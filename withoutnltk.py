import matplotlib.pyplot as plt
fil_text=open('text.txt',encoding='utf-8').read()
fil_word=open('emot.txt',encoding='utf-8').read()
#removing punctuation
r_pun=['<','>',',','*','\'','(',')',':','{','}','_','-','\\','\'','.','!','?',';','/','[',']','--','@','#','%','^','&','+','=','-']
store_text=''
nowords = ["i", "me", "my", "myself", "we", "our", "ours", "ourselves", "you", "your", "yours", "yourself",
              "yourselves", "he", "him", "his", "himself", "she", "her", "hers", "herself", "it", "its", "itself",
              "they", "them", "their", "theirs", "themselves", "what", "which", "who", "whom", "this", "that", "these",
              "those", "am", "is", "are", "was", "were", "be", "been", "being", "have", "has", "had", "having", "do",
              "does", "did", "doing", "a", "an", "the", "and", "but", "if", "or", "because", "as", "until", "while",
              "of", "at", "by", "for", "with", "about", "against", "between", "into", "through", "during", "before",
              "after", "above", "below", "to", "from", "up", "down", "in", "out", "on", "off", "over", "under", "again",
              "further", "then", "once", "here", "there", "when", "where", "why", "how", "all", "any", "both", "each",
              "few", "more", "most", "other", "some", "such", "no", "nor", "not", "only", "own", "same", "so", "than",
              "too", "very", "s", "t", "can", "will", "just", "don", "should", "now"]
#Cleaning the text area for good analysis.
for letter in fil_text:
    if letter not in r_pun:
        store_text+=letter
store_text=store_text.replace('\n','')
for i in store_text:
    store_text=store_text.replace(i.upper(),i.lower())
final=list()
for j in store_text.split(' '):
    if(j not in nowords):
        final.append(j)
#Making a dictionary to handle the words and their meaning 
h_dict=dict()
count_values=dict()
#Cleaning words related to emotion 
store_word=''
for let in fil_word:
    store_word+=let 
store_word=store_word.replace('\n','')
store_word=store_word.replace('\'','')
for val in store_word.split(','):
    key,value=val.split(':')
    h_dict.update({key.strip():value.strip()})
for la in final:
    if la in list(h_dict.keys()):
        count_values[h_dict[la]]=count_values.get(h_dict[la],0)+1
    
_fig,ax1=plt.subplots()
ax1.bar(count_values.keys(),count_values.values())
_fig.autofmt_xdate()
plt.show()
