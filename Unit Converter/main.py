import os

def Menu():
    Op = ["in->cm", "cm->in", "ft->m", "m->ft", "yd->m", "m->yd", "mile->km", "km->mile", "nmile->m", "m->nmile",
          "acre->sqm", "sqm->acre", "gal(US)->l", "l->gal(US)", "gal(UK)->l", "l->gal(UK)", "pc->km", "km->pc", "km/h->m/s", "m/s->km/h",
          "Oz->g", "g->Oz", "lb->kg", "kg->lb", "Atm->Pa", "Pa->Atm", "mmHg->Pa", "Pa->mmHg", "hp->kW", "kW->hp",
          "kgf/sqcm->Pa", "Pa->kgf/sqcm", "kgf.m->J", "J->kgf.m", "lbf/sqin->kPa", "kPa->lbf/sqin", "F->C", "C->F", "J->cal", "cal->J"]
    Code = ["[00]", "[01]", "[02]", "[03]", "[04]", "[05]", "[06]", "[07]", "[08]", "[09]",
          "[10]", "[11]", "[12]", "[13]", "[14]", "[15]", "[16]", "[17]", "[18]", "[19]",
          "[20]", "[21]", "[22]", "[23]", "[24]", "[25]", "[26]", "[27]", "[28]", "[29]",
          "[30]", "[31]", "[32]", "[33]", "[34]", "[35]", "[36]", "[37]", "[38]", "[39]"]
    print("************************************************************************** Unit Converter **************************************************************************\nOpCodes:\n")
    for i in range(0,len(Op)):
        if (i+1)%10==0 :
            print(Code[i]+Op[i])
        else: print(Code[i]+Op[i], end="    ")
    print("*********************************************************************************************************************************************************************\n")
    return Op

def Tform(num, Code):
    match Code:
        case '00': #in->cm
            return float(num)*2.54
        case '01': #cm->in
            return float(num)/2.54
        case '02': #ft->m
            return float(num)*0.3048
        case '03': #m->ft
            return float(num)/0.3048
        case '04': #yd->m
            return float(num)*0.9144
        case '05': #m->yd
            return float(num)/0.9144
        case '06': #mile->km
            return float(num)*1.60934
        case '07': #km->mile
            return float(num)/1.60934
        case '08': #nmile->m
            return float(num)*1852
        case '09': #m->nmile
            return float(num)/1852
        case '10': #acre->sqm
            return float(num)*0.0015625
        case '11': #sqm->acre
            return float(num)/0.0015625
        case '12': #gal(US)->l
            return float(num)*3.78541
        case '13': #l->gal(US)
            return float(num)/3.78541
        case '14': #gal(UK)->l
            return float(num)*4.54609
        case '15': #l->gal(UK)
            return float(num)/4.54609
        case '16': #pc->km
            return float(num)*3.086e+13
        case '17': #km->pc
            return float(num)/3.086e+13
        case '18': #km/h->m/s
            return float(num)*0.277778
        case '19': #m/s->km/h
            return float(num)/0.277778
        case '20': #Oz->g
            return float(num)*28.3495
        case '21': #g->Oz
            return float(num)/28.3495
        case '22': #lb->kg
            return float(num)*0.453592
        case '23': #kg->lb
            return float(num)/0.453592
        case '24': #Atm->Pa
            return float(num)*101325
        case '25': #Pa->Atm
            return float(num)/101325
        case '26': #mmHg->Pa
            return float(num)*133.322
        case '27': #Pa->mmHg
            return float(num)/133.322
        case '28': #hp->kW
            return float(num)*0.7457
        case '29': #kW->hp
            return float(num)/0.7457
        case '30': #kgf/sqcm->Pa
            return float(num)*98066.5
        case '31': #Pa->kgf/sqcm
            return float(num)/98066.5
        case '32': #kgf.m->J
            return float(num)*9.80665
        case '33': #J->kgf.m
            return float(num)/9.80665
        case '34': #lbf/sqin->kPa
            return float(num)*6.89476
        case '35': #kPa->lbf/sqin
            return float(num)/6.89476
        case '36': #F->C
            return (float(num)-32)*5/9
        case '37': #C->F
            return (float(num)*9/5)+32
        case '38': #J->cal
            return float(num)/4.2
        case '39': #cal->J
            return float(num)*4.2
        case default:
            return "Error"

def main():
    Op= Menu()
    num= input('Number: ')
    Code= input('OpCode: ')
    res= Tform(num,Code)
    print(f"\n{num} {Op[int(Code)]} {res}")
    print("\n*********************************************************************************************************************************************************************")
    clr= []
    clr= input('Clear: ')
    if (len(clr)>0):
        os.system('cls')
        main()

main()