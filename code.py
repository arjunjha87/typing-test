import time as t
import matplotlib.pyplot as plt

times = []
mistakes = 0

print("This program will help you type faster.")
input("Press enter to start.")

while(len(times)<5):
    start = t.time()
    word = input("Type the word:")
    end = t.time()
    time_elapsed = end - start
    times.append(time_elapsed)
    if(word.lower() != "programming"):
        mistakes += 1

print("You made " +
      str(mistakes) + " mistake(s)") 
print("Lets see your progress.")
t.sleep(2)

x = [1,2,3,4,5]
y = times
plt.plot(x,y)
legend = ["1","2","3","4","5",]
plt.xticks(x,legend)
plt.ylabel("Time in seconds")
plt.xlabel("Attempt")

plt.show()


import time as t
import matplotlib.pyplot as plt

times = []
mistakes = 0

print("This program will help you type faster.")
input("Press enter to start.")

while(len(times)<5):
    start = t.time()
    word = input("Type the word:")
    end = t.time()
    time_elapsed = end - start
    times.append(time_elapsed)
    if(word.lower() != "programming"):
        mistakes += 1

print("You made " +
      str(mistakes) + " mistake(s)") 
print("Lets see your progress.")
t.sleep(2)

x = [1,2,3,4,5]
y = times
plt.plot(x,y)
legend = ["1","2","3","4","5",]
plt.xticks(x,legend)
plt.ylabel("Time in seconds")
plt.xlabel("Attempt")

plt.show()


