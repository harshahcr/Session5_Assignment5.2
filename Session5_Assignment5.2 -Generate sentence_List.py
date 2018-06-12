#Declare all the items required in framing sentence
subject=["Americans", "Indians","Chinese"]
verb=["Play", "watch"]
object=["Baseball","cricket","Table Tennis"]

# Use list comprehension
sentence_list = [(sub+" "+ vb + " " + ob) for sub in subject for vb in verb for ob in object]
for sentence in sentence_list:
    print (sentence)