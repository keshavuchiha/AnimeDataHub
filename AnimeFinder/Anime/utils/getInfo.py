
def getInfo(details:list):
    info={}
    for row in details:
            row=row.split(':')
            row[0]=row[0].strip()
            row[1]=row[1].strip()
            if row[0]=='Score':
                info['score']=row[1]
            elif row[0]=='Episodes':
                temp=row[1].split(' ')
                info['episodeCount']=temp[0].strip()
                info['type']=temp[1].strip()
            elif row[0]=='Status':
                info['status']=row[1]
            elif row[0]=='Aired':
                temp=row[1].split('to')
                info['start']=temp[0].strip()
                info['end']=temp[1].strip()
            elif row[0]=='Popularity':
                temp=row[1].split('#')
                info['popularity']=temp[0].strip()
                if(info['popularity'][-1]=='('):
                    info['popularity']=info['popularity'][:-2]
                info['rank']=temp[1].strip()
                if(info['rank'][-1]==')'):
                    info['rank']=info['rank'][:-1]
            elif row[0]=='Rating':
                temp=row[1].split('-')
                info['rating']=temp[0].strip()
                info['ratingDetail']=temp[1].strip()
            elif row[0]=='Duration':
                temp=row[1].split(' ')
                info['duration']=temp[0].strip()
            elif row[0]=='Studios':
                temp=row[1].split(',')
                info['studios']=temp
    return info