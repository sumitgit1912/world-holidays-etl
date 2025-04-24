import subprocess

def run_extract():
    print('Running Extract step...')
    subprocess.run(['python', 'extract.py'], check = True)

def run_load():
    print('Runnig Load step...')
    subprocess.run(['python', 'load.py'], check = True)

def run_transform():
    print('Running Transfrom step...')
    subprocess.run(['python', 'transform.py'], check = True)

def main():
    print('Starting ETL pipeline...\n')
    run_extract()
    run_transform()
    run_load()
    print('\nETL pipeline completed succesfully.')

if __name__ == "__main__":
    main()