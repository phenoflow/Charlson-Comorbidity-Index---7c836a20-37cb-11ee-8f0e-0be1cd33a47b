# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2023.

import sys, csv, re

codes = [{"code":"7609.00","system":"readv2"},{"code":"7609300","system":"readv2"},{"code":"7609400","system":"readv2"},{"code":"7609y11","system":"readv2"},{"code":"7609z00","system":"readv2"},{"code":"760C300","system":"readv2"},{"code":"760C500","system":"readv2"},{"code":"760F300","system":"readv2"},{"code":"760F400","system":"readv2"},{"code":"761D800","system":"readv2"},{"code":"A704.00","system":"readv2"},{"code":"A704z00","system":"readv2"},{"code":"C310400","system":"readv2"},{"code":"G85..11","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('charlson-comorbidity-index-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["severe-charlson-comorbidity-index---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["severe-charlson-comorbidity-index---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["severe-charlson-comorbidity-index---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
