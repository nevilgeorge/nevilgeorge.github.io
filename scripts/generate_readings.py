# generate_readings.py
import csv
import codecs
import yaml

def main():
    readings = []
    with open('nevils_readings.csv', 'r') as f:
        reader = csv.DictReader(codecs.EncodedFile(f, 'utf8', 'utf_8_sig'))
        for row in reader:
            readings.append({
                'title': row['Name'],
                'author': row['Author'],
                'link': row['Link']
            })

    readings.reverse()

    with open('readings.yaml', 'w') as f:
        yaml.dump(readings, f)


if __name__ == '__main__':
    main()
