class Smith:
    input_bits= None
    curr_value=None
    total_predictions = 0
    def __init__(self,counter_bits,trace):
        self.counter_bits=counter_bits
        input_bits = self.counter_bits
        total_predictions = 0
        miss_predicted=0
        with open(trace) as f:
            self.lines = f.readlines()
        high_val = int(pow(2,input_bits)-1)
        low_val = 0
        mid_value = int((low_val+high_val+1)/2)
        curr_value = mid_value
        #print(high_val,low_val,mid_value,curr_value)
        for line in self.lines:
            total_predictions =total_predictions+1
            values= line.split(' ')
            status= values[1].strip()
            if(curr_value < mid_value):
                temp='n'
            else:
                temp ='t'
            if (status!= temp):
                miss_predicted= miss_predicted+1
            if(status =='t'and (curr_value != high_val)):
                curr_value=curr_value+1
            elif(status =='n'and (curr_value != low_val)):
                curr_value=curr_value-1
        missrate = (miss_predicted/total_predictions) * 100
        print('OUTPUT')
        print('number of predictions:		',total_predictions)
        print('number of mispredictions:	',miss_predicted)
        print('misprediction rate:		{:.2f}%'.format(missrate))
        print('FINAL COUNTER CONTENT:		',curr_value)
    
        



         