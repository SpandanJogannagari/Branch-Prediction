class Bimodal:
    input_bits= None
    curr_value=None
    def __init__(self,pc_bits,trace): 
        self.pc_bits=pc_bits
        pc_bits = self.pc_bits
        total_predictions = 0
        miss_predicted=0
        with open(trace) as f:
            self.lines = f.readlines()
        high_val = int(pow(2,3)-1)
        low_val = 0
        mid_value = int((low_val+high_val+1)/2)
        range_predictor = pow(2,pc_bits)
        block=[mid_value for _ in range(range_predictor)]
        # print(high_val,low_val,mid_value)
        # print(block)
        with open(trace) as f:
            self.lines = f.readlines()
        for line in self.lines:
            total_predictions =total_predictions+1
            values= line.split(' ')
            addr=values[0]
            status= values[1].strip()
            int_value= int(addr, 16)
            bin_value= str(bin(int_value))           
            bin_value=bin_value[2:]           
            l=len(bin_value)
            bin_value=bin_value[:l-2]           
            l=len(bin_value)
            bin_value=bin_value[l-pc_bits:]           
            int_index=int(bin_value,2)
            if(block[int_index] < mid_value):
                temp='n'
            else:
                temp ='t'
            if (status!= temp):
                miss_predicted= miss_predicted+1
            if(status =='t'and (block[int_index] != high_val)):
                block[int_index]=block[int_index]+1
            elif(status =='n'and (block[int_index] != low_val)):
                block[int_index]=block[int_index]-1


        missrate = (miss_predicted/total_predictions) * 100
        print('OUTPUT')
        print('number of predictions:		',total_predictions)
        print('number of mispredictions:	',miss_predicted)
        print('misprediction rate:		{:.2f}%'.format(missrate))
        print('FINAL BIMODAL CONTENTS')
        for i in range(0,len(block)):
            print(i,"\t",block[i])
        
       