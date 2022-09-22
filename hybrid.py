class Hybrid:
    def __init__(self,k,pc_bits,reg_bits,bimod_bits,trace): 
        self.pc_bits=pc_bits
        self.reg_bits=reg_bits
        self.bimod_bits=bimod_bits
        pc_bits = self.pc_bits
        reg_bits = self.reg_bits
        bimod_bits=self.bimod_bits
        self.k = k
        k=self.k
        total_predictions = 0
        miss_predicted=0

        hybrid_high_val = 3
        hybrid_low_val = 0
        hybrid_mid_value = 2

        high_val = 7
        low_val = 0
        mid_value = 4

        gshare_range = pow(2,pc_bits)
        bimodal_range = pow(2,bimod_bits)

        hybrid_block=[1 for _ in range(pow(2,k))]
        bimodal_block=[mid_value for _ in range(bimodal_range)]
        gshare_block=[mid_value for _ in range(gshare_range)]

        xbits =''
        for i in range(0,reg_bits):
            xbits=xbits+'0'
        
        with open(trace) as f:
            self.lines = f.readlines()
        for line in self.lines:
            total_predictions =total_predictions+1
            values= line.split(' ')
            addr=values[0]
            status= values[1].strip()

            bimodal_index =self.bimodelIndex(addr,bimod_bits)
            hybrid_index = self.getIndex(addr,k)

            int_value= int(addr, 16)
            bin_value= str(bin(int_value))           
            bin_value=bin_value[2:]           
            l=len(bin_value)
            bin_value=bin_value[:l-2]           
            l=len(bin_value)
            bin_value1=bin_value[l-pc_bits:l-reg_bits]           
            xor_input = bin_value[l-reg_bits:]
            s1=list(xor_input)
            s2=list(xbits)
            l1=len(s1)
            p=0
            bin_value2=''
            while (p < l1):
                if (s1[p]==s2[p]):
                    bin_value2=bin_value2+'0'
                else:
                    bin_value2=bin_value2+'1'
                p=p+1
            res=bin_value1+bin_value2
            gshare_index=int(res,2)


            bimodal_prediction = self.bimodal_predict(bimodal_block,bimodal_index,mid_value)
            gshare_prediction = self.gshare_predict(gshare_block,gshare_index,mid_value)

            if (hybrid_block[hybrid_index] >= hybrid_mid_value):
                if (status != gshare_prediction):
                    miss_predicted= miss_predicted+1
                if(status=='t'):
                    if (gshare_block[gshare_index]<high_val):
                        gshare_block[gshare_index]=gshare_block[gshare_index]+1
                if(status=='n'):
                    if (gshare_block[gshare_index]>low_val):
                        gshare_block[gshare_index]=gshare_block[gshare_index]-1
            
            else:
                if (status != bimodal_prediction):
                    miss_predicted=miss_predicted+1
                if(status =='t'):
                    if(bimodal_block[bimodal_index]<high_val):
                        bimodal_block[bimodal_index]=bimodal_block[bimodal_index]+1
                if(status =='n'):
                    if(bimodal_block[bimodal_index]>low_val):
                        bimodal_block[bimodal_index]=bimodal_block[bimodal_index]-1
            
            if (status=='t'):
                xbits = '1'+xbits
            else:
                xbits = '0'+xbits
            l_xbits=len(xbits)
            xbits = xbits[:l_xbits-1]

            if(bimodal_prediction==status and gshare_prediction != status):
                if(hybrid_block[hybrid_index]!= hybrid_low_val):
                    hybrid_block[hybrid_index]=hybrid_block[hybrid_index]-1
            elif(bimodal_prediction!=status and gshare_prediction==status):
                if(hybrid_block[hybrid_index]!= hybrid_high_val):
                    hybrid_block[hybrid_index]=hybrid_block[hybrid_index]+1
            
        missrate = (miss_predicted/total_predictions) * 100
        print('OUTPUT')
        print('number of predictions:		',total_predictions)
        print('number of mispredictions:	',miss_predicted)
        print('misprediction rate:		{:.2f}%'.format(missrate))
        print('FINAL CHOOSER CONTENTS')
        for i in range(0,len(hybrid_block)):
            print(i,"\t",hybrid_block[i])
        print('FINAL GSHARE CONTENTS')
        for i in range(0,len(gshare_block)):
            print(i,"\t",gshare_block[i])
        print('FINAL BIMODAL CONTENTS')
        for i in range(0,len(bimodal_block)):
            print(i,"\t",bimodal_block[i])



    def bimodelIndex(self,addr,bimod_bits):
        int_val= int(addr, 16)
        bin_val= str(bin(int_val))           
        bin_val=bin_val[2:]           
        c=len(bin_val)
        bin_val=bin_val[:c-2]           
        c=len(bin_val)
        bin_val=bin_val[c-bimod_bits:]           
        int_ind=int(bin_val,2)
        return int_ind       

    def getIndex(self,addr,k):
        int_val= int(addr, 16)
        bin_val= str(bin(int_val))           
        bin_val=bin_val[2:]           
        li=len(bin_val)
        bin_val=bin_val[:li-2]           
        li=len(bin_val)
        bin_val=bin_val[li-k:]           
        int_ind=int(bin_val,2)
        return int_ind

    
    def bimodal_predict(self,bimodal_block,index,mid_val):
        if (bimodal_block[index]<mid_val):
            temp='n'
        else:
            temp='t'
        return temp

    def gshare_predict(self,gshare_block,index,mid_val):
        if (gshare_block[index]<mid_val):
            temp='n'
        else:
            temp='t'
        return temp
    

    





