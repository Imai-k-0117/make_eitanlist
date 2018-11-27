import csv

PROLOG = '''<!DOCTYPE html>
<html lang="ja">
    <head>
        <meta charset="utf-8">
        <script type="text/javascript" src="http://www.francescomalagrino.com/BootstrapPageGenerator/3/js/jquery-ui"></script>
        <link href="http://www.francescomalagrino.com/BootstrapPageGenerator/3/css/bootstrap-combined.min.css" rel="stylesheet" media="screen">
        <script type="text/javascript" src="http://www.francescomalagrino.com/BootstrapPageGenerator/3/js/bootstrap.min.js"></script>
        <title>Word Book</title>
    </head>
    <body>
    	<h1  class="page-header">英単リスト</h1>

        <table class="table table-striped">
'''
HEADER = '''            <thead>
                <tr><th>%s</th><th>%s</th><th>%s</th></tr>
            </thead>
            <tbody>
'''
EPILOG = '''            </tbody>
        </table>

    </body>
</html>'''
RECORD = '                <tr><td>%s</td><td>%s</td><td>%s</td></tr>\n'

def read_csv(filename):
    with open(filename, encoding='shift_jis') as f:
        reader = csv.reader(f)
        data = []
        for i, row in enumerate(reader):
            if i == 0:
                header = row[:3]
            else:
                data.append(row)
        return header, data

def write_table(header, data, html):
    with open(html, 'w', encoding='utf-8') as f:
        f.write(PROLOG)
        f.write(HEADER % (header[0], header[1], header[2]))
        for record in data:
            f.write(RECORD % (record[0], record[1], record[2]))
        f.write(EPILOG)


if __name__ == '__main__':
    header, data = read_csv('output.csv')
    write_table(header, data, 'word.html')
