# Caroline Fairhust, Fabiola Martin, Ian Watt, Tim Doran, Martin Bland, William J Brackenbury, 2023.

import sys, csv, re

codes = [{"code":"43C3.11","system":"readv2"},{"code":"65QA.00","system":"readv2"},{"code":"65VE.00","system":"readv2"},{"code":"A788.00","system":"readv2"},{"code":"A788.11","system":"readv2"},{"code":"A788000","system":"readv2"},{"code":"A788100","system":"readv2"},{"code":"A788200","system":"readv2"},{"code":"A788300","system":"readv2"},{"code":"A788400","system":"readv2"},{"code":"A788500","system":"readv2"},{"code":"A788U00","system":"readv2"},{"code":"A788X00","system":"readv2"},{"code":"A788y00","system":"readv2"},{"code":"A788z00","system":"readv2"},{"code":"A789.00","system":"readv2"},{"code":"A789000","system":"readv2"},{"code":"A789100","system":"readv2"},{"code":"A789200","system":"readv2"},{"code":"A789300","system":"readv2"},{"code":"A789400","system":"readv2"},{"code":"A789900","system":"readv2"},{"code":"A789A00","system":"readv2"},{"code":"AyuC.00","system":"readv2"},{"code":"AyuCB00","system":"readv2"},{"code":"AyuCD00","system":"readv2"},{"code":"B56..00","system":"readv2"},{"code":"R109.00","system":"readv2"}];
REQUIRED_CODES = 1;
with open(sys.argv[1], 'r') as file_in, open('charlson-comorbidity-index-potential-cases.csv', 'w', newline='') as file_out:
    csv_reader = csv.DictReader(file_in)
    csv_writer = csv.DictWriter(file_out, csv_reader.fieldnames + ["charlson-comorbidity-index---primary-identified"])
    csv_writer.writeheader();
    codes_identified = 0;
    for row in csv_reader:
        newRow = row.copy();
        for cell in row:
            # Iterate cell lists (e.g. codes)
            for item in re.findall(r'\(([^,]*)\,', row[cell]):
                if(item in list(map(lambda code: code['code'], codes))): codes_identified+=1;
                if(codes_identified>=REQUIRED_CODES):
                    newRow["charlson-comorbidity-index---primary-identified"] = "CASE";
                    break;
            if(codes_identified>=REQUIRED_CODES): break;
        if(codes_identified<REQUIRED_CODES):
            newRow["charlson-comorbidity-index---primary-identified"] = "UNK";
        codes_identified=0;
        csv_writer.writerow(newRow)
