def fancy_name_plate(*names):
    for name in names:
        print('################################')
        print('##----------------------------##')
        print('##' + name.center(28, '-') + '##')
        print('##----------------------------##')
        print('################################')
def fancy_name_plate_defargs(name,length=26,symbol='&'):        
       print(symbol*length)
       print(symbol*2+(length-4)*'-'+symbol*2)
       print(symbol*2+name.center(length-4,'-')+symbol*2)
       print(symbol*2+(length-4)*'-'+symbol*2)
       print(symbol*length)

fancy_name_plate('thanmai','you the viewer','C3P0')
fancy_name_plate_defargs('sri',12,'%')
fancy_name_plate_defargs('sathvika',18,'o')



       
       
