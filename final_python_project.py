file_content = """
Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum.

"""
uninteresting_words = ["the", "a", "to", "if", "is", "it", "of", "and", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both", "each", "few", "more","s", "some", "such", "no", "nor", "too", "very", "can", "will", "just"]

file_content = "".join((i if i.isalpha() else " ")for i in file_content).lower().split()
new_file_content = []
dicto = {}
for i in file_content:
    if i not in uninteresting_words:
        new_file_content.append(i)
dicto = {j : new_file_content.count(j) for j in new_file_content}
print(new_file_content)













# file_content = "".join((char if char.isalpha() else " ") for char in file_content).lower().split()
# file_content = "".join(file_content).lower().split()
# sprt_words = []
# for i in file_content:
#     if i.isalpha() == False:
#         sprt_words.append(i)
#     else:
#         sprt_word = " "
# print(file_content)
# print(sprt_words)