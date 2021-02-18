import random
class PiggySimulator:
    def __init__(self,savings,start_balance,risk_level):
        self.savings=savings
        self.start_balance=start_balance
        self.risk_level=risk_level
        self.min_loss=0
        self.max_loss=0

    def gain_loss(self):
        if risk_level==1:
            self.min_loss,self.max_loss=-.0083,.0125
        elif risk_level==2:
            self.min_loss,self.max_loss=-.0125,.0208
        elif risk_level==3:
            self.min_loss,self.max_loss=-.0208,.0292
        elif risk_level==4:
            self.min_loss,self.max_loss=-.0250,.0375
        elif risk_level==5:
            self.min_loss,self.max_loss=-.0292,.0417
        elif risk_level==6:
            self.min_loss,self.max_loss=-.0333,.0458
        elif risk_level==7:
            self.min_loss,self.max_loss=-.0375,.0500

    def interest_sim(self):
        return random.randint(self.min_loss*1000000,
        self.max_loss*1000000)/1000000

    def new_balance(self,balance=self.start_balance,periods,percent_contribution):
        new_bal=balance*interest_sim()+percent_contribution*self.savings
        new_balance(balance=new_bal,periods,percent_contribution)
