class Gshare:
    input_bits= None
    curr_value=None
    def __init__(self,pc_bits,reg_bits,trace): 
        self.pc_bits=pc_bits
        self.reg_bits=reg_bits
        pc_bits = self.pc_bits
        reg_bits = self.reg_bits
        total_predictions = 0
        miss_predicted=0
        xbits =''
        for i in range(0,reg_bits):
            xbits=xbits+'0'
        
        high_val = int(pow(2,3)-1)
        low_val = 0
        mid_value = int((low_val+high_val+1)/2)
        range_predictor = pow(2,pc_bits)
        block=[mid_value for _ in range(range_predictor)]
        #print('block len',len(block))

 
        with open(trace) as f:
            self.lines = f.readlines()
        for line in self.lines:
        
            total_predictions =total_predictions+1
            #print(total_predictions)
            values= line.split(' ')
            addr=values[0]
            status= values[1].strip()
            int_value= int(addr, 16)
            bin_value= str(bin(int_value))           
            bin_value=bin_value[2:]           
            l=len(bin_value)
            bin_value=bin_value[:l-2]           
            l=len(bin_value)
            bin_value1=bin_value[l-pc_bits:l-reg_bits]           
            xor_input = bin_value[l-reg_bits:]
            #print(bin_value1,xor_input)
            
            
            c=self.xor1(xor_input,xbits)
            #print('function output',c)


            res=bin_value1+c
            #print(res)
            int_index=int(res,2)
            if(block[int_index] < mid_value):
                temp='n'
            else:
                temp ='t'
            if (status!= temp):
                miss_predicted= miss_predicted+1
            if(status =='t'):
                xbits = '1'+xbits
                l_xbits=len(xbits)
                xbits = xbits[:l_xbits-1]
                if(block[int_index] != high_val):
                    block[int_index]=block[int_index]+1
            elif(status =='n'):
                xbits = '0'+xbits
                l_xbits=len(xbits)
                xbits = xbits[:l_xbits-1]
                if (block[int_index] != low_val):
                    block[int_index]=block[int_index]-1


        missrate = (miss_predicted/total_predictions) * 100
        print('OUTPUT')
        print('number of predictions:		',total_predictions)
        print('number of mispredictions:	',miss_predicted)
        print('misprediction rate:		{:.2f}%'.format(missrate))
        print('FINAL GSHARE CONTENTS')
        for i in range(0,len(block)):
            print(i,"\t",block[i])

    def xor1(self,s1,s2):
        s1=list(s1)
        s2=list(s2)
            #print(s1,s2)
        l1=len(s1)
        p=0
        bin_value2=''
        while (p < l1):
            if (s1[p]==s2[p]):
                bin_value2=bin_value2+'0'
            else:
                bin_value2=bin_value2+'1'
            p=p+1
        return bin_value2
    
  
        


    