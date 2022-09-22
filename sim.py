import sys
from smith import Smith
from bimodal import Bimodal
from gshare import Gshare
from hybrid import Hybrid

class sim:
    def main(args):
        #print('input arguements length is ',len(args))
        if(len(args)== 3):
            Branch_type = str(args[0])
            if (Branch_type=='smith'):
                counter_bits = int(args[1])
                trace = str(args[2])
                branch_inp = Smith(counter_bits,trace)
            elif(Branch_type=='bimodal'):
                pc_bits=int(args[1])
                trace = str(args[2])
                branch_inp = Bimodal(pc_bits,trace)

        if(len(args) == 4):
            Branch_type = str(args[0])
            pc_bits=int(args[1])
            reg_bits=int(args[2])
            trace = str(args[3])
            branch_inp = Gshare(pc_bits,reg_bits,trace)


        if(len(args)== 6):
            Branch_type = str(args[0])
            k=int(args[1])
            pc_bits=int(args[2])
            reg_bits=int(args[3])
            bimod_bits2=int(args[4])
            trace = str(args[5])
            branch_inp = Hybrid(k,pc_bits,reg_bits,bimod_bits2,trace)

    main(sys.argv[1:])

# main(1,10,20,30,40,50,60,70)
