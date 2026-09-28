# While loop

# A while loop keeps repeating a block of code as long as a condition is True,
# and stops the moment it becomes False. 
# No condition change inside it = it never stops.

# Real-life situation/scenario

# Say you forgot your email password and you're trying different guesses to get back in
# But You don't know in advance how many guesses it'll take — could be 1,
# could be 10, could be that you never get it right. 
# What you do know is a condition: "keep trying until I successfully log in" 
# (or "until I run out of attempts,"
# if the email service locks you out after too many tries).

count = 0
while count < 5:
    print(count)
    count = count + 1
    
# count = 0                    -> count starts at 0
# while count < 5:             -> Python checks: is 0 < 5? Yes (True) -> enter loop

# --- Pass 1 ---
# print(count)                 -> prints 0 (current value, before it changes)
# count = count + 1            -> right side: take count's CURRENT value (0), add 1 -> 1
#                               -> that result (1) is stored back into count
# loop body done -> jump back UP to "while" line to re-check
# while count < 5:             -> is 1 < 5? Yes (True) -> enter loop again

# --- Pass 2 ---
# print(count)                 -> prints 1
# count = count + 1            -> take count's current value (1), add 1 -> 2 -> stored in count
# while count < 5:             -> is 2 < 5? Yes -> enter loop again

# --- Pass 3 ---
# print(count)                 -> prints 2
# count = count + 1            -> 2 + 1 -> 3 -> stored in count
# while count < 5:             -> is 3 < 5? Yes -> enter loop again

# --- Pass 4 ---
# print(count)                 -> prints 3
# count = count + 1            -> 3 + 1 -> 4 -> stored in count
# while count < 5:             -> is 4 < 5? Yes -> enter loop again

# --- Pass 5 ---
# print(count)                 -> prints 4
# count = count + 1            -> 4 + 1 -> 5 -> stored in count
# while count < 5:             -> is 5 < 5? NO (False) -> loop stops here

# Loop is done. Output printed: 0 1 2 3 4
# Notice count itself ends up at 5 -- but 5 never gets printed, because
# the check happens BEFORE the body runs on that final round, and it
# fails right there.


# In the above while loop, the condition becomes false when count is 5. 
# That is when the loop stops. 
# If we are interested to run block of code once the condition is no longer true, 
# we can use else.

number = 0
while number < 5:
    print(number)
    number = number + 1
else:
    print(number)
    
# Inside the loop (runs while true):

# Pass 1: prints 0, then number = number + 1 → number becomes 1
# Pass 2: prints 1, then number becomes 2
# Pass 3: prints 2, then number becomes 3
# Pass 4: prints 3, then number becomes 4
# Pass 5: prints 4, then number becomes 5
# Check again: is 5 < 5? No → loop stops, body doesn't run this time

# Now the else: block fires — because the loop ended by the condition going false (nobody hit break), so Python runs it:
# print(number) → number is currently 5 → prints 5

#  The Anatomy of a while Loop
# To understand it deeply, you need to see that every while loop has **three secret
# parts** working together. If you miss one, it breaks.
    
# 1.  The Starting Point: Where do we begin?
# 2.  The Condition (The Guard): The rule that keeps the loop running.
# 3.  The Change (The Update): Something that changes the starting point so the 
# condition can eventually become False.

battery = 80 # 1. starting point
while battery < 100: # 2. the condition (Guard asks: "is 80 < 100?")
    print('charging....', battery, '%')
    battery = battery + 1 # 3. the change (we must add to the battery!)
print('Battery is full') 
# this continues untill the battery is 100.

# tiny rocket example:
rocket = 5
while rocket > 0:
    print('Rocket is ready to Launch in:', rocket)
    rocket = rocket - 1
print("Blast off!")

numbers = 0
while numbers < 5:
    print(numbers)
    numbers = numbers + 1
    if numbers == 3:
        break
    
    
guest_list = ['Alex', 'Ajax', 'Ben', 'Chris', 'Mia', 'Sam']
looking_for = 'Chris'
index = 0
while index < len(guest_list):
    name = guest_list[index]
    print('Checking:', name)
    if name == looking_for:
        print('Found', looking_for, '!stopping the search.')
        break
    index = index + 1
    
