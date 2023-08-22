import queue
import random
import string

quantum_no=int(input("Enter the quantum no = "))
no_of_processes=int(input("Enter the no of processes = "))
all_tasks=[]
arrival_times=[]
ready_que=queue.Queue()
running_que=queue.Queue()
last_elements=[]
turn_around_times=[]
#Storing and creating queue's for processes
for i in range(no_of_processes):
   arrival_time=int(input(f"Enter the arrival time for process {i+1} = "))
   arrival_times.append(arrival_time)
   my_queue = queue.Queue()
   execution_time=random.randint(1,10)
   for j in range(execution_time):
        
        alphabet = string.ascii_uppercase
        # Generate a random uppercase letter
        random_uppercase = random.choice(alphabet)
        my_queue.put(random_uppercase)
        if j==execution_time:
           last_elements.append(random_uppercase)
   all_tasks.append(my_queue)
#Printing the summary of process
for i in range(no_of_processes):

    print(f"Process {i+1} :- \n")
    print(f"Execution time for process {i+1} = ",all_tasks[i].qsize()," Quantum no.")
    print(f"Arrival time = {arrival_times[i]}")
    task = list(all_tasks[i].queue)
    print(f"Tasks Elements for operation {i+1} = {task}\n")

#Working:-
#initliazing flag list

flag=[0]*no_of_processes
least_arrival_time=min(arrival_times)

counter=0
latest_task_que=least_arrival_time

while(sum(flag)!=no_of_processes):
   for j in range(no_of_processes):
    k=0
    if j==0:
     least_arrival_time=least_arrival_time+k+j
    else:
     least_arrival_time+=1
    print(f"Time :- {least_arrival_time} ")
    print("---------------------------")
    if counter == 0:
            Process_to_be_executed = [index for index, arrival in enumerate(arrival_times) if arrival <= least_arrival_time]
            if Process_to_be_executed:
                for d in Process_to_be_executed:
                    print(f"Process ID: {d+1}")
                    print("State: Enqueuing in Ready Queue")
                    ready_que.put(d)
                    arrival_times[d] = 1000
    
    if (counter==0 and j==0):
        pass
    else:
        temp=running_que.get()
        if not(all_tasks[temp].empty()):

            ready_que.put(temp)
            # print(f"State:-Putting Process{temp+1} in ready que")
        else:
           flag[temp]=1
    if sum(flag)==no_of_processes:
      print("All processes are processed")
      break
    latest_task_que=ready_que.get()      

    for k in range(quantum_no):
      
      if (counter==0 and  j==0):
        if all_tasks[j].empty():  
           break
        else:     
           
           if k!=0:
            least_arrival_time=least_arrival_time+k
            print(f"Time :- {least_arrival_time} ")
            print("---------------------------")

           if(k==0):
            
            running_que.put(latest_task_que)
           print(f"State:- Process {latest_task_que+1} in Running Que  \n")         
           if latest_task_que in last_elements and all_tasks[latest_task_que].qsize()==1:
             turn_around_times.append(latest_task_que)
           if not(all_tasks[latest_task_que].empty()):
            if k==0:
             
                print(f"PC :- {all_tasks[latest_task_que].queue[k+1]} ")
            else:

                print(f"PC :- {all_tasks[latest_task_que].queue[0]} ")
           print(f"Instruction Register :-Task {all_tasks[latest_task_que].get()} is executing \n")
      else:
         if all_tasks[latest_task_que].empty():      
           break
         else:     
           
           if k!=0:
            least_arrival_time=least_arrival_time+k
            print(f"Time :- {least_arrival_time} ")
            print("---------------------------")
           if(k==0):
             running_que.put(latest_task_que)
           print(f"State:- Process {latest_task_que+1} in Running Que  ")
           print(f"Instruction Register :-Task {all_tasks[latest_task_que].get()} is executing \n")

           if not(ready_que.empty()):
            if all_tasks[ready_que.queue[0]].empty():
                pc=all_tasks[latest_task_que].queue[0]
                print(f"PC :- {pc} \n")
            else:
                print(f"PC :- {all_tasks[ready_que.queue[0]].queue[0]} \n")
        #    else:
        #       print(f"PC :- {all_tasks[latest_task_que].queue[0]} \n")

   counter+=1
   
 




