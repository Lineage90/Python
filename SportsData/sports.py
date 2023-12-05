import pandas as pd

df = pd.read_csv('C:/Users/LeeHB/SportsData/sports.csv')




df['일자'] = df['일자'].str.replace(r'\(\s*[가-힣]+\s*\)', '').apply(lambda x: f'{x[:2]}/{x[2:]}')

df['날짜'] = df['년도'].astype(str) + '/' + df['일자'].str.replace(r'\(\s*[가-힣]+\s*\)', '')

df = df.drop(['년도', '일자'], axis=1)
df = df.drop(['시간', '단체', '리그'], axis= 1)

df['경기 이름'] = df['홈팀'] + ' ' + df['스코어'] + ' ' + df['원정팀']

df = df.drop(['홈팀', '스코어', '원정팀'], axis=1)

df.rename(columns={'장소': '경기장'}, inplace=True)
print(df)

df.to_csv('sports_retouch.csv', index=False, encoding='utf-8-sig')