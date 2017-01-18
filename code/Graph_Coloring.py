'''
Code by Akshay Reddy (reddyak@iu.edu)

'''


import timeit
from decimal import Decimal
import random

# for case 3
colors = ['Red', 'Blue', 'Green', 'Yellow', 'Black','Purple','Brown','White','Megenta','Safforon','Gold',
          'Silver','Red-blue','Greem-yello','Purple-Black','Brown-White','Mengenta-saffrin','safforon-Gold'
          'Silver-Grey','Grey','Orange','Grey-Orange','Grey-Red','Orange-Red','Red-Green','Red-Black','Red-Brown',
          'Red-Purple','Red-Megenta','Red-safrron','Yello-white','Saffron-White','Blue-Yellow','Blue-Purple',
          'Blue-Brown','Blue-White','Blue-Safforon','Blue-Gold','Blue-Silver','Blue-Grey','Blue-Orange'
          'Yellow-Purple','Yellow-White','Yellow-Safforon','Yellow-Gold','Yellow-Silver','Yello-Grey','Yellow-Orange'
          'Megenta--Gold','Megenta-Grey','Megenta-Orange','Megenta-Purple','Lime']


# for case 1 and 2
#colors=['Red', 'Blue', 'Green', 'Yellow', 'Black','Purple'] 


states=['WA', 'DE', 'DC', 'WI', 'WV', 'HI', 'FL', 'WY', 'NH', 'NJ', 'NM', 'TX', 
       'LA', 'NC', 'ND', 'NE', 'TN', 'NY', 'PA', 'RI', 'NV', 'VA', 'CO', 'CA', 
       'AL', 'AR', 'VT', 'IL', 'GA', 'IN', 'IA', 'OK', 'AZ', 'ID', 'CT', 'ME', 'MD', 
       'MA', 'OH', 'UT', 'MO', 'MN', 'MI', 'KS', 'MT', 'MS', 'SC', 'KY', 'OR', 'SD']

neighbors = {}
colors_of_states = {}

Graph_Choice=input("Enter\n1-Simple Graph\n2-Complete Graph\n3-Bipartite Graph\n")

if Graph_Choice==1:
	f=open("Simple_Graph.txt","r")
	contents=f.readlines()
	for i in contents:
		temp=i.replace('\n','').split(',')
		neighbors[temp.pop(0)]=temp

elif Graph_Choice==2:
	f=open("Complete_Graph.txt","r")
	contents=f.readlines()
	for i in contents:
		temp=i.replace('\n','').split(',')
		neighbors[temp.pop(0)]=temp

elif Graph_Choice==3:
	#case 4 Creating a Bipartite Graph
	for i in states[:25]:
		neighbors[i]=states[25:random.randint(26,len(states)-1)]

	for i in states[25:]:
		neighbors[i]=states[:random.randint(0,24)]

else:
	print "Invalid Input"
	exit()

Algorithm_Choice=input("Enter\n1-Simple Greedy\n2-DSatur\n")


def Dsatur(simple_order):

	New_Order=[]
	List_Of_Count=[]
	for x in simple_order:
		count=0
		try:
			for y in neighbors.get(x):
				color_of_neighbor = colors_of_states.get(y)
				if color_of_neighbor in colors:
					count+=1
			List_Of_Count.append(count)
		except TypeError:
			return simple_order
    
    #creating a list based on the saturation level in descending order
	for i in range(len(simple_order)):                 
		index=List_Of_Count.index(max(List_Of_Count))
		New_Order.append(simple_order[index])
		List_Of_Count[index]=-1

	return New_Order

def Simple_Greedy(state, color):
	if Algorithm_Choice==1:
		order=neighbors.get(state)
	elif Algorithm_Choice==2:
		order=Dsatur(neighbors.get(state))
	else:
		print "Invalid Choice"
		exit()

	for neighbor in order:
		color_of_neighbor = colors_of_states.get(neighbor)
		if color_of_neighbor == color:
			return False
	return True

def get_color_for_state(state):
    for color in colors:
        if Simple_Greedy(state, color):
            return color

def main():
    for state in states:
        colors_of_states[state] = get_color_for_state(state)

    print colors_of_states


start=Decimal(timeit.default_timer(),5)
main()
end=Decimal(timeit.default_timer(),5)

print "Excution time="+str(end-start)