def import_data(file_name):
    headers = []
    data = []

    with open(file_name, 'r') as f:
        headers = f.readline().strip().split(',')
        for line in f:
            data.append(line.strip().split(','))

    return headers, data


def main():
    input_data_file_name = 'data.csv'
    output_data_file_name = 'sorted_data.csv'

    headers, data = import_data(input_data_file_name)
    freq_rating_idx = headers.index('frequency rating')

    if freq_rating_idx == -1:
        raise Exception('Data must contain a \'frequency rating\' column')

    sorted_data = sorted(data, key=lambda x: int(x[freq_rating_idx]))

    # save sorted_data.csv
    with open(output_data_file_name, 'w') as f:
        f.write(','.join(headers) + '\n')
        for row in sorted_data:
            f.write(','.join(row) + '\n')


if __name__ == '__main__':
    main()
