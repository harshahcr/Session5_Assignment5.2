#Declare all the items required in framing sentence
subject=["Americans", "Indians","Chinese"]
verb=["Play", "watch"]
object=["Baseball","cricket","Table Tennis"]
ComSent = ''
#using loop condition
for sub in subject:
    for vb in verb:
        for obj in object:
            ComSent = (sub+" "+vb+" "+obj)
            print(ComSent)