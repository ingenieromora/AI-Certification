import random

def get_non_prize_door(host, num_doors, player_choice):
  i = 1
  while (i == host or i== player_choice ):
    i = (i+1)%(num_doors)

  return i

def switch_function(shown_door, num_doors, player_choice):
  i = 1
  while (i == shown_door or i== player_choice ):
    i = (i+1)%(num_doors)

  return i

def monty_hall_game(num_tests):


  win_switch_cnt = 0
  win_no_switch_cnt = 0
  lose_switch_cnt = 0
  lose_no_switch_cnt = 0
  doors = [0,1,2] #Get the doors
  num_doors = len(doors) #Get the number of doors
  
  
  for i in range(0,num_tests):
    door_with_prize = random.randint(0, num_doors-1) #Randomly choose the door with the wanted prize
    host = door_with_prize #The host knows which door has the prize
    #The player chooses initially a random door that s/he believes has the prize
    player_choice = random.randint(0, num_doors-1) 
    original_player_choice = player_choice
    shown_door = get_non_prize_door(host, num_doors, player_choice)
    
    switch = random.randint(0,1) == 1
    if switch == True:
      player_choice = switch_function(shown_door,num_doors, player_choice)
    
    if player_choice == host and switch == False:
      #Then the player wins from not switching
      #print('Player Wins (No switch) - The player chose door: ', player_choice,' Original choice: ',original_player_choice ,', Door with prize:', door_with_prize, ', Shown Door: ',shown_door )
      win_no_switch_cnt = win_no_switch_cnt + 1
    elif player_choice == host and switch == True:
      #Then the player wins from switching
      #print('Player Wins (switch) - The player chose door: ', player_choice,' Original choice: ',original_player_choice , ', Door with prize:', door_with_prize, ', Shown Door: ',shown_door )
      win_switch_cnt = win_switch_cnt +1
    elif player_choice != host and switch == False:
      #The player lost from not switching
      #print('Player Lost (No switch) - The player chose door: ', player_choice,' Original choice: ',original_player_choice , ', Door with prize:', door_with_prize, ', Shown Door: ',shown_door )
      lose_no_switch_cnt = lose_no_switch_cnt + 1
    elif player_choice != host and switch == True:
      #The player lost from switching
      #print('Player Lost (switch) - The player chose door: ', player_choice,' Original choice: ',original_player_choice , ', Door with prize:', door_with_prize, ', Shown Door: ',shown_door )
      lose_switch_cnt = lose_switch_cnt + 1
    else:
      print('SOMETHING IS WRONG')

  return win_no_switch_cnt,win_switch_cnt,lose_no_switch_cnt,lose_switch_cnt

numb_tests = 100
win_no_switch_cnt, win_switch_cnt, lose_no_switch_cnt, lose_switch_cnt = monty_hall_game(numb_tests)

print('Win after switch %: ', win_switch_cnt/ float(numb_tests))
print('Lose after switch %: ', lose_switch_cnt / float(numb_tests))
print('Win after no switch %: ', win_no_switch_cnt/ float(numb_tests))
print('Lose after No switch %: ', lose_no_switch_cnt/ float(numb_tests))