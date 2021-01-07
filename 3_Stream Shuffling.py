import random

input_stream = range(0, 100)
output_list = list(input_stream)

for (i, v) in enumerate(input_stream):
    rand_id = random.randint(i, len(input_stream) - 1) #Selecting a random index from the input stream, excluding the indexes already iterated over & shuffled
    if rand_id != i: #No point in swapping the same value with itself
        output_list[i], output_list[rand_id] = output_list[rand_id], output_list[i] #Swapping values between current index and randomly selected index

#---------------------------------------
print(output_list)