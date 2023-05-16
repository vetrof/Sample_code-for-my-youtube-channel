from pathlib import Path
import pandas

link_obj = Path('temp/').glob('*.csv')

for file in link_obj:
    csv = pandas.read_csv(file)
    csv.to_excel(f'{str(file)[:-4]}.xlsx')
