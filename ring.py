n = int(input("Enter the number of processors - "))

processor = []
status = []
temp1 = []
temp2 = []

for i in range(n):
    print("Enter the processor id -")
    processor.append(int(input()))

for i in range(n):
    print("Enter the status")
    status.append(int(input()))

print("processor status")
for i in range(n):
    print(processor[i]," ",status[i])

failure = int(input("Enter the processor failed - "))
fail = processor.index(failure)

status[fail] = 0

print("The current coordinator - ",max(processor))
print("The failed processor - ",failure)

print("processor status")
for i in range(n):
    print(processor[i]," ",status[i])

new_proc =[]
proc=[]
for i in range(n):
    if(status[i]!=0):
        new_proc.append(processor[i])

start = int(input("The processor that will initiate the election process - "))
index = new_proc.index(start)

temp1 = new_proc[0:index]
temp2 = new_proc[index:]

proc = temp2 + temp1

print(proc)

def election_process(pos):
    for i in range(len(proc)-1):
        print("Election message sent from ",proc[i]," to",proc[i+1])
    print("Election message sent from ",proc[len(proc)-1]," to",proc[0])

election_process(start)

#print("After election process the final coordinator is - ",max(proc))
