import csv
import json

ADS = 'ads'
CATEGORY = 'categories'


def csv_to_json(csv_file_path, json_file_path, model):
    result = []
    with open(csv_file_path, encoding='utf-8') as csvf:
        for row in csv.DictReader(csvf):
            to_add = {
                'model': model,
                'pk': int(row['id'] if 'id' in row else row['Id'])
            }
            if 'id' in row:
                del row['id']
            else:
                del row['Id']

            if 'is_published' in row:
                if row['is_published'] == 'True':
                    row['is_published'] = True
                else:
                    row['is_published'] = False

            if 'price' in row:
                row['price'] = int(row['price'])

            to_add['fields'] = row
            result.append(to_add)

    with open(json_file_path, 'w', encoding='utf-8') as jsonf:
        jsonf.write(json.dumps(result, indent=4, ensure_ascii=False))


csv_to_json(f'{ADS}.csv', f'{ADS}.json', 'ads.ad')
csv_to_json(f'{CATEGORY}.csv', f'{CATEGORY}.json', 'ads.category')
