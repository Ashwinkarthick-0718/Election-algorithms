n = int(input("Enter the number of processors - "))

processors = []
status = []

for i in range(n):
    print("Enter the status of the process")
    status.append(int(input()))

for i in range(n):
    print("Entetr the processor id  - ")
    processors.append(int(input()))

print("processor     status \n")
for i in range(n):
    print(processors[i] , "            " , status[i])

End = int(input("Enter the processor which fails - "))

failure = processors.index(End)
status[failure] = 0

print('\n')
print("The current coordinator is the - ",max(processors),'\n')
print("The failed processor - ",End,'\n')

print("processor     status \n")
for i in range(n):
    print(processors[i] , "            " , status[i])

start = int(input("Enter the processs that will initiate the election - "))

def election_process(pos):
    for i in range(n):
        if(processors[pos-1] < processors[i]):
            if(processors[i] == End or status[i] == 0):
                print("Election message is sent from" , (pos) , "to", processors[(i)] , "\n")
                print(" - - - There is no response from ", processors[(i)] ,"to", (pos) , "\n")
            else:
                print("Election message is sent from" , (pos) , "to", processors[(i)] , "\n")
                print("+ + + Active response recived from ", processors[(i)] ,"to", (pos) , "\n")

    if pos < n:
        election_process(pos+1)


election_process(start)

rem_proc = []
new_proc = []

for i in range(n):
    if(status[i]== 0 ):
        rem_proc.append(processors[i])

for i in processors:
    if i not in rem_proc:
        new_proc.append(i)

print("After election processor the final coordinataor is - ",max(new_proc))







