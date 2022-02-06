import random
   
available_tasks_list = [x for x in range(1,13)]
print ("A lista original is : " + str(available_tasks_list))
random_task = random.choice(available_tasks_list)
print ("A atividade selecionada foi : " + str(random_task))
