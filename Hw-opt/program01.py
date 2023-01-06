# -*- coding: utf-8 -*-
'''
An e-cash system allows the registered users to transfer electronic currency
    units between one another. We shall use the following symbol to denote
    the currency unit: Ħ.
    To transfer Ħ’s, the players resort to intermediary agents who manage the
    transactions at the price of a transaction fee. The transaction fees
    are based on varying percentages decided by the intermediary agents.

The aim of this program is to process a log of transactions between the
    players of the e-cash system and compute:
    1) a list with the final balance of every account of the involved
       player’s accounts;
    2) a list with the final amount earned by every intermediary;
    3) a list in which, for every intermediary, a nested list reports the
       remaining debts of the player’s accounts (0 if no debt was accumulated,
       or a negative integer otherwise).
    Results (1), (2) and (3) should be elements of a tuple.

In particular, the following function should be designed:
    ex1(acn1, acn2, acn3, imd_acn1, imd_acn2, init_amount, transact_log)
    where
    – acn1, acn2 and acn3 are the account numbers of player 1, 2 and 3,
      respectively;
    – imd_acn1 and imd_acn2 are the account numbers of intermediaries 1 and 2,
      respectively;
    – init_amount is the initial amount in the accounts of the three players
      (we assume that all players start with the same starting amount);
    – the accounts of intermediaries start with a balance of 0Ħ;
    – transact_log is a list of transactions; every transaction is a tuple,
      which consists of the following elements:
      · a pair of integers indicating the account number of the sender and
        the account number of the receiver;
      · the transferred amount;
      · the account number of the intermediary;
      · the percentage of the transaction fee (to be computed based on the
        transferred amount).

For example, the following tuple:
      ((0x44AE, 0x5B23), 800, 0x1612, 4)
    indicates a transaction transferring 800Ħ from the account number
    0x44AE to the account number 0x5B23, with the help of the intermediary
    who will receive 4% of 800Ħ (thus, 32Ħ) on their account at 0x1612.
    As a result,
    - the balance of the sender (0x44AE) will decrease by
        800 + 32 = 832Ħ,
    - the balance of the recipient (0x5B23) will increase by
        800Ħ,
    - and the intermediary will earn and deposit on their account (0x1612)
        32Ħ.

Notice that if the funds in the sender’s account are insufficient,
    the transaction is declared invalid by the intermediary. The intermediary
    will get the fee anyway from the sender, if there are enough Ħ’s in the
    sender’s account. If the sender’s account cannot pay the transaction fee,
    the intermediary will get all the remaining funds and take its part
    from the next transactions to the sender until the debt is paid.
    In the example above, if there were only 700Ħ in account 0x44AE,
    the intermediary would earn 32Ħ and the amount in 0x44AE would decrease
    to 668Ħ. If there were only 10Ħ in account 0x44AE, the intermediary would
    earn 10Ħ and the amount in 0x44AE would decrease to 0Ħ; also, the
    intermediary would hold a credit of 22Ħ from the sender. The sender would be
    obliged to repay the 22Ħ getting the due amount from the transactions
    received later until the debt is extinguished.

    If a debt is accumulated towards two intermediary agents, funds go to the
    intermediary having the highest credit first, and the remainder goes to
    the other intermediary, for as much as is left. For instance, let player 1
    owe 300Ħ to intermediary 1 and 200Ħ to intermediary 2; as player 1
    receives 400Ħ, 300Ħ are paid to intermediary 1 and 100Ħ are paid to
    intermediary 2. If the same amount is due to both intermediary agents,
    the payback is evenly split. For instance, let player 2 owe 100Ħ to
    intermediary 1 and 100Ħ to intermediary 2; as player 2 receives 100Ħ,
    50Ħ go to each intermediary.

As an example,
    ex1(0x5B23, 0xC78D, 0x44AE, 0x1612, 0x90FF, 1000,
        [ ((0x44AE, 0x5B23),  800, 0x1612,  4),
          ((0x44AE, 0xC78D),  800, 0x90FF, 10),
          ((0xC78D, 0x5B23),  400, 0x1612,  8),
          ((0x44AE, 0xC78D), 1800, 0x90FF, 12),
          ((0x5B23, 0x44AE),  100, 0x1612,  2)
        ])
    returns
    ( [2098, 568, 0], [66, 268], [ [0, 0, 0], [0, 0, -28] ] )
    because all players start with 1000Ħ in their account and, at the end,
    – the balance of player 1 amounts to 2098Ħ,
    – the balance of player 2 amounts to 568Ħ,
    – the balance of player 3 amounts to 0Ħ,
    – intermediary 1 earned 66Ħ,
    – intermediary 2 earned 268Ħ,
    – player 3 still owes 28Ħ to intermediary 2.

NOTE: the timeout for this exercise is of 2 seconds for each test.

WARNING: Make sure that the uploaded file is UTF8-encoded
    (to that end, we recommend you edit the file with Spyder)

'''
def ex1(acn1, acn2, acn3, imd_acn1, imd_acn2, init_amount, transaction_log):
    account1=acn1  #renaming
    account2=acn2 #"
    account3=acn3 #"
    initialamount=init_amount #"
    balance1=initialamount #initializing dictionary
    balance2=initialamount #"
    balance3=initialamount #"
    balance1x=0 #"
    balance2x=0 #"
    dizionarioscemo={account1:balance1,account2:balance2,account3:balance3,imd_acn1:balance1x,imd_acn2:balance2x} #main balance dictionary 
    
    dizionariodebiti={ #debt dictionary
    account1:{imd_acn1:0,imd_acn2:0},
    account2:{imd_acn1:0,imd_acn2:0},
    account3:{imd_acn1:0,imd_acn2:0}
    }

    for transaction in transaction_log: 
        id1,id2=transaction[0] #unpacking transaction_log
        amount=transaction[1] #"
        idinter=transaction[2] #"
        fee=transaction[3]*amount/100 #"
        
        if dizionarioscemo[id1]>=fee+amount:#everything goes well
            dizionarioscemo[id1]-=(amount+fee)
            dizionarioscemo[id2]+=amount   
            dizionarioscemo[idinter]+=(fee) 
        elif dizionarioscemo[id1]>=fee:#transaction invalid and paid fee
            dizionarioscemo[id1]-=(fee)
            dizionarioscemo[idinter]+=(fee) 
        elif  dizionarioscemo[id1]>0:#has some money but not enough for the fee (debt)
            dizionariodebiti[id1][idinter]=(fee-dizionarioscemo[id1])
            dizionarioscemo[idinter]+=(dizionarioscemo[id1])
            dizionarioscemo[id1]=0
        else:#has no money for the fee (severe debt)
            dizionariodebiti[id1][idinter]=fee 
            
    for account in dizionariodebiti:#check debt
        while True:
                if all([t==0 for t in dizionariodebiti[account].values()]):# no debt yeee :)
                    break
                elif dizionarioscemo[account]==0:# poor (absolutely no pennies):(
                    break
                
                # balanced debt :|
                if dizionariodebiti[account][imd_acn1]==dizionariodebiti[account][imd_acn2]:
                    totale_debito = dizionariodebiti[account][imd_acn1] + dizionariodebiti[account][imd_acn2]
                    
                    if totale_debito <= dizionarioscemo[account]: #debt free!!! every debt gets paid
                        dizionarioscemo[account]-=totale_debito
                        dizionarioscemo[imd_acn1]+=dizionariodebiti[account][imd_acn1]
                        dizionarioscemo[imd_acn2]+=dizionariodebiti[account][imd_acn2]
                        dizionariodebiti[account][imd_acn1]=0
                        dizionariodebiti[account][imd_acn2]=0
                        break
        
                    else: #whats left of the founds is split evenly
                        dizionarioscemo[imd_acn1]+=(dizionarioscemo[account])/2
                        dizionarioscemo[imd_acn2]+=(dizionarioscemo[account])/2
                        dizionariodebiti[account][imd_acn1]-=(dizionarioscemo[account])/2
                        dizionariodebiti[account][imd_acn2]-=(dizionarioscemo[account])/2
                        dizionarioscemo[account]=0
                        break
                    
                # preferential debt -_-
                if dizionariodebiti[account][imd_acn1] < dizionariodebiti[account][imd_acn2]:#which debt is the first to get paid?
                    id_debitone=imd_acn2
                else:
                    id_debitone=imd_acn1
                    
                if dizionariodebiti[account][id_debitone] <= dizionarioscemo[account]: #pay the biggest debt
                    dizionarioscemo[account]-=dizionariodebiti[account][id_debitone]
                    dizionarioscemo[id_debitone]+=dizionariodebiti[account][id_debitone]
                    dizionariodebiti[account][id_debitone]=0
                    #NO BREAK so on the next iteration the smallest debt is paid
                else:#give everything to the bigger creditor an still be in debt :(((
                    dizionariodebiti[account][id_debitone]-=dizionarioscemo[account]
                    dizionarioscemo[id_debitone]+=dizionarioscemo[account]
                    dizionarioscemo[account]=0
                    break
                
    phynix=( #return set (the int casting isnt necessary but iwas trying it out)
            [int(dizionarioscemo[account1]),int(dizionarioscemo[account2]),int(dizionarioscemo[account3])],
            [int(dizionarioscemo[imd_acn1]),int(dizionarioscemo[imd_acn2])],
            [[int(-dizionariodebiti[account1][imd_acn1]),int(-dizionariodebiti[account2][imd_acn1]),int(-dizionariodebiti[account3][imd_acn1])],
            [int(-dizionariodebiti[account1][imd_acn2]),int(-dizionariodebiti[account2][imd_acn2]),int(-dizionariodebiti[account3][imd_acn2])]]
            )
    
    return(phynix)  

if __name__ == '__main__':
    # Insert your own tests here
    pass
